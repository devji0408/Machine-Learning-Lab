from sklearn.linear_model import LogisticRegression

X = [[0],[1],[2],[3]]
y = [0,0,1,1]

model = LogisticRegression()
model.fit(X,y)

print("Prediction:", model.predict([[1.5]]))
