import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

X1 = pd.read_csv('../winequality-red.csv')

print("La discretización le permite analizar estas variables numéricas en términos de categorías, lo que puede facilitar la interpretación de cómo influyen en la calidad del vino. Sin embargo, es importante recordar que la discretización puede ser una simplificación y puede perder cierta información contenida en los valores numéricos originales.")

discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')

X2 = discretizer.fit_transform(X1)

print(X2)



