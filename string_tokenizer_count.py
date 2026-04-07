import re

def tokenizer_counter(sentence):
    res = {}
    sentence = sentence.lower()
    sentence = re.sub('[!"\'?;:]', " ", sentence)
    for s in sentence.split():
        if s in res:
            res[s] += 1
        else:
            res[s] = 1
    return dict(sorted(res.items()))
    
