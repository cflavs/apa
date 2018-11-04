import numpy as np 
from heap import *

file = open("teste.txt", "r")
text = file.read()
file.close()

def get_frequency(text):
    frequency = {}
    for character in text:
        if not character in frequency:
            frequency[character] = 1
        else:
            frequency[character]+=1
    return frequency

dict_values = get_frequency(text)
freq = np.array(list(dict_values.values()))
#print(freq)
heapSort(freq,len(freq))
#print(freq)