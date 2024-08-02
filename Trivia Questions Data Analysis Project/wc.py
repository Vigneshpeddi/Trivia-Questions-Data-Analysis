from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import json

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def get_word_frequency(data):
    all_text = ' '.join([item['Question'] + ' ' + item['Answer'] for item in data])
    words = [word.lower() for word in all_text.split() if word.isalpha() and word.lower() not in STOPWORDS]
    word_frequency = Counter(words)
    return word_frequency

def plot_word_frequency(word_frequency):
    common_words = word_frequency.most_common(10)
    words, counts = zip(*common_words)
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Most Frequent Words in Trivia')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
