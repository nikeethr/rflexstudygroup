import math
import numpy as np

#def basic_sigmoid(x):
#    s = 1 / (1 + math.exp(-x))
#    return s

def basic_sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s

def sigmoid_derivative(x):
    s = basic_sigmoid(x)
    ds = s * (1 - s)
    return ds

def image2vector(image):
    image = image.reshape(image.shape[0] * image.shape[1] * image.shape[2], 1)
    return image

def normalizeRows(x):
    x_norm = np.linalg.norm(x, ord=2, axis=1, keepdims=True)
    x = x / x_norm
    return x

def softmax(x):
    ex = np.exp(x)
    ex = ex / np.sum(ex, axis=1, keepdims=True)
    return ex

def L1(yhat, y):
    loss = np.sum(np.abs(y - yhat))
    return loss

def L2(yhat, y):
    loss = np.dot(yhat - y, yhat - y)
    return loss

if __name__ == "__main__":
    print("basic_sigmoid(3)")
    print(basic_sigmoid(3))

    x = np.array([1,2,3])

    print("basic_sigmoid([1,2,3])")
    print(basic_sigmoid(x))

    print("sigmoid_derivative([1,2,3])")
    print(sigmoid_derivative(x))

    image = np.array(
       [[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])

    print ("image2vector(image) = " + str(image2vector(image))) 

    x = np.array([
        [0, 3, 4],
        [1, 6, 4]])

    print("normalizeRows(x) = " + str(normalizeRows(x)))

    x = np.array([
        [9, 2, 5, 0, 0],
        [7, 5, 0, 0 ,0]])

    print("softmax(x) = " + str(softmax(x))) 

    yhat = np.array([.9, 0.2, 0.1, .4, .9])
    y = np.array([1, 0, 0, 1, 1])
    print("L1 = " + str(L1(yhat,y)))

    yhat = np.array([.9, 0.2, 0.1, .4, .9])
    y = np.array([1, 0, 0, 1, 1])
    print("L2 = " + str(L2(yhat,y)))
