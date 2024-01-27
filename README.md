# Chaotic Pendulum
### author: John Francis 1/26/2024

# Overview
Chaos is an interesting phenomena in physics. In physics, we like to be able to predict something's behavior at a later time. Many systems have a predictable outcome, that doesn't vary much with initial conditions. For example. If someone were to throw a ball at 10 m/s from x = 1 m versus x = 1.0001 m, it would probably land in a very similar spot. Even in harder problems that can't be solved analytically, we can usually predict where they will be using a numerical method. For example, throwing a ball with air drag, magnus force, and coriolis force. 

Certain systems don't behave in such a predictable way. These are called chaotic systems. In a chaotic system, one extremely small change in an initial condition could cause a drastically different outcome down the line. 

Here we will explore a very simple chaotic system, the driven-damped pendulum. A driven-damped pendulum is an ideal pendulum, which periodically swings from the driving of gravity, and adds a linear damping force (friction or simplified air drag) as well as a periodic driving force. This periodic driving force is sinusodal, meaning that it has a period (omega) when it drives strongest. The driving force can be compared to somebody bumping the pendulum every one second periodically. The equations of motion for this pendulum are as follows:

$$f = ma$$





# Coding this problem

This code features a second order runge-kutta method to find the position of the pendulum at the next theta. There is a class, "Pendulum" that handles most of the logic. 

# Development environment

This simulation is coded in Python, using numpy and matplotlib libraries.

How to install using python virtual environment (windows):

```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```
