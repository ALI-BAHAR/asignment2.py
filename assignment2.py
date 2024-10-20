# -*- coding: utf-8 -*-
"""Untitled46.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10AtwUkZSjr6kLjzJY6fyFHOjQnCpvTeJ
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

nltk.download('punkt')
nltk.download('stopwords')

#Function to calculate the frequency length of the words#
def get_frequency_distribution(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    return FreqDist(word for word in words if word.isalnum() and word not in stop_words)

#Function to summarize text which use the word frequencies#
def summarize_text(text, target_length, freq_dist):
    sentences = sent_tokenize(text)

    #Scoring the sentences based on word frequencies#
    scored_sentences = [(sum(freq_dist.get(word, 0) for word in word_tokenize(sentence)), sentence) for sentence in sentences]
    scored_sentences.sort(reverse=True)

#Selecting sentences when the target length is reached#
    summary_sentences = []
    current_length = 0
    for score, sentence in scored_sentences:
        sentence_length = len(word_tokenize(sentence))
        if current_length + sentence_length <= target_length:
            summary_sentences.append(sentence)
            current_length += sentence_length
        else:
            break

    return TreebankWordDetokenizer().detokenize(summary_sentences)

#Function to perform hierarchical summarization#
def hierarchical_summarization(text, max_tokens):
    sentences = sent_tokenize(text)
    freq_dist = get_frequency_distribution(text)
    segments = []
    current_length = 0

    while current_length < len(sentences):
        # Define segment as a set of sentences fitting the token size
        segment_text = ' '.join(sentences[current_length:current_length + max_tokens])
        summary = summarize_text(segment_text, max_tokens // 2, freq_dist)
        segments.append(summary)
        current_length += max_tokens

    return ' '.join(segments)

#Example usage#
text1 = "Your long text 1 goes here..."
text2 = "Your long text 2 goes here..."

#Calculating the total number of tokens across the two texts#
total_length = len(word_tokenize(text1)) + len(word_tokenize(text2))

#Computing the target lengths proportionally#
target_length1 = int((len(word_tokenize(text1)) / total_length) * 4000)
target_length2 = int((len(word_tokenize(text2)) / total_length) * 4000)

#Generate hierarchical summaries#
summary1 = hierarchical_summarization(text1, target_length1)
summary2 = hierarchical_summarization(text2, target_length2)

#Combine the two summaries#
final_summary = summary1 + " " + summary2

#Final summary
print("Final Summary:")
print(final_summary)
