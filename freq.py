import sys
import re
import nltk
from nltk.probability import FreqDist
import pandas as pd
from pymystem3 import Mystem

# nltk.download('punkt') # uncomment if need
# nltk.download('stopwords') # uncomment if need

with open(sys.argv[1]) as f:
    mystem = Mystem()
    stopwords = set(nltk.corpus.stopwords.words('russian') + [' ', 'это'])

    text = f.read()
    unpuncted = re.sub(r'\W+', ' ', text)
    lemmarized = mystem.lemmatize(unpuncted)
    stopworded = [i for i in lemmarized if not i in stopwords]
    freqDisted = FreqDist(stopworded)
    
    df_fdist = pd.DataFrame.from_dict(freqDisted, orient='index')
    df_fdist.columns = ['count']
    df_fdist.index.name = 'word'
    df_fdist = df_fdist.sort_values(by=['count'], ascending=False)
    df_fdist.to_excel("output.xlsx")
