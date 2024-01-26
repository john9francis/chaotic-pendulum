from matplotlib import pyplot as plt
import rk2_pendulum

def main():
  
  recreate_fig_3_6()

  pass

def recreate_fig_3_5():
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
  # define our driving and damping forces
  fDriving = 1.2
  fDamping = .5
  omegaDriving = 2/3

  # initialize our pendulum
  pendulum = rk2_pendulum.Pendulum(fDriving, fDamping, omegaDriving)

  # set parameters
  pendulum.set_length(9.8)

  pendulum.run_rk2(60, th_initial=.2)
  plt.plot(pendulum.get_time_array(), pendulum.get_theta_array())
  plt.show()


if __name__ == "__main__":
  main()