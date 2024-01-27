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

  pendulum.run_rk2(simulationTime, th_initial=theta_i)

  # now only save the data points when omegad is in phase
  poincare_thetas = []
  poincare_omegas = []
  
  original_thetas = pendulum.get_theta_array()
  original_omegas = pendulum.get_omega_array()
  original_times = pendulum.get_time_array()

  n = 1

  for i, time in enumerate(original_times):
    if abs(time - n*2*np.pi/omegaDriving) < dt/2:
      poincare_thetas.append(original_thetas[i])
      poincare_omegas.append(original_omegas[i])
      n += 1


  # now plot
  plt.plot(poincare_thetas, poincare_omegas, 'g.')
  plt.show()



if __name__ == "__main__":
  main()