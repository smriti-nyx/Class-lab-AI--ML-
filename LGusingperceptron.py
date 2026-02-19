import numpy as np

# Step activation function
def step(z):
    return 1 if z >= 0 else 0


# Input combinations for 2-input logic gates
inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])


# Perceptron training function
def train_perceptron(T, lr=0.1, epochs=20):
    w = np.array([0.0, 0.0])   # weights
    b = 0.0                    # bias

    for _ in range(epochs):
        for i in range(len(inputs)):
            net = np.dot(w, inputs[i]) + b
            y = step(net)
            error = T[i] - y

            w = w + lr * error * inputs[i]
            b = b + lr * error

    return w, b


# Testing function
def test_gate(name, T):
    w, b = train_perceptron(T)

    print(name, "Gate")
    print("Final w:", w, "Final b:", b)

    for x1, x2 in inputs:
        net = (w[0] * x1) + (w[1] * x2) + b
        print(x1, x2, "->", step(net))
    print()


# Testing different gates
test_gate("AND", np.array([0, 0, 0, 1]))
test_gate("OR", np.array([0, 1, 1, 1]))
test_gate("NAND", np.array([1, 1, 1, 0]))
test_gate("XOR", np.array([0, 1, 1, 0]))






import numpy as np

def step(z):
    if z >= 0:
        return 1
    return 0

def xor(x1, x2):

   
    
    w_or = np.array([1, 1])
    b_or = -0.5

   
    w_nand = np.array([-1, -1])
    b_nand = 1.5

    x = np.array([x1, x2])

    
    z_or = np.dot(w_or, x) + b_or
    h1 = step(z_or)

  
    z_nand = np.dot(w_nand, x) + b_nand
    h2 = step(z_nand)

   

    w_and = np.array([1, 1])
    b_and = -1.5

    h = np.array([h1, h2])

    z_out = np.dot(w_and, h) + b_and
    y = step(z_out)

    return y



for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(x1, x2, xor(x1, x2))
