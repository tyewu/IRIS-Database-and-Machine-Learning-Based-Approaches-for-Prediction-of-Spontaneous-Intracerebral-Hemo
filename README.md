# IRIS-Database-and-Machine-Learning-Based-Approaches-for-Prediction-of-Spontaneous-Intracerebral-Hemo
IRIS Database and Machine Learning Based Approaches for Prediction of Spontaneous Intracerebral Hemorrhage
Spontaneous intracerebral hemorrhage (SICH) has been common in China with high morbidity and mortality rates. This study aims to develop a machine learning (ML)-based predictive model for the 90-day evaluation after SICH.
Spontaneous intracerebral hemorrhage (SICH) is common in China with high morbidity and mortality. This study aimed to develop a machine learning (ML)-based predictive model for the 90-day post-SICH evaluation. This project uses IRIS and a trained machine learning model (AUC=0.85) to predict the probability of a patient suffering from the disease based on patient characteristics, and store the data and probability in the IRIS database to achieve interaction with the IRIS database.
# Installation
- Setting connection.config file, change to your own configuration.
- Execute the creatdatatable.py file, create the Dhc.Intrahemor.
- Execute the server.py file, start the service.
- Run test.py file, output prediction result.
- You can modify the data parameter in the file. "GCS" is "Glasgow Coma Scale", "GFR" is "Glomerular filtration rate"
- URL: http://localhost:5001/api
- The result is returned as shown below.
![image](https://user-images.githubusercontent.com/44487844/155253776-a56a6b46-72cd-4d1b-b47f-287adfddd47b.png)

