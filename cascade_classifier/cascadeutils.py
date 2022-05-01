import os

def generate_negative_description_file():
    with open('neg.txt', 'w') as f:
        for filename in os.listdir('../dataset/negative'):
            f.write('../dataset/negative/' + filename + '\n')

generate_negative_description_file()