# Prepared by Muhammad Qasim Riaz (Lecturer - GIK Institute)
# =====================================================
# Complete Project - Exploratory Data Analysis (EDA)
# Using Pandas + Matplotlib
# Dataset: Iris
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iris = pd.read_csv("iris.csv")

print(iris.head())
print(iris.tail())
print(iris.shape)
print(iris.columns)
iris.info()
print(iris.describe())

print(iris.isnull().sum())
iris = iris.drop_duplicates()

print(iris.sort_values(by=iris.columns[0]).head())
print(iris.corr(numeric_only=True))

iris.plot(x=iris.columns[0], y=iris.columns[1], title="Line Plot")
plt.show()

iris.plot(kind="scatter", x=iris.columns[0], y=iris.columns[1])
plt.show()

iris[iris.columns[0]].plot(kind="hist")
plt.show()

iris.head().plot(kind="bar", x=iris.columns[0])
plt.show()

if "species" in iris.columns:
    iris["species"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.ylabel("")
    plt.show()

iris.boxplot()
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(iris.iloc[:,0],iris.iloc[:,1],iris.iloc[:,2])
plt.show()

X=iris.iloc[:,0:4]
y=iris.iloc[:,4]
print(X.head())
print(y.head())

iris.to_csv("iris_cleaned.csv",index=False)
print("Done")
