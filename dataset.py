import torch
import torch.nn as nn

file = open("data/input.txt","r",encoding="utf-8")
text = file.read()
file.close()

chars = sorted(set(text))

stoi = {}
number = 0

for ch in chars:
    stoi[ch] = number
    number += 1

itos = {}

for ch in stoi:
    number = stoi[ch]
    itos[number]=ch 


def encode(text):
    result=[]

    for ch in text:
            number = stoi[ch]
            result.append(number)

    return result

def decode(numbers):
    result = ""

    for number in numbers:
        char = itos[number]
        result = result + char

    return result


data = encode(text)

context_length = 4

inputs = []
targets = []

for start in range(0,len(data)-context_length):
    input_data = data[start:start + context_length]
    target_data = data[start+1:start + context_length +1]

    inputs.append(input_data)
    targets.append(target_data)

input_tensor = torch.tensor(inputs)
target_tensor = torch.tensor(targets)

batch_size = 4

random_indexes = torch.randint(0,len(input_tensor),(batch_size,))

batch_input = input_tensor[random_indexes]
batch_target = target_tensor[random_indexes]



vocab_size = len(chars)

embedding_size = 8

embedding = nn.Embedding(vocab_size,embedding_size)


batch_embedding = embedding(batch_input)

linear = nn.Linear(context_length * embedding_size,vocab_size)

batch_size = batch_input.shape[0]

flattened_batch = batch_embedding.reshape(
    batch_size,context_length*embedding_size
)

logits = linear(flattened_batch)


first_ex_logits = logits[0]

predicted_token_id = torch.argmax(first_ex_logits)

predicted_token_id = predicted_token_id.item()

predicted_char = itos[predicted_token_id]

loss_function = nn.CrossEntropyLoss()

correct_next_tokens = batch_input[:,-1]
print(correct_next_tokens)
print(correct_next_tokens.shape)


loss = loss_function(logits,correct_next_tokens)

print(loss.item())
