import numpy as np

class ACT_reservoir:
    def __init__(self, input_dim, hidden_dim, output_dim, max_iter=20):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.max_iter = max_iter
        
        self.total_dim = 1 + input_dim + hidden_dim + output_dim + 1  # Including bias and halting node
        self.W = np.random.uniform(-2, 2, (self.total_dim, self.total_dim))

        # Index ranges for different parts of the state vector
        self.input_indices = range(1, input_dim + 1)
        self.hidden_indices = range(input_dim + 1, input_dim + hidden_dim + 1)
        self.output_indices = range(input_dim + hidden_dim + 1, input_dim + hidden_dim + output_dim + 1)
        self.halting_index = input_dim + hidden_dim + output_dim + 1

    def relu(self,x):
        return np.maximum(0, x)

    def predict(self, xi):
        # Create initial state vector with given input, xi, and set bias unit to 1
        self.x = np.zeros((self.total_dim, 1))
        self.x[0] = 1  # Bias unit
        self.x[self.input_indices] = xi.reshape((self.input_dim, 1))  # Input part

        t = 0
        while t < self.max_iter and self.x[self.halting_index][0] <= 1:
            self.x = self.relu(self.W @ self.x) #the core of the network
            t += 1

        # Extracting and returning the output part of the state vector
        return self.x[self.output_indices],t

    def summary(self):
        print("Total Parameters:", self.total_dim ** 2)  # Since W is a square matrix
        print("Input Dimension:", self.input_dim)
        print("Hidden Dimension:", self.hidden_dim)
        print("Output Dimension:", self.output_dim)
        print("Max Iterations:", self.max_iter)