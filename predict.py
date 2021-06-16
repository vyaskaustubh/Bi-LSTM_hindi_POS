from keras.models import load_model
import pickle
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical

with open('PickledData/data.pkl', 'rb') as f:
	X_train, Y_train, word2int, int2word, tag2int, int2tag = pickle.load(f)

	del X_train
	del Y_train
  
sentence = ['यह', 'एशिया', 'की', 'सबसे', 'बड़ी', 'मस्जिदों', 'में', 'से', 'एक', 'है', '।'] 
new = ""
for x in sentence:
   new = new + x + ' '
print(new) 
sentence = new.split()
print(sentence)
tokenized_sentence = []

for word in sentence:
	tokenized_sentence.append(word2int[word])

tokenized_sentence = np.asarray([tokenized_sentence])
padded_tokenized_sentence = pad_sequences(tokenized_sentence, maxlen=100)

print('The sentence is ', sentence)
print('The tokenized sentence is ',tokenized_sentence)
print('The padded tokenized sentence is ', padded_tokenized_sentence)

model = load_model('Models/model.h5')

prediction = model.predict(padded_tokenized_sentence)
print(prediction.shape)

for i, pred in enumerate(prediction[0]):
	try:
		print(int2tag[np.argmax(pred)])
	except:
		pass
		#print('NA')
