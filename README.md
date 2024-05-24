import math

text = str(input("Enter the text: "))
key = str(input("Enter the key: "))

if len(text) <= len(key):
    cropped_key = key[:len(text)]
else:
    ceil = math.ceil(len(text) / len(key))
    new_key = []
    for i in range(0, ceil):
        for l in key:
            new_key.append(l)
    cropped_key = new_key[:len(text)]

def encrypt(text, key):
    cipher_list = []
    print(key)
    for (t, k) in zip(text, key):
        position = ord(t)
        position_list = ord(k)
        letter = chr(position + position_list)
        cipher_list.append(letter)
    t = "".join(cipher_list)
    print(t)

encrypt(text, cropped_key)
