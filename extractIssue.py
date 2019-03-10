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
            if fuzz.ratio(a,b) >60:
                print(a,b)
                val.append(b)
    print(set(val))
    return set(val)

# extract(str)