import tensorflow as tf
import numpy as np
dataGen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale = 1./255,
    rotation_range=5,
    horizontal_flip=True,
    vertical_flip=True,
)
train_dataset_aug = dataGen.flow_from_directory("PlantSeedlings/plant-seedlings-final/train",target_size = (224,224),batch_size = 32,shuffle=True,seed = 865)
test_dataset_aug = dataGen.flow_from_directory("PlantSeedlings/plant-seedlings-final/val",target_size = (224,224),batch_size = 32,shuffle=True,seed = 865)
pretrained_model = tf.keras.applications.InceptionResNetV2(input_shape=(224,224,3),include_top=False,weights='imagenet')
pretrained_model.trainable = False
model = tf.keras.models.Sequential()
model.add(pretrained_model)
model.add(tf.keras.layers.GlobalAveragePooling2D())
model.add(tf.keras.layers.Dense(650, activation='relu'))
model.add(tf.keras.layers.Dense(350, activation='relu'))
model.add(tf.keras.layers.Dense(150, activation='relu'))
model.add(tf.keras.layers.Dense(85, activation='relu'))
model.add(tf.keras.layers.Dense(12, activation='softmax'))
model.compile(optimizer = 'adam',loss='categorical_crossentropy',metrics = ['accuracy'])
history = model.fit(train_dataset_aug, validation_data=test_dataset_aug, epochs = 15)
model.save('Saved_Model_Backup')
