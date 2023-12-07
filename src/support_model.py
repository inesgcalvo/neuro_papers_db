import pandas as pd
import numpy as np
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences



def preprocess_text(text):
    '''
    '''
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    processed_text = ' '.join(tokens)
    return processed_text



def column_embeddings(df, col, n_components=50):
    '''
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



def predict_journal(title, abstract, model, label_encoder):
    '''
    '''
    title = preprocess_text(title)
    abstract = preprocess_text(abstract)

    input_df = pd.DataFrame({'title': [title], 'abstract': [abstract]})
    embeddings_df = column_embeddings(input_df, 'title')
    embeddings_df = pd.concat([embeddings_df, column_embeddings(input_df, 'abstract')], axis=1)

    input_embeddings_reshaped = embeddings_df.values.reshape(1, -1)
    prediction = model.predict(input_embeddings_reshaped)
    probability = model.predict_proba(input_embeddings_reshaped)

    decoded_prediction = label_encoder.inverse_transform(prediction)
    result = [{"journal": journal, "probability": prob} for journal, prob in zip(decoded_prediction, probability[0])]

    return result