from matplotlib import pyplot as plt
import numpy as np
import rk2_pendulum

def main():
  create_bifurcation_plot(0, 1.7)
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

  # run an runge kutta 2 for 20 seconds
  pendulum.run_rk2(20)

  # plot theta vs time
  plt.plot(pendulum.get_time_array(), pendulum.get_theta_array())
  plt.title(f"non-chaotic driven damped pendulum Fd = {fDriving}")
  plt.xlabel("time (s)")
  plt.ylabel("theta (radians)")
  plt.show()


def recreate_fig_3_6():
  '''
  This figure shows a chaotic pendulum theta vs. t.
  Slightly adjusting initial conditions dramatically
  changes the outcome. 
  '''
  # define our initial conditions to match fig 3.6
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

  # run our rk2 simulation, specifying our initial theta
  pendulum.run_rk2(simulationTime, th_initial=theta_i)

  # plot theta vs. time
  plt.plot(pendulum.get_time_array(), pendulum.get_theta_array())
  plt.title(f"Chaotic driven damped pendulum Fd = {fDriving}")
  plt.xlabel("time (s)")
  plt.ylabel("theta (radians)")
  plt.show()


def recreate_fig_3_8():
  '''
  This figure shows a chaotic pendulum 
  theta vs. omega. (a phase diagram)
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
  # (this function makes sure theta stays
  # between -pi and pi)
  pendulum.set_reset_theta(True)

  # run rk2 simulation
  pendulum.run_rk2(simulationTime, th_initial=theta_i)

  # plot theta vs. omega
  plt.plot(pendulum.get_theta_array(), pendulum.get_omega_array(), "r,")
  plt.title(f"Phase space plot for the chaotic pendulum Fd = {fDriving}")
  plt.xlabel("theta (radians)")
  plt.ylabel("omega (radians/s)")
  plt.show()


def create_poincare_plot(f_driving=1.2):
  '''
  This is another theta vs omega plot, but only at times
  when time is "in phase" with the driving force. this means
  only plotting when omegad*t = 2npi where n is an int.
  in our case, we will plot when abs(t - 2npi/omegad) < dt/2.
  '''
  # define our driving and damping forces
  fDriving = f_driving
  fDamping = .5
  omegaDriving = 2/3
  pendulumLength = 9.8
  theta_i = .2
  dt = .01

  # initialize our pendulum
  pendulum = rk2_pendulum.Pendulum(fDriving, fDamping, omegaDriving)

  # set parameters
  pendulum.set_length(pendulumLength)
  pendulum.set_dt(dt)

  # reset theta to see the pattern
  pendulum.set_reset_theta(True)

  # run a poincare simulation with 500 periods
  drivingPeriods = 500
  pendulum.run_poincare(drivingPeriods, th_initial=theta_i)

  # now plot
  plt.plot(pendulum.get_theta_array(), pendulum.get_omega_array(), 'g.')
  plt.title(f"Poincare plot, Fd = {fDriving}")
  plt.xlabel("theta (radians)")
  plt.ylabel("omega (radians/s)")
  plt.show()


def recreate_fig_3_10(fd=1.4):
  '''
  This figure shows theta vs. time, showing that even in a
  chaotic system there can arise patterns. This takes in 
  optional driving force (fd) and plots rk2 theta vs. time
  '''
  # define our driving and damping forces
  fDamping = .5
  omegaDriving = 2/3
  pendulumLength = 9.8
  simulationTime = 100
  theta_i = .2

  # initialize our pendulum
  pendulum = rk2_pendulum.Pendulum(fd, fDamping, omegaDriving)

  # set parameters
  pendulum.set_length(pendulumLength)
  pendulum.set_reset_theta(True)

  # run rk2 simulation
  pendulum.run_rk2(simulationTime, th_initial=theta_i)

  # plot theta vs time
  plt.plot(pendulum.get_time_array(), pendulum.get_theta_array(),)
  plt.title(f"Driving force: {fd}")
  plt.xlabel("time (s)")
  plt.ylabel("theta (radians)")
  plt.show()



def create_bifurcation_plot(fd_i=1.35, fd_f=1.5):
  '''
  This run will be more computationally expensive.
  We need to do a run for 400 drive periods, or until
  n = 400. We discard the first 300, so the oscillations can settle. 
  Then, we plot only thetas in phase with driving 
  force, much like we did in the poincare plot. Then, 
  we repeat for many driving forces from 1.35 to 1.5.
  Finally, plot Fd vs. theta.
  '''

  fd_initial = fd_i
  fd_final = fd_f
  fDamping = .5
  omegaDriving = 2/3
  pendulumLength = 9.8
  theta_i = .2

  # total runs and runs to keep can be adjusted
  # for better computational performance
  total_runs = 100
  runs_to_keep = 40

  # get an arrays of driving forces for our range
  fds = np.linspace(fd_initial, fd_final, 100)

  # init pendulum
  pendulum = rk2_pendulum.Pendulum(fd_initial, fDamping, omegaDriving)
  pendulum.set_length(pendulumLength)
  pendulum.set_reset_theta(True)

  # start looping through driving force array
  for fd in fds:

    # set pendulum's driving force to fd
    pendulum.set_params(fd, fDamping, omegaDriving)

    # run a poincare simulation
    pendulum.run_poincare(total_runs, th_initial=theta_i)

    # discard the first data points to remove randomness
    thetas = pendulum.get_theta_array()[runs_to_keep:]

    # plot a dot for each theta corresponding to fd
    for theta in thetas:
      plt.plot(fd, theta, '.')

    # print something so we know it's working
    print(f"{fd} done plotting")

    # now reset the pendulum
    pendulum.reset()

  # show plot
  plt.title("Bifurcation diagram")
  plt.xlabel("Fd")
  plt.ylabel("theta (radians)")
  plt.show()




if __name__ == "__main__":
  main()