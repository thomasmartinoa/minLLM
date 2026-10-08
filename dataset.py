import torch

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


print(batch_input)
print(batch_target)

