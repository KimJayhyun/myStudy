import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 가중치와 편향을 초기화해주는 함수

def init_network():
    network = {}
    
    network["W1"] = np.array([
        [0.1, 0.3, 0.5],
        [0.2, 0.4, 0.6]
        ])
    
    network["b1"] = np.array([0.1, 0.2, 0.3])
    
    network["W2"] = np.array([
      [0.1, 0.4],
      [0.2, 0.5],
      [0.3, 0.6]  
    ])

    network["b2"] = np.array([
        [0.1, 0.2]
    ])

    network["W3"] = np.array([
        [0.1, 0.3],
        [0.2, 0.4]
    ])

    network["b3"] = np.array([
        [0.1, 0.2]
    ])

    return network

# 입력 신호를 출력으로 변환하는 과정(순방향)

def forward(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    Z1 = sigmoid(a1)
 
    a2 = np.dot(Z1, W2) + b2
    Z2 = sigmoid(a2)

    a3 = np.dot(Z2, W3) + b3
    y = a3

    return y

network = init_network()
x = np.array([1.0, 0.5])

y = forward(network, x)

print(y)


