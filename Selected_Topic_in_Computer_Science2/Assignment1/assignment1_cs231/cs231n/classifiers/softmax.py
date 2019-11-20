from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    scores = X.dot(W)
    num_data = X.shape[0]
    num_classes = W.shape[1]
    # calculate loss function
    # reference https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/
    for i in range(num_data):
        
        # numeric stability http://cs231n.github.io/linear-classify/
        # shift values for 'scores' for numeric reasons (over-flow cautious)
        scores[i] -= scores[i].max() # for numeric stability  
        scores_expsum = np.sum(np.exp(scores[i]))
        target_exp = np.exp(scores[i][y[i]])
        loss += - np.log( target_exp / scores_expsum)
        
        # for correct class
        dW[:, y[i]] += (-1) * (scores_expsum - target_exp) / scores_expsum * X[i]
        for j in xrange(num_classes):
            # pass correct class gradient
            if j == y[i]:
                continue
            # for incorrect classes
            dW[:, j] += np.exp(scores[i][j]) / scores_expsum * X[i]
    
    loss /= num_data
    loss += reg * np.sum(W * W)
    dW /= num_data
    dW += 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_data = X.shape[0]
    scores = X.dot(W)
    scores -= np.max(scores)
    scores = np.exp(scores)
    scores_sums = np.sum(scores, axis=1)
    target_exp = scores[range(num_data), y]
    loss = scores[np.arange(num_data),y]/scores_sums
    loss = -np.sum(np.log(loss))/num_data + reg * np.sum(W * W)
    
    # np.divide fucntion reference
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.divide.html
    s = np.divide(scores, scores_sums.reshape(num_data, 1))
    s[range(num_data), y] = - (scores_sums - target_exp) / scores_sums
    dW = X.T.dot(s)
    dW /= num_data
    dW += 2 * reg * W

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
