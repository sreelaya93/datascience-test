# from tensorflow.keras.datasets import mnist
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
# from tensorflow.keras.utils import to_categorical
# #from tensorflow.python.keras.saving.saved_model.load import metrics
#
# # load mnist dataset
# (xtrain,ytrain),(xtest,ytest)=mnist.load_data()
#
#
# # reshape data (CNN needs 4D input)
# xtrain=xtrain.reshape((60000,28,28,1))
# xtest=xtest.reshape((10000,28,28,1))
#
# #normalize pixel values (0-255 -> 0-1)
# xtrain=xtrain/255
# xtest=xtest/255
#
# # one -hot encodes labels(0-9 -> 10 categories)
# ytrain=to_categorical(ytrain)
# ytest=to_categorical(ytest)
#
# # build CNN model
# model=Sequential()
#
# # convolution layer
# model.add(Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)))
#
# #pooling layer
# model.add(MaxPooling2D((2,2,)))
#
# # flatten layer
# model.add(Flatten())
#
# # hidden dence layer
# model.add(Dense(128,activation='relu'))
#
# # output layer (10 digits)
# model.add(Dense(10,activation='softmax'))
#
# # compile model
# model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
#
# # train model
# model.fit(xtrain,ytrain,epochs=5,batch_size=32)
#
# # test accuracy
# test_loss,test_acc=model.evaluate(xtest,ytest)
# print('test accuracy : ',test_acc)

#-----------------------------------------------------------------------------------------------------


# import numpy as np
# import pandas as pd
# from keras.saving.saved_model.load import metrics
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
# import tensorflow as tf
# from tensorboard.plugins.scalar.summary import scalar
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.callbacks import EarlyStopping
#
# # create simple synthetic dataset(student -> pass/fail)
# # we will simulate 1000 students with study hours/attendance/sleep hours/assignments done
#
# from sklearn.datasets import make_classification
# from tensorflow.python.keras.utils.version_utils import callbacks
#
# x,y=make_classification(n_samples=1000,n_features=4,n_informative=3,n_redundant=0,n_classes=2,random_state=42)
#
# #conver to dataframe to make it readable
#
# df=pd.DataFrame(x,columns=['study_hours','attendance','sleep_hours','assignments_done'])
# df['pass']=y
#
# # quick look (optional)
#
# print(df.head())
#
# # split features and labels
#
# x=df[['study_hours','attendance','sleep_hours','assignments_done']].values
# y=df['pass'].values
#
# # train test split
#
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)
#
# # feature scaling(very importance for neural net)
#
# scaler=StandardScaler()
# xtrain=scaler.fit_transform(xtrain)
# xtest=scaler.transform(xtest)
#
# # build an ANN model(sequential API)
#
# model=Sequential([Dense(16,activation='relu',input_shape=(xtrain.shape[1],)), #first hidden layer
#                   Dense(8,activation='relu'), #second layer
#                   Dense(1,activation='sigmoid') ])# output layer for binary classification
#
# # compile the model(choose optimizer,loss,metrics)
#
# model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
#
# #early stopping callback to prevent outfitting
#
# early_stop=EarlyStopping(monitor='val_loss',patience=8,restore_best_weights=True)
#
# #train the model
#
# history=model.fit(xtrain,ytrain,validation_split=0.2,epochs=100,batch_size=32,callbacks=[early_stop],verbose=1)
#
# #evaluate on test set
#
# loss,acc=model.evaluate(xtest,ytest,verbose=0)
# print(f'Test accuracy :{acc:.4}')
#
# # prediction and metrics
#
# y_pred_prob=model.predict(xtest).flatten()
# y_pred=((y_pred_prob>=0.5).astype(int))
# print('confusion metrics:',(ytest,y_pred))
# print('classification report :',classification_report(ytest,y_pred))
#
# # save the model and scaler for later use
#
# model.save('student_pass_model.h5')
# import joblib
# joblib.dump(scaler,'scaler.save')
# print('model and scaler saved')

#-------------------------------------------------------------------------------------------------------------

# # simple perceptron using numpy
#
# import numpy as np
# from scipy.cluster.hierarchy import weighted
#
#
# def step(x):
#     return 1 if x>=0 else 0
# weights=np.array([0.5,0.5])
# bias=-0.7
# input=np.array([1,0])
# output=step(np.dot(weights,input)+bias)
# print(output) # output:0
#
# # sigmoid activation function
#
# import numpy as np
# def sigmoid(x):
#     return 1/(1+np.exp(-x))
# print('sigmoid',sigmoid(0)) #output:0.5
#
# #simple feedforward with one hidden layer using keras
#
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# model=Sequential([Dense(4,input_dim=2,activation='relu'),
#                   Dense(1,activation='sigmoid')])
# model.summary()
#
# # binary classification on dummy data
#
# import numpy as np
# x=np.array([[0,0],[0,1],[1,0],[1,1]])
# y=np.array([0,1,1,0]) #XOR eg
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# model=Sequential([Dense(4,input_dim=2,activation='relu'),
#                   Dense(1,activation='sigmoid')])
# model.compile(optimizer='adam',loss='binary_crossentropy',metrics='accuracy')
# model.fit(x,y,epochs=100)
#
# # MNIST digit dataset load medium
# from tensorflow.keras.datasets import mnist
# (xtrain,ytrain),(xtest,ytest)=mnist.load_data()
# print(xtrain.shape,ytrain.shape) # output:(60000,28,28)(60000)
#
# # flattening input for neural network
#
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.layers import Flatten
#
# model=Sequential([Flatten(input_shape=(28,28)),
#                   Dense(128,activation='relu'),
#                   Dense(10,activation='softmax')])
# model.summary()
#
# # one hot encoding labels
# from tensorflow.keras.utils import to_categorical
# y=[0,1,2,1]
# y_encoded=to_categorical(y,num_classes=3)
# print(y_encoded)
#
# #simple relu demonstration
#
# import numpy as np
# def relu(x):
#     return np.maximum(0,x)
# print('relu :',relu([-1,0,5])) # output=0,0,5
#
# #single neuron forward pass
#
# import numpy as np
# x=np.array([1,2])
# w=np.array([0.5,-0.5])
# b=0.1
# output=np.dot(x,w)+b
# print('output :',output)  #output:-0.4
#
# # mean squared error calculation
#
# import numpy as np
# y_true=np.array([1,0])
# y_pred=np.array([0.8,0.2])
# mse=np.mean((y_true-y_pred)**2)
# print('mse :',mse) # output:0.04

#----------------------------------------------------------------------------------------------------------


