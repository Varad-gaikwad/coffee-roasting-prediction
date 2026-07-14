# %%
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd.read_csv("coffee_roasting_dataset.csv")
x=df[['Temperature', 'Time']]
y=df[['GoodRoast']]


'''We use the train_test_split function to split the dataset into training and testing sets so that we can evaluate the model's performance on unseen data. 
We specify a test size of 20% and a random state for reproducibility.'''
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Training set shape:", x_train.shape, y_train.shape)
print("Testing set shape:", x_test.shape, y_test.shape)


# %%

#Normalize the input features to improve model performance
normalizer = tf.keras.layers.Normalization()
normalizer.adapt(x_train.values)

#build the model.
'''the difference between relu and sigmoid activation functions is that relu is used for hidden layers and outputs positive values, 
while sigmoid is used for the output layer and outputs values between 0 and 1.'''
model = Sequential([
    normalizer,
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')])


#adam optimiser to get w and b weights as a tensorflow function
#binary_crossentropy loss function to measure the difference between predicted and actual values
#accuracy metric to evaluate the model's performance during training and testing.
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#it trains the model on the training data 
#epochs=100 means the model will iterate over the entire training dataset 100 times during training.
#verbose=1 means that the training progress will be displayed in the console.
model.fit(x_train,y_train, epochs=300, verbose=1)

#to save the model
model.save("coffee_model.keras")


# %%
'''After training the model, we evaluate its performance on the test set using the evaluate method. This method returns the loss and accuracy of the model on the test data. 
We then print these values to assess how well the model generalizes to unseen data.'''
loss, accuracy=model.evaluate(x_test, y_test)
print("Test loss:", loss)
print("Test accuracy:", accuracy*100, "%")

print("Training Finished!")





# %%
