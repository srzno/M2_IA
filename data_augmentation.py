# -*- coding: utf-8 -*-
"""Data_augmentation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BEUKVmgLEprTTHoZrrViYraWFl8jajrt
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/drive/MyDrive/hotdog-nothotdog"
!ls

"""### Data Augmentation


"""

import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

base_dir = '/content/drive/MyDrive/hotdog-nothotdog'
test_dir = os.path.join(base_dir, 'test')
train_dir = os.path.join(base_dir,'train')


train_datagen = ImageDataGenerator(
							rescale = 1./255,
							rotation_range = 150,
							width_shift_range = 0.1,
							height_shift_range = 0.1,
							shear_range = 0.2,
							horizontal_flip = True)

"""### Utilice imageGenerator para ampliar y enriquecer el conjunto de datos de entrenamiento ("train") de su modelo de aprendizaje automático mediante la modificación creativa de las imágenes existentes. De esta manera, generará un conjunto de datos más robusto que permitirá un entrenamiento más efectivo de su modelo, lo que se traduce en un mejor rendimiento y resultados más precisos."""

train_generator = train_datagen.flow_from_directory(
							train_dir,
							target_size = (150, 150),
							batch_size = 1,
							class_mode ='binary',
							)


plt.figure()
#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(1, 5, figsize=(30, 8))

for i in range(5) :
  axarr[i].imshow(train_generator[0][0][0])

train_generator = train_datagen.flow_from_directory(
							train_dir,
							target_size = (150, 150),
							batch_size = 8,
							class_mode ='binary',
							)

images , labels = train_generator[0]

print(images.shape)
print(labels)

plt.figure()
#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(1, images.shape[0], figsize=(30, 4))

for i in range(images.shape[0]) :
  axarr[i].imshow(images[i])

"""
### Podemos guardar las imágenes generadas para verlas más tarde y entender mejor cómo entrenó el modelo."""

path = "/content/drive/MyDrive/hotdog-nothotdog"

train_generator = train_datagen.flow_from_directory(
							train_dir,
							target_size = (150, 150),
							batch_size = 8,
							class_mode ='binary',
							save_to_dir= path + '/augmented',
              save_prefix='aug',
              save_format='png'
							)

from tensorflow.keras import optimizers
from tensorflow.keras import models
from tensorflow.keras import layers

model = models.Sequential()
model.add(layers.Conv2D(10, (3, 3), activation="relu", input_shape = (150,150,3)))
model.add(layers.Flatten())
model.add(layers.Dense(256,activation='relu'))
model.add(layers.Dense(1,activation='sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy',
						optimizer=optimizers.RMSprop(learning_rate=2e-5),
						metrics=['acc'])

history = model.fit(
						train_generator,
						epochs = 2)

acc = history.history['acc']
loss = history.history['loss']

epochs = range(1, len(acc)+1)

plt.plot(epochs,acc,'bo',label='train accuracy')
plt.title('train acc')
plt.legend()

plt.figure()

plt.plot(epochs,loss, 'bo', label ='training loss')
plt.title('train loss')
plt.legend()

plt.show()

test_datagen = ImageDataGenerator(1./255)
test_generator = test_datagen.flow_from_directory(
					test_dir,
					target_size = (150, 150),
					batch_size = 1,
					class_mode= 'binary')

test_loss, test_acc = model.evaluate(test_generator, steps = 25)
print('\ntest acc :\n', test_acc)