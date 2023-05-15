# Diabetes Assessment Tool 

As a data science student, I embarked on a supervised learning classification project utilizing the Pima Diabetes Dataset. The objective of this project was to develop a machine learning model that could accurately predict if an individual has diabetes based on various health indicators. Given this context, the purpose of this project extends far beyond its technical aspects. The primary aim is to provide an accessible tool that empowers individuals to understand their risk of diabetes better. By identifying risk factors early, it is possible to take preventive measures before the onset of the disease. This not only has the potential to improve physical health outcomes, but it can also alleviate the emotional burden associated with managing a chronic condition like diabetes.

## The diabetes assessment tool is live! You can access it by clicking [**Here!**](https://diabeticsprediction.onrender.com/)

Data Source: https://www.openml.org/search?type=data&sort=runs&id=37


### Workflow
The entire project followed a structured workflow that started with data pre-processing, followed by model selection, training and evaluation, and finally, the deployment of the predictive model in a web application.

![Capture](https://github.com/oolwinds/diabetesprediction/assets/130780065/afb4cb0c-01f0-4797-8249-657c6cede834)


**Data Pre-processing**: Importing the dataset, dealing with missing or unrealistic values, and feature engineering.
**Model Selection**: Choosing suitable models based on the nature of the dataset and the problem statement.
**Model Training and Evaluation**: Training selected models on the processed dataset, evaluating them using various metrics, and selecting the best performing model.
**Web Application Development** and Deployment: Building a user-friendly web application with Streamlit and deploying it on Render for users to get real-time diabetes predictions.

### Data Analysis & Pre-processing
The first step involved pre-processing and analyzing the dataset, which consisted of features such as Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, and Age. On close inspection, I noticed that some features (Glucose, BloodPressure, SkinThickness, Insulin, BMI) had zero values. Given that these features couldn't realistically be zero, I replaced such instances with the mean value of the respective feature. I also detected and replaced extreme outliers with the mean to ensure more robust predictions.

To make the dataset more user-friendly, I engineered a new feature 'familydiabetic' from the 'DiabetesPedigreeFunction'. This feature was designed to represent whether a family member of the individual is diabetic or not. After this, I removed the 'SkinThickness' and 'DiabetesPedigreeFunction' features from the dataset.

### Train-Test-Split
Next, I scaled the data to ensure all values fell within the range of [0,1] and split the dataset into a 70-30 train-test split. To address multicollinearity, I employed Principal Component Analysis (PCA) to reduce the dimensionality of the dataset while retaining 95% of the variance.

### Models and Metrics Selection

I chose five models for this classification task - Random Forest, Logistic Regression, Support Vector Machine, K-Nearest Neighbour, and Naïve Bayes. Each of these models was selected due to their unique strengths:

**Random Forest** is an ensemble learning model that is effective at handling non-linear relationships and complex interactions between features.

**Logistic Regression** is a straightforward and robust model for binary classification tasks. It provides a probabilistic interpretation of class membership, which can be valuable in a healthcare context.

**Support Vector Machine** is a maximum-margin classifier capable of handling both linear and non-linear problems. It effectively mitigates overfitting through regularization, making it suitable for small datasets.

**K-Nearest Neighbour** effectively handles irregular decision boundaries and adapts well to the structure of the data, especially when the number of features is small.

**Naïve Bayes** assumes conditional independence between features, simplifying the computation of joint probabilities. This model typically performs well on small datasets.

To evaluate the performance of these models, I used a variety of metrics: accuracy, precision, recall, F1-score, and Area under the ROC curve. Each metric provides unique insights, making it possible to identify the best model based not only on accuracy but also on its ability to adapt well to unseen data and its validity to the dataset’s distinct challenges.

### Model Evaluation & Main Findings

Logistic Regression emerged as the best performing model, achieving the highest test accuracy (77.92%), precision score (69.12%), F1-score (0.653), and AUC-ROC score (0.84). Other models, despite their unique strengths, showed signs of overfitting or had lower precision and F1-scores, making them less suitable for this dataset.

![Capture](https://github.com/oolwinds/diabetesprediction/assets/130780065/6d60a5e3-cdd8-412f-8f72-8db808048e4c)

The 'familydiabetic' feature held the highest importance in predicting diabetes, followed by 'Pregnancies' and 'BMI'. These findings align with medical understanding that diabetes risk is influenced by heredity and high BMI.
![download](https://github.com/oolwinds/diabetesprediction/assets/130780065/0e1ce5c7-3153-44ff-84ec-76b19f579459)

### Web Application
As a final step, I developed a web application using Streamlit and deployed it onto Render. This application allows users to input their own health indicators and receive a prediction of their diabetes risk based on the trained logistic regression model.

The web application is user-friendly, with clear instructions for users to input their personal health data, such as the number of pregnancies, glucose level, blood pressure, insulin level, BMI, and age. The interface also includes an option to indicate whether there are any family members with diabetes, which is a critical feature according to the model.

Once the user inputs their data and clicks the 'Predict' button, the logistic regression model processes the data and provides a probability of having diabetes. The results are displayed in an easily understandable format, empowering users to take charge of their health.

### Conclusion
This project allowed me to apply various data science concepts in a real-world context. From the nuanced process of pre-processing data to the selection and evaluation of machine learning models, each step was a learning opportunity. The final web application serves as a practical tool for individuals to assess their diabetes risk, demonstrating the potential of machine learning in healthcare applications. It has been a humbling and enriching experience to apply data science techniques to a problem that could potentially make a difference in people's lives. I believe that data science has a pivotal role to play in healthcare, and I look forward to contributing further to this field in my future projects.

Through this project, I learned that although several models might seem suitable for a given dataset, the choice of model can significantly impact the accuracy and reliability of predictions. Therefore, it is crucial to thoroughly evaluate each model using appropriate metrics. I also learned the importance of feature engineering in improving model performance and making the dataset more user-friendly.

As a future direction, I plan to explore more complex models and feature engineering techniques to further improve the model's predictive performance. I also hope to integrate more health indicators into the web application to provide a more comprehensive health assessment for users.

![Capture](https://github.com/oolwinds/diabetesprediction/assets/130780065/4d83beab-d3bc-4cb9-91f7-b52cf6e4b350)
