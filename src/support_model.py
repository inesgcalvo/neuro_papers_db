import re
import pandas as pd
import numpy as np

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences



def preprocess_text(text):
    '''
    Preprocesses a given text by converting to lowercase, removing non-alphabetic characters,
    tokenizing, and removing English stop words.

    Parameters:
    - text (str): The input text to be preprocessed.

    Returns:
    str: The preprocessed text.
    '''
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    processed_text = ' '.join(tokens)
    return processed_text



def column_embeddings(df, col, n_components):
    '''
    Perform word embedding and dimensionality reduction on a text column in a DataFrame.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the text column.
    - col (str): The name of the text column in the DataFrame.
    - n_components (int, optional): The number of components to reduce the embeddings to.
      Defaults to 50.

    Returns:
    pandas.DataFrame: A DataFrame containing the reduced-dimensional embeddings as new columns.

    Raises:
    - ValueError: If the specified column 'col' is not found in the DataFrame.
    - ValueError: If 'n_components' is not a positive integer.

    Note:
    This function tokenizes the text in the specified column, performs word embedding using
    an embedding layer, flattens the embeddings, and then applies PCA for dimensionality reduction.
    '''
    df[col] = df[col].astype(str)

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(df[col])
    total_words = len(tokenizer.word_index) + 1
    sequences = tokenizer.texts_to_sequences(df[col])
    padded_sequences = pad_sequences(sequences)
    embedding_dim = 100  
    model = tf.keras.models.Sequential([tf.keras.layers.Embedding(input_dim=total_words, 
                                                                  output_dim=embedding_dim, 
                                                                  input_length=padded_sequences.shape[1])])

    embeddings = model.predict(padded_sequences)
    embeddings_flat = np.array([emb.flatten() for emb in embeddings])
    pca = PCA(n_components=n_components)
    embeddings_reduced = pca.fit_transform(embeddings_flat)
    embedding_columns = [f'{col}_emb_{i}' for i in range(n_components)]
    embeddings_df = pd.DataFrame(embeddings_reduced, columns=embedding_columns)
    return embeddings_df



def preprocess_input(title, abstract):
    '''
    Preprocesses the input title and abstract text.

    Parameters:
    - title (str): The title text to be preprocessed.
    - abstract (str): The abstract text to be preprocessed.
    '''
    title = preprocess_text(title)
    abstract = preprocess_text(abstract)
    return title, abstract



def generate_input_embeddings(title, abstract):
    '''
    Generates input embeddings for the given title and abstract.

    Parameters:
    - title (str): The preprocessed title text.
    - abstract (str): The preprocessed abstract text.
    '''
    title_embedding = column_embeddings(pd.DataFrame({'input': [title]}), 'input', n_components=1).iloc[0]
    abstract_embedding = column_embeddings(pd.DataFrame({'input': [abstract]}), 'input', n_components=1).iloc[0]
    return pd.concat([title_embedding, abstract_embedding], axis=0)



def predict_journal(model, input_embeddings):
    '''
    Predicts the journal using the given model and input embeddings.

    Parameters:
    - model: The trained machine learning model.
    - input_embeddings (pd.Series): Embeddings of the input text.
    '''
    input_embeddings_reshaped = input_embeddings.values.reshape(1, -1)
    prediction = model.predict(input_embeddings_reshaped)
    probability = model.predict_proba(input_embeddings_reshaped)
    return prediction, probability



def get_results(prediction, probability, label_encoder):
    '''
    Decodes the prediction and organizes results.

    Parameters:
    - prediction: The predicted journal.
    - probability: The probability of the prediction.
    - label_encoder: The label encoder used for encoding and decoding.
    '''
    decoded_prediction = label_encoder.inverse_transform(prediction)
    result = [{"journal": journal, "probability": prob} for journal, prob in zip(decoded_prediction, probability[0])]
    return result



def predict_journal_for_input(title, abstract, model, label_encoder):
    '''
    Predicts the journal for the given input title and abstract.

    Parameters:
    - title (str): The title text.
    - abstract (str): The abstract text.
    - model: The trained machine learning model.
    - label_encoder: The label encoder used for encoding and decoding.
    '''
    title, abstract = preprocess_input(title, abstract)
    input_embeddings = generate_input_embeddings(title, abstract)
    prediction, probability = predict_journal(model, input_embeddings)
    result = get_results(prediction, probability, label_encoder)
    return result



#### When columns contain lists of text:
'''
def preprocess_list_of_text(text_list):
    processed_texts = []
    for text in text_list:
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]
        processed_text = ' '.join(tokens)
        processed_texts.append(processed_text) 
    return processed_texts
    
columns_to_preprocess_list = ['authors', 'terms']
for column in columns_to_preprocess_list:
    data[column] = data[column].apply(preprocess_list_of_text)
''';