from sklearn.ensemble import RandomForestClassifier
X = [[190,70,44],[166,65,45],[190,90,47],[175,64,39],[171,75,40],[177,80,42],[160,60,38],[144,54,37]]
Y = ['male','male','male','male','female','female','female','female']
P = [[190,80,46]]
rfor = RandomForestClassifier()
rfor.fit(X,Y)
print "4) Using RandomForestClassifier Prediction is " + str(rfor.predict(P)) +"\n"
