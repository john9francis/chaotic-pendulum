from matplotlib import pyplot as plt
import rk2_pendulum

def main():
  
  recreate_fig_3_8()

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
  #pendulum.set_reset_theta(True)

  pendulum.run_rk2(simulationTime, th_initial=theta_i)
  plt.plot(pendulum.get_theta_array(), pendulum.get_omega_array())
  plt.show()




if __name__ == "__main__":
  main()