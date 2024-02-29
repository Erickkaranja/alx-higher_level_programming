#!/usr/bin/env python3
# coding: utf-8

# In[1]:


from PIL import Image
import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, Dense, Activation, Dropout, Flatten
from tensorflow.keras.layers import experimental
from keras.callbacks import ModelCheckpoint, EarlyStopping


# In[ ]:


#Import all images to X list, with corresponding label of 0 or 1
X = []
y = []

classes = [r"Healthy", r"Disease"]

for i in range(2):
    for filename in glob.glob(r"/kaggle/input/potato-leaf-disease-detection/Potato Leaf Disease/" + classes[i] + r"/*.JPG"):
        image = Image.open(filename).resize((256,256))
        matrix_temp = np.asarray(image)
        X.append(matrix_temp)
        y.append(i)
    for filename in glob.glob(r"/kaggle/input/potato-leaf-disease-detection/Potato Leaf Disease/" + classes[i] + r"/*.jpg"):
        image = Image.open(filename).resize((256,256))
        matrix_temp = np.asarray(image)
        X.append(matrix_temp)
        y.append(i)
    
    print("Class Done")


print("Data imported")


# In[ ]:


#Split data into training and testing set
import gc

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, shuffle = True)

del X
del y

gc.collect()

print("Data Split")

#Convert all to numpy array, convert Y set from 0/1 label to binary vectors

X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)

y_test_raw = y_test

y_train = tf.keras.utils.to_categorical(y_train,5)
y_test = tf.keras.utils.to_categorical(y_test,5)

print("Data converted")


# In[ ]:


#Data augmentation layers
resize_and_rescale = tf.keras.Sequential([
  experimental.preprocessing.Resizing(256, 256),
  experimental.preprocessing.Rescaling(1./255),
])

data_augmentation = Sequential([
  experimental.preprocessing.RandomFlip("horizontal_and_vertical",input_shape = (32,256,256,3)),
  experimental.preprocessing.RandomRotation(0.1),
  experimental.preprocessing.RandomZoom(0.1),
  experimental.preprocessing.RandomTranslation(height_factor = 0.1, width_factor = 0.1)
])


# In[ ]:


#Initialize model architecture 
input_shape = (32, 256, 256, 3)

model = Sequential([
    resize_and_rescale,
    data_augmentation,
    Conv2D(32, kernel_size = (3,3), activation='relu', input_shape=input_shape),
    MaxPooling2D((2, 2)),
    Conv2D(64,  kernel_size = (3,3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64,  kernel_size = (3,3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(5, activation='softmax'),
])

#Build model
model.build(input_shape = input_shape)
print("Model Built")


# In[ ]:


model.summary()


# In[ ]:


#Compile Model
model.compile(
    optimizer='adam',
    loss="categorical_crossentropy",
    metrics=['accuracy']
)
print("Model Compiled")


# In[ ]:


#Train
early = EarlyStopping(monitor = "val_loss", patience = 5,restore_best_weights = True)
history = model.fit(X_train, y_train, batch_size=32, validation_split = 0.1, verbose=1, epochs=50, callbacks = [early])


# In[ ]:


#Evaluation. Bring the y_pred back to label of 0 to 1
y_pred = model.predict(X_test)
y_pred_raw = y_pred
y_pred = np.argmax(y_pred, axis = 1)

accuracy = accuracy_score(y_test_raw, y_pred)


# In[ ]:


print(accuracy)


# In[ ]:


model.save("/kaggle/working/")

