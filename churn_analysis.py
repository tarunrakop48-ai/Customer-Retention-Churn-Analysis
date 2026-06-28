import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries Imported Successfully")

import pandas as pd
df = pd.read_csv("Dataset/Customer churn.csv")
print (df.head())
print("\nDataset Shape:")
print(df.shape)
print("\nColumns:")
print(df.columns)

df = pd.read_csv("Dataset/Customer churn.csv")
print("missing values")
print(df.isnull().sum())

print(df.dtypes)

print("Duplicate Rows:",df.duplicated().sum())

import pandas as pd
print(df["Churn"].value_counts())

print(df["Churn"].value_counts(normalize=True)*100)

print(df.describe())

for col in df.columns:
 print("\n",col)
 print(df[col].unique())

 print((df["TotalCharges"]==" ").sum())

 print(df["TotalCharges"].dtype)

print(df.shape)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df["TotalCharges"].isnull().sum())

df["TotalCharges"]=df["TotalCharges"].fillna(df["TotalCharges"].median())

#Churn Distribution
import matplotlib.pyplot as plt
df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Customers")
plt.show()

#Churn Percentage
df["Churn"].value_counts().plot(kind="pie", autopct="%1.1f%%")

plt.ylabel("")
plt.title("Churn Percentage")
plt.show()


import seaborn as sns
sns.countplot(x="Gender",hue="Churn",data=df)

#churn by gender
plt.title("Churn by Gender")
plt.show()

#churn by Contract
sns.countplot(x="Contract",hue="Churn",data=df)
plt.title("Churn by Contract Type")
plt.xticks(rotation=15)
plt.show()

#churn by Payment Method
plt.figure(figsize=(10,5))
sns.countplot(y="PaymentMethod",hue="Churn",data=df)

plt.title("Churn by Payment Method")
plt.show()

sns.countplot(x="InternetService",hue="Churn",data=df)
plt.title("Churn by Internet Services")
plt.show()

#churn by Senior Citizen
sns.countplot(x="SeniorCitizen",hue="Churn",data=df)
plt.title("Churn by SeniorCitizen")
plt.show()

#churn by MonthlyCharges
sns.boxplot(x="Churn",y="MonthlyCharges",data=df)
plt.title("Churn by MonthlyCharges")
plt.show()

#churn vs Tenure
sns.boxplot(x="Churn",y="Tenure",data=df)
plt.title("Churn Vs Tenure")
plt.show()

#Correlation Heatmap
numeric_cols = df.select_dtypes(include=["int64","float64"])

sns.heatmap(numeric_cols.corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

