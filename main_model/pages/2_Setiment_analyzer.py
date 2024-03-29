#Importing modules
import pandas as pd 
import numpy as np 
import re 
import string 
import matplotlib.pyplot as plt 
import seaborn as sns
import nltk 
import warnings
import streamlit as st

warnings.filterwarnings('ignore')

df = pd.read_csv(r'C:\Users\DevenShah\Desktop\test\SunHacks2022\tweets_analysis\train_E6oV3lV.csv')
df.head()

#Preprocessing the dataset
#remove a pattern in input text
def remove_pattern(input_txt, pattern):
  r = re.findall(pattern, input_txt)
  for word in r:
    input_txt = re.sub(word,"",input_txt)
  return input_txt

#removing twitter handles
df['clean_tweet'] = np.vectorize(remove_pattern)(df['tweet'],"@[\w]*")
df.head()

#removing special characters, numbers, and symbols
df['clean_tweet'] = df['clean_tweet'].str.replace("[^a-zA-Z#]"," ")
df.head()

#remove short words
df['clean_tweet'] = df['clean_tweet'].apply(lambda x: " ".join([w for w in x.split() if len(w)>3]))
df.head()
st.write("This the dataset which has being cleared of all the unwanted data from the sentences") 
st.write(df.head())

#Tokenization (sentence -> broken -> words(tokens))
tokenized_tweet = df['clean_tweet'].apply(lambda x: x.split())
tokenized_tweet.head()

#Stemming
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
tokenized_tweet = tokenized_tweet.apply(lambda sentence: [stemmer.stem(word) for word in sentence])
tokenized_tweet.head()

#combine tokens to a single sentence
for i in range(len(tokenized_tweet)):
  tokenized_tweet[i] = " ".join(tokenized_tweet[i])

df['clean_tweet'] = tokenized_tweet
df.head()

#Visualize the frequent words

all_words = " ".join([sentence for sentence in df[ 'clean_tweet' ]])

from wordcloud import WordCloud
wc = WordCloud(background_color='pink', width=800, height=500, random_state=42, max_font_size=100).generate(all_words)

#graph
plt.figure(figsize=(15,8))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.markdown("<h4 style='text-align: center; color: white;'>Visualizaton the frequent words</h4>", unsafe_allow_html=True)
st.pyplot()

#visualizaton of frequent positive words

all_words = " ".join([sentence for sentence in df['clean_tweet'][df['label']==0]])  #0 for positive, 1 for negative

wc = WordCloud(background_color='lavender', width=800, height=500, random_state=42, max_font_size=100).generate(all_words)

#graph
plt.figure(figsize=(15,8))
plt.imshow(wc, interpolation='sinc')
plt.axis('off')
plt.show()
st.markdown("<h4 style='text-align: center; color: white;'>Visualizaton of frequent positive words</h4>", unsafe_allow_html=True)
st.pyplot()

#visualization of frequent negative words

all_words = " ".join([sentence for sentence in df['clean_tweet'][df['label']==1]])

wc = WordCloud(width=800, height=500, random_state=42, max_font_size=100).generate(all_words)

#graph
plt.figure(figsize=(15,8))
plt.imshow(wc, interpolation='sinc')
plt.axis('off')
plt.show()
st.markdown("<h4 style='text-align: center; color: white;'>Visualizaton of frequent positive words</h4>", unsafe_allow_html=True)
st.pyplot()

#for extracting the hashtag from tweet
def hashtag_extract(tweets):
    hashtags = []
    for tweet in tweets:
        ht = re.findall(r"#(\w+)", tweet)
        hashtags.append(ht)
    return hashtags

ht_positive = hashtag_extract(df['clean_tweet'][df['label']==0])
print('positive hashtags-', ht_positive[:5])

ht_negative = hashtag_extract(df['clean_tweet'][df['label']==1])
print('negative hashtags-', ht_negative[:3])

#combine everything to a single list/unnest the list
ht_positive= sum(ht_positive, [])
ht_negative= sum(ht_negative, [])
 
ht_positive[:10]

ht_negative[:10]

#to process the positive tweets

freq = nltk.FreqDist(ht_positive)

d = pd.DataFrame({'hashtag': list(freq.keys()),
                 'count': list(freq.values())})
d.head()

#graph of top 10 positive hashtags
d = d.nlargest(columns='count', n=10)
plt.figure(figsize=(15,9))
sns.barplot(data=d, x='hashtag', y='count')
plt.show()
st.markdown("<h4 style='text-align: center; color: white;'>Graph of top 10 positive hashtags</h4>", unsafe_allow_html=True)
st.pyplot()

#to process the negative tweets

freq = nltk.FreqDist(ht_negative)

d = pd.DataFrame({'hashtag': list(freq.keys()),
                 'count': list(freq.values())})
d.head()

#graph of 10 largest negative hashtags

d=d.nlargest(columns='count', n=10)
plt.figure(figsize=(15,9))
sns.barplot(data=d, x='hashtag', y='count')
plt.show()
st.markdown("<h4 style='text-align: center; color: white;'>Graph of top 10 negative hashtags</h4>", unsafe_allow_html=True)
st.pyplot()

#feature extraction of data
from sklearn.feature_extraction.text import CountVectorizer
bow_vectorizer = CountVectorizer(max_df=0.90,min_df=2,max_features = 1000,stop_words='english')
bow = bow_vectorizer.fit_transform(df['clean_tweet'])
#bow[0].toarray()

#splitting the data for training and testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(bow,df['label'], random_state=42 , test_size=0.25)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, accuracy_score

# Model Training
model = LogisticRegression()
model.fit(x_train,y_train)

# Testing
pred = model.predict(x_test)
f1_score(y_test, pred)

accuracy_score(y_test, pred)
st.write("Accuracy Score of the model is :", accuracy_score(y_test, pred))