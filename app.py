import numpy as np
import pickle
import streamlit as st


# Load the trained model
loaded_model = pickle.load(open('trained_model.sav','rb'))

# Function for making diabetes prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction[0] == 0):
        return "**You are not likely to be diabetic.**"
    else:
        return """
        **You are likely to be diabetic.** Please consult with a healthcare professional for further guidance. Here are some general tips for managing diabetes:

        1. Follow a healthy, balanced diet with plenty of fruits and vegetables.
        2. Try to maintain a regular exercise routine.
        3. Regularly monitor your blood glucose levels.
        4. If you smoke, try to quit, and limit your alcohol consumption.
        5. Regularly check your feet for cuts or sores, as diabetes can lead to foot complications.

        Remember, these tips are general advice and may not be suitable for everyone. Always consult with a healthcare professional for personalized advice.
        """

def main():
    # UI title
    st.title('Diabetes Prediction App')

    # UI description
    st.write("""
    Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces. 
    This application uses a machine learning model to predict whether a person is likely to have diabetes based on certain health metrics. 
    """)
    st.markdown('**Note : This app is just a project and should not be used as health advice.**')
    st.image('diabetes.jpg')
    
    # User input
    age = st.slider('Age', min_value=0, max_value=90, value=30)
    bmi = st.number_input('BMI', min_value=0.0, max_value=75.0, value=25.0)
    glucose = st.number_input('Glucose Level', min_value=0, max_value=200 ,value=100)
    blood_pressure = st.number_input('Blood Pressure (mm Hg)', min_value=0,  value=70)
    insulin = st.number_input('Insulin (mu U/ml)', min_value=0, value=30)
    pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0)
    familydiabetic = st.selectbox('Family History of Diabetes', ['No', 'Yes'])

    
    # Diabetes Test Result button
    if st.button('Am I Diabetic?'):
        familydiabetic = 1 if familydiabetic == 'Yes' else 0
        diagnosis = diabetes_prediction([age,bmi,glucose,blood_pressure,insulin,pregnancies,familydiabetic])
        if "not likely" in diagnosis:
            st.success(diagnosis)
        else:
            st.error(diagnosis)
    
    # Links to GitHub and LinkedIn
    st.markdown("""
    **Author:** [Linkedin](https://www.linkedin.com/in/oolwinds111/)
    
    **Source Code:** [GitHub](https://github.com/oolwinds/diabetesprediction)
    """)

if __name__ == '__main__':
    main()
