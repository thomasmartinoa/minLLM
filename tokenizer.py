text = "hello world"

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
