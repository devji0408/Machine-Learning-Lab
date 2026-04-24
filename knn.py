from sklearn.neighbors import KNeighborsClassifier

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)

print("Prediction:", model.predict([[2.5]]))
