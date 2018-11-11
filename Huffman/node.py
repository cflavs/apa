class Node:
    def __init__(self,freq,char=None,left=None,right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    def __getitem__(self,key):
        return self.char[key]
    def get_frequency(text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 1
            else:
                frequency[character]+=1
        return frequency

