import tensorflow as tf
from tensorflow import keras
import numpy as np
import sys

data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000)
# man nimmt nur worte die unter den top 10 000 sind die vorkommen mit num words macht es einfacher

# print(train_data[0])
# wörter sind als integer getrart --> dictonary von tensorflow wird verwendet
word_index = data.get_word_index()
#print(word_index.items())


word_index = {k: (v + 3) for k, v in word_index.items()}
word_index['<PAD>'] = 0
word_index['<START>'] = 1
word_index['<UNK>'] = 2
word_index['<UNUSED>'] = 3

train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index['<PAD>'], padding='post',
                                                        maxlen=250)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index['<PAD>'], padding='post', maxlen=250)

model = keras.Sequential()
model.add(keras.layers.Embedding(10000, 16))
# versucht wortgruppen zu finden die ähnliche bedeutung haben macht 10 000 wortvektoren mit 16 dimensionen
model.add(keras.layers.GlobalAveragePooling1D())  # macht die vektoren kleiner
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.summary()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

x_val = train_data[:10000]
x_train = train_data[10000:]

y_val = train_labels[:10000]
y_train = train_labels[10000:]

fitModel = model.fit(x_train, y_train, epochs=40, batch_size=512, validation_data=(x_val, y_val), verbose=1)

results = model.evaluate(test_data, test_labels)

print(results)
