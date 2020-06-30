import numpy as np
import matplotlib.pyplot as plt

n = 10000
rhos = [0.5, 0.8, 0.99, 1]
b = 1
X = np.zeros(n)
E = np.random.randint(-100, 100, n)


for rho in rhos:
    
    for i in range(len(X) - 1):
        e = np.random.choice(E)
        X[i+1] = rho*X[i] + b*e

    plt.plot(X)
    plt.title('rho = {}'.format(rho))
    plt.show()
