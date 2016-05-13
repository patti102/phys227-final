# phys227-final


**Author:** Taylor Patti

[![Build Status](https://travis-ci.org/chapman-phys227-2016s/phys227-final.svg?branch=master)](https://travis-ci.org/chapman-phys227-2016s/phys227-final)

**Due date:** 2016/04/28

## Specification

We will now get really real with coupled differential equations in that we will implement not just a set of two, but rather, three equations, x, y, and z. Moreover, we are now adding some non-linearity, as two of the equations, x and z, are now combined in the relation zx. Let's look at those equations now.

$$\dot{x} = -y -z $$
$$\dot{y} = x = ay$$
$$\dot{z} = b + z(x - c)$$

We will be fixing the parameters of $a$ and $b$ at a bland $a = b = 0.2$ for the purposes of this final, but we could adjust them to observe certain effects. Instead, we will be focusing on changing $c$, which will produce well behaved oscillatory motion once steady state has been reached, or chaotic motion, or any number of fixed points inbetween, depending on the value of the $c$ parameter.

To do this we are going to use a 4th-Order Runga-Kutta integration process. We will then plot it in a variety of creative ways, showing both non-chaotic and chaotic behavior, as well as illustrating dependence of the maxima on the parametric value of c.

We will ultimately generate bifurcation diagrams for x, y, and z by varying the c value over a densely perforated mesh of c values and plotting the resulting maximum values, each distinct maximum value representing a distinct cycle with its own periodicity at that c value point.

## Assessment



## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

I looked up error codes, as always.

Signed,

Taylor Patti
