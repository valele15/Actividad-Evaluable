import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv('d.csv')
df.head()

plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.xticks(rotation= 45)
plt.show()

corr= df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr,annot= True, cmap= "RdPu")
plt.show()

#Varianzas

varianza1=df["Agricultura.ganaderia"].var()
print(varianza1)

varianza2=df["Industria.electricidad"].var()
print(varianza2)

varianza3=df["Industria.manufacturera"].var()
print(varianza3)

varianza4=df["Construccion"].var()
print(varianza4)