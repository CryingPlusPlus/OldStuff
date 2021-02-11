import tensorflow as tf
from tensorflow import keras  # keras ist eine API von tensorflow; weniger code zum schreiben
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist  # data

# splitting in testing und training data -> 90-80% werden trainiert mit dem rest wird getestet um zu schauen ob es funktioniert hat

(train_images, train_labels), (test_images, test_labels) = data.load_data()  # data aus der keras api

class_names = ['TShirt/Top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([ # eine sequenz aus layers
    keras.layers.Flatten(input_shape=(28, 28)),  # Flatten 28x28 array zu 784x1 array
    keras.layers.Dense(128, activation='relu'),
    # regtify linear unit very fat activationfunction Dense = Fully conected
    keras.layers.Dense(10, activation='softmax')  # nimmt die größte wahrscheinlichkeit... gibt prozentwerte zuurück
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)
# epochs gibt traiing data in unterschiedlicher reihenfolge um die genauigkeit zu erhöhen

prediction = model.predict([np.array(test_images)])

for i in range(5):
    print(class_names[test_labels[i]], ' --- ', class_names[np.argmax(prediction[i])])
