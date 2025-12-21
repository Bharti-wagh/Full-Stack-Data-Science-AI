

import pickle

#Save the trained model to disk
filename = 'linear_regression_model.pkl'
#Open a file in write-binary mode and dump the model
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as linear_regression_model.pkl")

import os 
os.getcwd()