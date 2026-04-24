from sklearn.ensemble import RandomForestClassifier

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

model = RandomForestClassifier()
model.fit(X,y)

print("Prediction:", model.predict([[2.5]]))
