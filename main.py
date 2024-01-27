from matplotlib import pyplot as plt
import numpy as np
import rk2_pendulum

def main():
  
  create_poincare_plot()

  pass

def recreate_fig_3_5():
  '''
  This figure shows a non-chaotic driven-damped pendulum
  it plots theta vs. t.
  basically it settles down to a repeating pattern.
  '''

  # define our driving and damping forces
  fDriving = .2
  fDamping = 1
  omegaDriving = 2

  # initialize our pendulum
  pendulum = rk2_pendulum.Pendulum(fDriving, fDamping, omegaDriving)
  pendulum.run_rk2(20)
  plt.plot(pendulum.get_time_array(), pendulum.get_theta_array())
  plt.show()

def recreate_fig_3_6():
  '''
  This figure shows a chaotic pendulum theta vs. t.
  Slightly adjusting initial conditions dramatically
  changes the outcome. 
  '''
  # define our driving and damping forces
  fDriving = 1.2
  fDamping = .5
  omegaDriving = 2/3
  pendulumLength = 9.8
  simulationTime = 60
  theta_i = .2

  # initialize our pendulum
  pendulum = rk2_pendulum.Pendulum(fDriving, fDamping, omegaDriving)

  # set parameters
  pendulum.set_length(pendulumLength)

  pendulum.run_rk2(simulationTime, th_initial=theta_i)
  plt.plot(pendulum.get_time_array(), pendulum.get_theta_array())
  plt.show()


def recreate_fig_3_8():
  '''
  This figure shows a chaotic pendulum theta vs. omega.
  It shows an interesting pattern and shape. 
  '''
  # define our driving and damping forces
  fDriving = 1.2
  fDamping = .5
  omegaDriving = 2/3
  pendulumLength = 9.8
  simulationTime = 500
  theta_i = .2

  # initialize our pendulum
  pendulum = rk2_pendulum.Pendulum(fDriving, fDamping, omegaDriving)

  # set parameters
  pendulum.set_length(pendulumLength)

  # reset theta to see the pattern
  pendulum.set_reset_theta(True)

  pendulum.run_rk2(simulationTime, th_initial=theta_i)
  plt.plot(pendulum.get_theta_array(), pendulum.get_omega_array(), "r,")
  plt.show()


def create_poincare_plot():
  '''
  This is another theta vs omega plot, but only at times
  when time is "in phase" with the driving force. this means
  only plotting when omegad*t = 2npi where n is an int.
  in our case, we will plot when abs(t - 2npi/omegad) < dt/2.
  '''
  # define our driving and damping forces
  fDriving = 1.2
  fDamping = .5
  omegaDriving = 2/3
  pendulumLength = 9.8
  simulationTime = 5000
  theta_i = .2
  dt = .01

  # initialize our pendulum
  pendulum = rk2_pendulum.Pendulum(fDriving, fDamping, omegaDriving)

  # set parameters
  pendulum.set_length(pendulumLength)
  pendulum.set_dt(dt)

  # reset theta to see the pattern
  pendulum.set_reset_theta(True)

  pendulum.run_poincare(500, th_initial=theta_i)

  # now plot
  plt.plot(pendulum.get_theta_array(), pendulum.get_omega_array(), 'g.')
  plt.show()


def create_bifurcation_plot():
  '''
  This run will be more computationally expensive.
  We need to do a run for 400 drive periods, or until
  n = 400. We discard the first 300, so the oscillations can settle. 
  Then, we plot only thetas in phase with driving 
  force, much like we did in the poincare plot. Then, 
  we repeat for many driving forces from 1.35 to 1.5.
  Finally, plot Fd vs. theta.
  '''

  fDriving = 1.2
  fDamping = .5
  omegaDriving = 2/3

  thetas = []
  fds = []

  pendulum = rk2_pendulum.Pendulum(fDriving, fDamping, omegaDriving)

  # do 400 rounds while omega is in phase with t
  n = 1
  #while n < 400:


if __name__ == "__main__":
  main()