from sklearn import svm

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

model = svm.SVC()
model.fit(X,y)

print("Prediction:", model.predict([[2.5]]))
