#! /usr/bin/env python

"""
File: final.py
Copyright (c) 2016 Taylor Patti
License: MIT

Description: A fourth-order Runga-Kutta integrator which uses a system of three coupled equations. Contains various plotting
functions as well as functions required in order to generate bifurcation diagrams for each equation.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Rossler():
    """Class which contains the differential equations and the rk4 method required to integrate them."""
    
    def __init__(self, c, dt=0.001, T0=250, T=500):
        """Begins a class based on the parameter values given."""
        self.c = c
        self.a = self.b = 0.2
        self.dt = dt
        self.T =T
        self.num = int(T / float(dt))
        self.t = np.linspace(0, T, self.num)
        self.x = np.zeros(self.num)
        self.y = np.zeros(self.num)
        self.z = np.zeros(self.num)
    
    def x_dot(self, t, x, y, z):
        """The first differential equation."""
        return(- y - z)
    
    def y_dot(self, t, x, y, z):
        """The second differential equation."""
        return(x + self.a * y)
    
    def z_dot(self, t, x, y, z):
        """The third differential equation."""
        return(self.b + z * (x - self.c))
    
    def run(self):
        """Carries out the rk4 differential equation integration for the three differential equations."""
        
        x = y = z = 0
        
        for i in range(1, self.num):
            k1_x = self.dt*self.x_dot(self.t[i-1], x, y, z)
            k1_y = self.dt*self.y_dot(self.t[i-1], x, y, z)
            k1_z = self.dt*self.z_dot(self.t[i-1], x, y, z)

            k2_x = self.dt*self.x_dot(self.t[i-1] + self.dt / 2.0, x + 0.5*k1_x, y + 0.5*k1_y, z + 0.5*k1_z)
            k2_y = self.dt*self.y_dot(self.t[i-1] + self.dt / 2.0, x + 0.5*k1_x, y + 0.5*k1_y, z + 0.5*k1_z)
            k2_z = self.dt*self.z_dot(self.t[i-1] + self.dt / 2.0, x + 0.5*k1_x, y + 0.5*k1_y, z + 0.5*k1_z)

            k3_x = self.dt*self.x_dot(self.t[i-1] + self.dt / 2.0, x + 0.5*k2_x, y + 0.5*k2_y, z + 0.5*k2_z)
            k3_y = self.dt*self.y_dot(self.t[i-1] + self.dt / 2.0, x + 0.5*k2_x, y + 0.5*k2_y, z + 0.5*k2_z)
            k3_z = self.dt*self.z_dot(self.t[i-1] + self.dt / 2.0, x + 0.5*k2_x, y + 0.5*k2_y, z + 0.5*k2_z)

            k4_x = self.dt*self.x_dot(self.t[i-1] + self.dt / 2.0, x + k3_x, y + k3_y, z + k3_z)
            k4_y = self.dt*self.y_dot(self.t[i-1] + self.dt / 2.0, x + k3_x, y + k3_y, z + k3_z)
            k4_z = self.dt*self.z_dot(self.t[i-1] + self.dt / 2.0, x + k3_x, y + k3_y, z + k3_z)


            self.x[i] = x = x + (k1_x + k2_x + k2_x + k3_x + k3_x + k4_x)/6
            self.y[i] = y = y + (k1_y + k2_y + k2_y + k3_y + k3_y + k4_y)/6
            self.z[i] = z = z + (k1_z + k2_z + k2_z + k3_z + k3_z + k4_z)/6

        return self.x, self.y, self.z
    
    def plotx(self):
        """Plots x vs t"""
        plt.plot(self.t, self.x)
        plt.title('x vs t')
        plt.xlabel('t')
        plt.ylabel('x')
        plt.ylim([-12, 12])
        
    def ploty(self):
        """Plots y vs t"""
        plt.plot(self.t, self.y)
        plt.title('y vs t')
        plt.xlabel('t')
        plt.ylabel('y')
        plt.ylim([-12, 12])
        
    def plotz(self):
        """Plots z vs t"""
        plt.plot(self.t, self.z)
        plt.title('z vs t')
        plt.xlabel('t')
        plt.ylabel('z')
        plt.ylim([0, 25])
        
    def plotxy(self):
        """Plots x vs y"""
        plt.plot(self.x[self.num/2:-1], self.y[self.num/2:-1])
        plt.title('x vs y')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim([-12, 12])
        plt.ylim([-12, 12])
        
    def plotyz(self):
        """Plots y vs z"""
        plt.plot(self.y[self.num/2:-1], self.z[self.num/2:-1])
        plt.title('y vs z')
        plt.xlabel('y')
        plt.ylabel('z')
        plt.xlim([-12, 12])
        plt.ylim([0, 25])
        
    def plotxz(self):
        """Plots x vs z"""
        plt.plot(self.x[self.num/2:-1], self.z[self.num/2:-1])
        plt.title('x vs z')
        plt.xlabel('x')
        plt.ylabel('z')
        plt.xlim([-12, 12])
        plt.ylim([0, 25])
        
    def plotxyz(self):
        """Plots a 3-D plot of x, y, and z"""
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(self.x[self.num/2:-1], self.y[self.num/2:-1], self.z[self.num/2:-1])
        ax.set_title('x and y vs z')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_xlim([-12, 12])
        ax.set_ylim([-12, 12])
        ax.set_zlim([0, 25])
        
    def findmaxima(self, x):
        """Finds the local maxima of integrated functions."""
        maxima = [max(x[self.num/2:-1])]
        for i in range(self.num / 2, self.num - 1):
            if((x[i] - 0.000001 > x[i-1]) and (x[i] - 0.000001 > x[i+1])):
                maxima.append(x[i])
        return maxima
    
def plotmaxima(indexval):
    """Makes bifurcation diagrams for the integrated function indicated by the indexval for x, y, and z"""
    c_values = np.linspace(2, 6, int(4/0.001))
    limlist = [[3, 12], [-1, 12], [-2, 27]]
    for c in c_values:
        solution = Rossler(c, dt = 0.05)
        data = solution.run()[indexval]
        max_list = solution.findmaxima(data)
        plt.plot([c]*len(max_list), max_list, 'ko', markersize=0.001)
    plt.title('Max Value vs c')
    plt.ylim(limlist[indexval])
    plt.ylabel('Max Value')
    plt.xlabel('c')

def test_z_dot():
    """Ensures that the z_dot definition works."""
    example = Rossler(2)
    apt = ((np.abs(example.z_dot(0, 1, 0, 1) + 0.8) < 1e-6))
    msg = 'z_dot function fails.'
    assert apt, msg
    
def test_run():
    """Compares the value of x after the first step for a c value of 2 to a hand-calculated result."""
    example = Rossler(2)
    apt = ((np.abs(example.run()[0][1] + 1e-7) < 1e-8))
    msg = 'Run calculation failure for x.'
    assert apt, msg