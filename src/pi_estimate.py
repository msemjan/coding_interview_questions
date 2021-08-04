from random import random  # perform this import outside the function

def find_pi(n):
    """
    Function to estimate the value of Pi
    """
    inside=0

    for i in range(0,n):
        x=random()
        y=random()
        if (x*x+y*y)**(0.5)<=1:  # if i falls inside the circle
            inside+=1

    pi=4*inside/n
    return pi
