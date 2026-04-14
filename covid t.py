import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

df=pd.read_csv("project datsets.csv")
print(df.head())
print (df.isnull().sum())
df.fillna(0,inplace=True)
print(df.shape)

plt.figure()
plt.scatter(df["Recovered"],df["Deaths"])
plt.title(" total covid 19 case in World")
plt.xlabel("Recovered")
plt.ylabel("Deaths")
plt.show()

X = df[['Confirmed', 'Recovered', 'Active']]
y = df['Deaths']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
print("Linear Regression MAE:", mean_absolute_error(y_test, y_pred_lr))
print("Linear Regression R2:",r2_score(y_test, y_pred_lr))


from sklearn.tree import DecisionTreeRegressor


dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)

y_pred_dt = dt.predict(X_test)

print("Decision Tree MAE:", mean_absolute_error(y_test, y_pred_dt))
print("Decision Tree R2:", r2_score(y_test, y_pred_dt))

models = ['Linear Regression', 'Decision Tree']
mae_scores = [
    mean_absolute_error(y_test, y_pred_lr),
    mean_absolute_error(y_test, y_pred_dt)]

plt.plot(models, mae_scores)
plt.title("Model Comparison (MAE)")
plt.ylabel("Mean Absolute Error")
plt.show()


print("Enter values to predict Deaths")

confirmed = int(input("Confirmed cases: "))
recovered = int(input("Recovered cases: "))
active = int(input("Active cases: "))

prediction = dt.predict([[confirmed, recovered, active]])

print("Predicted Deaths:", int(prediction[0]))
