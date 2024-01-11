import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#im
time = pd.read_csv('dataset/Time.csv')
timeage = pd.read_csv('dataset/TimeAge.csv')
timegender = pd.read_csv('dataset/TimeGender.csv')
timeprovince = pd.read_csv('dataset/TimeProvince.csv')
patient = pd.read_csv('dataset/PatientInfo.csv')
searchtrend = pd.read_csv('dataset/PSearchTrend.csv')
region = pd.read_csv('dataset/PSearchTrend.csv')



# looking at patient info -> dataframe
patient_df = pd.DataFrame(patient)


