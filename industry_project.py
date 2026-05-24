import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

print(df.head())

# Advanced Visuals
sns.pairplot(df)
plt.show()

plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

plt.figure()
sns.boxplot(x='Category', y='Revenue', data=df)
plt.show()

plt.figure()
sns.lineplot(x='Date', y='Revenue', data=df)
plt.xticks(rotation=45)
plt.show()

# ML Model
X = df[['Price','Quantity']]
y = df['Revenue']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test,y_test))

pred = model.predict([[5000,3]])
print("Prediction:", pred)
