import numpy as np
import pickle

loaded_model = pickle.load(open('trained_model.sav','rb'))

input_data = (5,5,5,5,5,5)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)

if (prediction[0] ==0):
    print("This person is not diabetic.")
else:
    print("This person is diabetic.")