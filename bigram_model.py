import torch
import torch.nn as nn
from torch.nn import functional as F
from tokenizer import tokenizer

# hyperparameter setting
batch_size = 32
block_size = 8  # max context length
max_iters = 3000
eval_interval = 300
learning_rate = 1e-2
device = "cuda" if torch.cuda.is_available() else "cpu"
eval_iters = 200

torch.manual_seed(8)

with open("data/tinyshakespeare.txt", "r") as f:
    text = f.read()

tok = tokenizer()
char_to_int, int_to_char = tok.create_character_vocabulary(text)

# train and test splits
data = torch.tensor(tok.encode(text), dtype=torch.long)
train_size = int(0.9 * len(data))
train_data = data[:train_size]
val_data = data[train_size:]

# data loading
def get_batch(split: str = "train"):
    data = train_data if split == "train" else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,)) # get random starting indices
    x = torch.stack([data[i:i + block_size] for i in ix])
    y = torch.stack([data[i + 1:i + block_size + 1] for i in ix])

    return x, y