import re;
def tokenize(sentence):
    sentence = sentence.lower()
    sentence = re.sub('[^a-z0-9]', " ", sentence)
    return sentence.split()