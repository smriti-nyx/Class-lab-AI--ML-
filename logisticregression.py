#generate a csv file (homework)


import numpy as np
import math

def sigmoid(z):   # z = w1x1 + w2x2 + w3x3 + w4x4+..+b z can acquire any value .
#sigmoid coverts the linear expression z into probability using 
    return 1 / (1 + math.exp(-z)) #sigmoid(z) = 1\ 1+e^(-z)

X_train = [
    [35, 120, 180, 22.5], [42, 130, 195, 24.1], [45, 135, 200, 25.0],
    [50, 140, 210, 26.3], [52, 145, 220, 27.5], [55, 150, 230, 28.4],
    [60, 160, 250, 30.1], [48, 138, 205, 26.0] #training input dataset 
]
y_train = [0, 0, 0, 1, 1, 1, 1, 0] #disease ouput 

w1, w2, w3, w4 = 0.0, 0.0, 0.0, 0.0 #initialising the parameters for new unknown dataset.

bias = 0.0  #bias is rep by b , Bias allows the model to shift the 
#decision boundary. Bias directly shifts prediction.


learning_rate = 0.000001 #the rate by which we move through the gradient descent.


for i in range(100000): # 1000 iterations 
    dw1, dw2, dw3, dw4, db = 0, 0, 0, 0, 0 #starting
    m = len(X_train) #gives the 8 sets

    for j in range(m): #m = 8 
        z = (w1 * X_train[j][0]) + (w2 * X_train[j][1]) + \
            (w3 * X_train[j][2]) + (w4 * X_train[j][3]) + bias
      
          
          #X_train[j] = [Age, BP, Cholesterol, BMI]
          #X_train[0] = [35,120,180,22.5]
            #x1 = 35 x2 = 12. x3 = 18 x4 = 22.5






        prediction = sigmoid(z)

        error = prediction - y_train[j]


        #Gradient for wi​=error× xi
        #adding up gradient contributions

        dw1 += error * X_train[j][0]
        dw2 += error * X_train[j][1]
        dw3 += error * X_train[j][2]
        dw4 += error * X_train[j][3]
        db  += error



     #the parameters getting updated n  becoming more error- less
    w1 = w1 - (learning_rate * dw1 / m)
    w2 = w2 - (learning_rate * dw2 / m) 
    w3 = w3 - (learning_rate * dw3 / m)
    w4 = w4 - (learning_rate * dw4 / m)
    bias = bias - (learning_rate * db / m)

X_test = [
    [40, 128, 190, 23.8], [47, 138, 205, 26.2],
    [53, 148, 225, 28.0], [58, 155, 240, 29.5]
]

print(" Final Predictions \n")
for sample in X_test:
    z = (w1 * sample[0]) + (w2 * sample[1]) + \
        (w3 * sample[2]) + (w4 * sample[3]) + bias

    prob = sigmoid(z)

    if prob >= 0.5:
        result = "Disease (1)"
    else:
        result = "No Disease (0)"

    print("Probability of Disease:", round(prob, 4))
    print("Predicted Disease:", result)
    print("\n")