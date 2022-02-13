import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("GDP.csv",encoding="shift-jis")
y=df["国内総生産(支出側)"].str.replace(",","").astype("float")
plt.plot(y)
