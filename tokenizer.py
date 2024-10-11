

class tokenizer:
    def __init__(self):
        self.characters = None
        self.vocab_size = None
        self.char_to_int = None
        self.int_to_char = None

    def create_character_vocabulary(self, text):
        characters = sorted(list(set(text)))
        self.vocab_size = len(characters)

        self.char_to_int = {char: i for i, char in enumerate(characters)}
        self.int_to_char = {i: char for i, char in enumerate(characters)}

        return self.char_to_int, self.int_to_char

    def encode(self, text):
        if self.char_to_int is None:
            raise ValueError('Character vocabulary not created')
        return [self.char_to_int[char] for char in text]

    def decode(self, encoded_text):
        if self.int_to_char is None:
            raise ValueError('Character vocabulary not created')
        return ''.join([self.int_to_char[i] for i in encoded_text])


if __name__ == '__main__':
    text = 'hello world'

    tok = tokenizer()
    tok.create_character_vocabulary(text)
    print(tok.char_to_int)
    print(tok.encode("hell"))
