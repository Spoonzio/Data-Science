from sklearn import tree

# Inititate tree
classify = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
dataX = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# Gender matching dataset 1
dataY = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

# Form tree
classify = classify.fit(dataX, dataY)

# Get int input
while True:
    try:
        height = int(input("Enter your height:\n"))
        weight = int(input("Enter your weight:\n"))
        shoe_size = int(input("Enter your shoe size:\n"))
    except TypeError:
        continue
    else:
        break

# Predict result base on tree
guess = classify.predict([[height, weight, shoe_size]])

# Print result
print("You are:" + str(guess[0]))