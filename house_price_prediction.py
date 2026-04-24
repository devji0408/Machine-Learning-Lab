import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Area":[1000,1500,2000,2500],
    "Price":[10,15,20,25]
}

df = pd.DataFrame(data)

X = df[["Area"]]
y = df["Price"]

model = LinearRegression()
model.fit(X,y)

print("Price for 1800 area:", model.predict([[1800]]))
