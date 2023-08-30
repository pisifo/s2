#task1 stemming
from nltk .stem import PorterStemmer
ps = PorterStemmer()
print(ps.stem("better"))
# nltk. download('wordnet')
# nltk. download(omw-1.4')
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
print(wnl.lemmatize('better'))

#task2
import nltk
with open("candidate1.txt", "r", encoding="utf-8") as f:
    text=f.read()
    print(text)
    a = nltk.word_tokenize(text)
    print(a)


from nltk.tokenize import word_tokenize
words = word_tokenize(text)

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]

from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
lemm_words=[wnl.lemmatize(word) for word in words]

# Find the number of different words between stemmed_words and lemm_words
different_words = set(stemmed_words) ^ set(lemm_words)
num_different_words = len(different_words)

print("Number of different words:", num_different_words)

#%%
from nltk.stem import PorterStemmer
ps = PorterStemmer()
print(ps.stem("campaigning"))

#%%
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
print(wnl.lemmatize("campaining"))

#%%
from nltk import word_tokenize
with open("candidate1.txt", "r", encoding="utf-8") as f:
   words = word_tokenize(f.read())
   different_words = []
   for word in words:
       if ps.stem(word) != wnl.lemmatize(word):
           different_words.append((ps.stem(word),wnl.lemmatize(word)))
   print(different_words)
   print(len(different_words))


#task 2
import pandas as pd
df = pd.read_csv("news.csv")
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
print(analyzer.polarity_scores(df.iloc[0,-1]))

positive_news = []
negative_news = []
neutral_news = []

for index, row in df.iterrows():
    compound_score = analyzer.polarity_scores(row[-1])['compound']
    if compound_score >= 0.05:
        positive_news.append(row[-1])
    elif compound_score <= -0.05:
        negative_news.append(row[-1])
    else:
        neutral_news.append(row[-1])
print(len(positive_news),len(negative_news),len(neutral_news))

print('c')
print('d')