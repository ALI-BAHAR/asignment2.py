# assignment2.py
# Hierarchical Text Summarization

## Project Description
This project implements hierarchical text summarization using NLTK (Natural Language Toolkit) in Python. The goal is to summarize long texts by segmenting them and reducing each segment using frequency-based sentence scoring.

### Key Features:
- **Frequency-based Sentence Selection**: Sentences are scored based on word frequency, and the most relevant ones are selected for the summary.
- **Token-based Hierarchical Summarization**: Text is broken down into segments, summarized independently, and then combined into a final summary.
- **Text Processing with NLTK**: Tokenization, stopword removal, and frequency analysis are performed using NLTK tools.

## Project Structure

- `summarizer.py`: Main Python script that contains the summarization functions.
- `README.md`: This file, providing an overview of the project.

## How it Works

1. **Word Frequency Distribution**: The frequency of words in the input text is calculated, excluding stopwords and punctuation.
2. **Sentence Scoring**: Sentences are scored based on how often important words appear.
3. **Hierarchical Summarization**: Text is divided into segments of predefined size, and each segment is summarized individually. The summaries are then combined to create the final summarized text.
4. **Adjustable Token Limit**: The length of the summary for each text is determined by its proportional length in relation to the tota
