import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math

dataset = pd.read_csv('bank.csv')

X = dataset.iloc[:,0:16].values
y = dataset.iloc[:,-1].values



from sklearn.preprocessing import LabelEncoder
lab= LabelEncoder()

#Encoding workclass

X[:,1] = lab.fit_transform(X[:,1])
#Encoding education
X[:,2] = lab.fit_transform(X[:,2])
#Encoding marital-status
X[:,3] = lab.fit_transform(X[:,3])
#Encoding occupation
X[:,4] = lab.fit_transform(X[:,4])
#Encoding relationship
X[:,6] = lab.fit_transform(X[:,6])
#Emcoding race
X[:,7] = lab.fit_transform(X[:,7])
#Encoding sex
X[:,8] = lab.fit_transform(X[:,8])
#Encoding native-country
X[:,10] = lab.fit_transform(X[:,10])
#Encoding sex
X[:,15] = lab.fit_transform(X[:,15])
#Encoding native-country 

from sklearn.preprocessing import OneHotEncoder
one = OneHotEncoder(categorical_features = [1,2,3,4,6,7,8,10,15])
X = one.fit_transform(X)
X= X.toarray()

y = lab.fit_transform(y)
                  
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

log_reg.score(X_train, y_train)
log_reg.score(X_test, y_test)
log_reg.score(X, y)

y_pred = log_reg.predict(X_test)

#Data Exploration

sns.countplot(x = y, data = dataset, palette = 'hls')
plt.show()
plt.savefig('count_plot')


dataset['deposit'].value_counts() 

c1 = len(dataset[dataset['deposit']=='yes'])
c2 = len(dataset[dataset['deposit']=='no'])

print("Percentage of people saying yes",(c1/(c1+c2))*100)
print("Percentage of people saying no",(c2/(c1+c2))*100)

dataset = dataset.groupby('job').mean()
dataset = dataset.groupby('deposit').mean()
dataset = dataset.groupby('marital').mean()
dataset = dataset.groupby('education').mean()

#VISUALISATION

pd.crosstab(dataset.job, dataset.deposit, margins = 'True')


''' 
‘bar’ or ‘barh’ for bar plots
‘hist’ for histogram
‘box’ for boxplot
‘kde’ or ‘density’ for density plots
‘area’ for area plots
‘scatter’ for scatter plots
‘hexbin’ for hexagonal bin plots
‘pie’ for pie plots
'''

pd.crosstab(dataset.job, dataset.deposit, margins = 'True').plot(kind = 'bar')
plt.title('Purchase Frequency for Job Title')
plt.xlabel('Job')
plt.ylabel('Frequency of purchase')
plt.savefig('purchase_fre_job')
pd.crosstab(dataset.job, dataset.deposit, margins = 'True').plot(kind = 'hist')
pd.crosstab(dataset.job, dataset.deposit, margins = 'True').plot(kind = 'box')
pd.crosstab(dataset.job, dataset.deposit, margins = 'True').plot(kind = 'kde')
pd.crosstab(dataset.job, dataset.deposit, margins = 'True').plot(kind = 'area')

#stacked bar graph
pd.crosstab(dataset.marital, dataset.deposit, margins = 'True').plot(kind = 'bar', stacked = 'True')
plt.title('Marital status VS purchase')
plt.xlabel('Marital')
plt.ylabel('Purchase frequency')

pd.crosstab(dataset.education, dataset.deposit, margins = 'True').plot(kind = 'bar', stacked = 'True')
plt.title('Education status VS purchase')
plt.xlabel('Education')
plt.ylabel('Purchase frequency')

pd.crosstab(dataset.month, dataset.deposit, margins = 'True').plot(kind = 'bar')
plt.title(' Purchase frequency for month')
plt.xlabel('Month')
plt.ylabel('Frequency of purchase')

#Histogram
plt.hist(dataset.age)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram for age')

dataset['marital'].unique()

#Pie chart
                   
labels = 'single', 'married', 'divorced' 
colors = ['red', 'yellow', 'blue']  
sizes = [200,567,233]
explode = (0.5, 0, 0)     # only "explode" the 1st slice (i.e. 'single')
plt.pie(sizes, labels = labels, colors = colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
 #histogram
N = 11162           
K = int(1 + 3.322*math.log(N)) #import math
print(plt.style.available)

plt.hist(dataset.age, bins = K, color='pink')
plt.style.use('ggplot')
plt.xlabel('Age')
plt.show()
                   
plt.hist(dataset.age, bins = K, color='pink')
plt.style.use('fivethirtyeight')
plt.show()
                                 
plt.hist(dataset.age, bins = K, color='pink')
plt.style.use('seaborn-pastel')
plt.show()
                                  
                   
plt.hist(dataset.age, bins = K, color='pink')
plt.style.use('Solarize_Light2')
plt.show()
                                  
plt.hist(dataset.duration, bins = K, color='red')
plt.xlabel('Duration')
plt.show()  

# Stratified sampling(to avoid overfitting)

dataset.columns            *

 # not working 
 '''from sklearn.model_selection import StratifiedShuffleSplit
X_train, X_test, y_train, y_test = StratifiedShuffleSplit(X, y, n_splits = 5, test_size = 0.2, random_state = 0)'''


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, test_size =0.2)

X_train.shape                 
X_test.shape
y_train.shape
y_test.shape

dataset.info()              *

#correlation matrix
""" Here we need to change 'y'(deposit) in dataset in 0 and 1, and consider the whole dataset"""
from sklearn.preprocessing import LabelEncoder
lab2= LabelEncoder()
dataset.deposit = lab2.fit_transform(dataset.deposit)

numeric_dataset = dataset.select_dtypes(exclude = "object")

plt.figure(figsize = (40,40))
sns.heatmap(numeric_dataset.corr())
#sns.palplot(sns.light_palette("green")) 
plt.title("Correlation Matrix", fontsize = 16)
plt.show()

plt.figure(figsize = (40,40))
corr = sns.heatmap(numeric_dataset.corr())
corr.style.background_gradient(cmap = "coolwarm")


