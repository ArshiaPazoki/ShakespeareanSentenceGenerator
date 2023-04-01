# ShakespeareanSentenceGenerator
This is a simple language model that generates Shakespearean-style sentences using bigram frequency analysis. The model is based on the Shakespeare's Hamlet corpus from the NLTK library.
# Requirements
- Python 3.x
- NLTK library

# Installation
1. Install Python 3.x on your machine if it's not already installed. You can download Python from the official website: https://www.python.org/downloads/
2. Install the NLTK library by running the following command in your terminal:
```
pip install nltk
```
3. Download the Shakespeare's Hamlet corpus from the NLTK library by running the following Python code in your terminal:
```
import nltk
nltk.download('shakespeare-hamlet')
```
# Usage
1. Clone or download this repository to your local machine.
2. Open a terminal window and navigate to the directory where you saved the repository.
3. Run the following command to generate a sentence:
```
python main.py
```
4. You can modify the length of the sentence and the seed word by editing the sentence list in the main.py file. For example, to generate a sentence of 20 words starting with the word "Friend", you can modify the sentence list as follows:
```python
sentence = ['Friend']
for i in range(20):
    ...
```

# Contributing
Contributions to this project are welcome. If you find a bug or have an idea for a new feature, please open an issue on GitHub or submit a pull request with your changes.

# License
This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit/) file for details.