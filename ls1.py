import numpy
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/sakura/Загрузки/Most-Recent-Cohorts-Scorecard-Elements.csv")
print(df)

df_norm = (df["NPT43_PRIV"] - df["NPT43_PRIV"].mean())/df["NPT43_PRIV"].std()
plt.plot(df_norm)

corr = df["NPT43_PRIV"].corr(df["NPT44_PRIV"])
print(corr)

plt.show()