# Plant-Seedlings-Classification-using-Deep-Learning
Final Project of Computer Vision with Deep Learning PESU-I/O

We have taken a Plant Seedlings Classification dataset that classifies 12 different varieties of plant seedlings. They are as follows:
* Black-grass
* Charlock
* Cleavers
* Common Chickweed
* Common Wheat
* Fat Hen
* Loose Silky-bent
* Maize
* Scentless Mayweed
* Shepherds Purse
* Small-flowered Cranesbill
* Sugar Beet

Our model uses a InceptionResNetV2 pretrained model in replacement for CNN. We have then added a GlobalAveragePooling2D layer to reduce the dimensionality of the images, following which we have added 5 Dense layers, 4 of which have an activation of 'relu' and the other having 'softmax' activation'. The model is then compiled with optimizer to be 'adam', loss function to be 'categorical_crossentropy'.

Our method of approach to increase accuracy was by using Data Augmentation and by increasing the number of layers in the neural network.

Current Training Accuracy | Current Validation Accuracy
------------------------- | ---------------------------
% | %

To run the code and classify your image, copy the code from GUI.py and download Saved_Model folder from the Google Drive link at the end of this README.md file. Note that the python file and the Saved_Model folder must belong to the same directory.

Link to the Saved_Model - https://drive.google.com/drive/folders/1ddCXen9sAn-xsIUTgo0TjdOnzrYJEt1m?usp=sharing
