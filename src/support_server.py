import os
import nltk
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')


def remove_stopwords(word_list):
    '''
    '''
    stop_words = set(stopwords.words('english'))
    filtered_list = [word for word in word_list if word.lower() not in stop_words]
    return filtered_list



def cloud_for_column(df, column, journal):
    '''
    ''' 
    titles = df[column][df['journal'] == journal]
    titles_words = []
    for row in titles:
        for word in row.split():
            word = word.lower()
            titles_words.append(word)

    titles_words_filtered = remove_stopwords(titles_words)

    freq_words = {}
    count_description = Counter(titles_words_filtered)
    common_words = count_description.most_common()

    for word, frequency in common_words:
        freq_words[word] = frequency

    font_path = "/windows/fonts/georgia.ttf"

    word_cloud = WordCloud(width=800, 
                            height=400, 
                            background_color=None,
                            mode='RGBA',
                            font_path = font_path,
                            colormap='Greys').generate_from_frequencies(freq_words)

    fig = plt.figure(figsize=(10, 5), facecolor='none')
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')   
    return fig
