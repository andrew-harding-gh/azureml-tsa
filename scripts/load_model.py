from keras.models import load_model 
import time
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from gensim.models import Word2Vec
import pickle
  
w2v_model = Word2Vec.load('C:\\Users\\Peter Samoaa\\Downloads\\results\\model.w2v')
model = load_model('C:\\Users\\Peter Samoaa\\Downloads\\results\\model.h5') 

with open('C:\\Users\\Peter Samoaa\\Downloads\\results\\tokenizer.pkl', 'rb') as handle:
     tokenizer = pickle.load(handle) 
with open('C:\\Users\\Peter Samoaa\\Downloads\\results\\encoder.pkl', 'rb') as handle:
     encoder = pickle.load(handle)