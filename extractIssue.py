import json
import nltk
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz
words = stopwords.words('english')+["doesn’t"]


def extract(str):
    fp = json.load(open('problems.json','r'))
    # print(fp)
    cleaned = [i for i in str.lower().split() if i not in words]
    # print(cleaned)
    val = []
    for a in cleaned:
        for b in fp:
            rat= fuzz.ratio(a,b)
            if rat >50:
                # print(a,b)
                val.append(b)
    # print(set(val))
    return val

# extract(str)