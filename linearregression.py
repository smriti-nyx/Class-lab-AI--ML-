import numpy as np
X = np.array([
    [600, 2],
    [650, 2],
    [700, 2],
    [750, 3],
    [800, 3],
    [850, 3],
    [900, 3],
    [950, 3],
    [1000, 4],
    [1050, 4],
    [1100, 4],
    [1150, 4],
    [1200, 4],
    [1250, 5],
    [1300, 5],
    [1350, 5],
    [1400, 5],
    [1450, 5],
    [1500, 6],
    [1600, 6]
])

y = np.array([
    32, 35, 38, 45, 48, 52, 55, 58, 65, 68,
    72, 75, 78, 85, 88, 92, 95, 98, 105, 112
])

m = len(y)   #   m =20 [1, 600, 2]
X = np.c_[np.ones(m), X]     #(1 × θ₀) + (area × θ₁) + (bedrooms × θ₂) =y 
theta = np.zeros(X.shape[1])  #[ 0, 0,0 ]
alpha = 0.00000001      #learning rate        
iterations = 1000.       #1000 times loop ran 
def compute_cost(X, y, theta):  #function to find the cost of the house 
    predictions = X.dot(theta)  # [1 * theta not , area * theta 1 , rooms* theta 2 ] =y(output)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost
for i in range(iterations):
    predictions = X.dot(theta)
    gradient = (1 / m) * X.T.dot(predictions - y)
    theta = theta - alpha * gradient
X_test = np.array([1, 1200, 3])
predicted_price = X_test.dot(theta)

print("Estimated Housing Price:", predicted_price, "Lakhs")