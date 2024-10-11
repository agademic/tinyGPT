# tinyGPT
Repository for educational purposes. Here, we are going to recreate the basic GPT codebase and train the model on a toy dataset.

## tokenizer
To train the model on a corpus, we first need to define a vocabulary based on a certain corpus of text (i.e. the vocabulary will contain all tokens within the corpus). 

A simple method would be to put every unique word from that corpus into our vocabulary, but that would result in a very large and inefficient vocabulary (the english language has over a million words, where 170k words are currently in use).

A commonly used method by researchers is to train a tokenizer on a corpus. The resulting tokenizer will contain not whole words but rather tokens (i.e. subwords). For example `"tokenizers in language models"` will be encoded to `[5963, 12509, 304, 4221, 4211]` and decoded back to `[b'token', b'izers', b' in', b' language', b' models']`. 

In our case, we will train the model to predict the next character rather than the next token. Thus, we will create a vocabulary from characters.