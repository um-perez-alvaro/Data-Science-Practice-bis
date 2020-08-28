# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:41:26 2020

@author: javier.perez-alvaro
"""
from matplotlib.colors import ListedColormap
def plot_decision_boundary(clf, X, y, labels, transformation = None):
    import numpy as np
    import matplotlib.pyplot as plt
    '''Function for plotting the classification boundaries.
    
    INPUTS:
    
        clf: a sklearn classifier
        
        X: features matrix 
        
        y: target vector ({0,1} or {0,1,2})
        
        labels: vector with the class labels
    '''
    # get axes names
    axes_names = X.columns
    # get axes limits
    axes=[X.iloc[:,0].min()-0.5, X.iloc[:,0].max()+0.5, X.iloc[:,1].min()-0.5, X.iloc[:,1].max()+0.5]
    # create a 100x100 meshgrid
    x1s = np.linspace(axes[0], axes[1], 1000)
    x2s = np.linspace(axes[2], axes[3], 1000)
    x1, x2 = np.meshgrid(x1s, x2s) 
    X_new = np.c_[x1.ravel(), x2.ravel()]
    # make a prediction at each point of the mesh grid
    if transformation == None:
        y_pred = clf.predict(X_new).reshape(x1.shape)
    else:
        X_new_transformed = transformation.transform(X_new)
        y_pred = clf.predict(X_new_transformed).reshape(x1.shape)
    custom_cmap = ListedColormap(['#fafab0','#9898ff','#a0faa0']) # some nice colors
    # contour map
    colors = ['blue','red','green']
    plt.contourf(x1, x2, y_pred, alpha=0.3, cmap=custom_cmap)
    for i in range(len(labels)):
        plt.plot(X.loc[y==i,axes_names[0]],X.loc[y==i,axes_names[1]], 'o', color=colors[i], label = labels[i])

    'set axes'
    plt.axis(axes)
    'axes labels'
    plt.xlabel("Petal length", fontsize=14)
    plt.ylabel("Petal width", fontsize=14)
    'plot legend'
    plt.legend(loc="lower right", fontsize=14)