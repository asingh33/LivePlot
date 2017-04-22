#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:36:41 2017

@author: abhisheksingh
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

import socket
import json

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    
    try:
        with open('sample.txt','r') as outfile:
            array = json.load(outfile)
    except ValueError as err:
        print err
    else:
        #print array
        
        xar= [1, 2, 3, 4]
        yar = []
        xtitles = ['']
        
        indexvalue = 0
        for items in array:
            #xar.append(int(x))
            yar.append(array[items])
            xtitles.append(items)
        
        ax1.clear()        
        plt.bar(xar,yar, align='center')
        plt.xticks(np.arange(5), xtitles)


def Main():
    
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

if __name__ == "__main__":
    Main()




        
