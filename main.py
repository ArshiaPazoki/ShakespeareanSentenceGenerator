import random
import nltk
from nltk.corpus import gutenberg
from nltk import bigrams, word_tokenize

# Load the corpus and tokenize it into sentences
corpus = gutenberg.sents('shakespeare-hamlet.txt')

# Create a list of bigrams for each sentence
bigram_list = [bigrams(sent) for sent in corpus]

# Create a dictionary to store the frequency of each bigram
freq_dict = {}
for sent in bigram_list:
    for bigram in sent:
        if bigram[0] not in freq_dict:
            freq_dict[bigram[0]] = {}
        if bigram[1] not in freq_dict[bigram[0]]:
            freq_dict[bigram[0]][bigram[1]] = 0
        freq_dict[bigram[0]][bigram[1]] += 1

# Calculate the probabilities for each bigram
for word1 in freq_dict:
    total = sum(freq_dict[word1].values())
    for word2 in freq_dict[word1]:
        freq_dict[word1][word2] /= total

# Generate a sentence
# start with a seed word
sentence = ['Friend']
# generate 10 words
for i in range(10):
    # get the last word in the sentence
    word1 = sentence[-1]
    # get the possible next words
    choices = list(freq_dict[word1].keys())
    # get the probability of each next word
    probabilities = list(freq_dict[word1].values())
    # randomly select the next word based on the probability distribution
    word2 = random.choices(choices, probabilities)[0]
    # add the next word to the sentence
    sentence.append(word2)

# print the generated sentence
print(' '.join(sentence))
