# class that computes 2nd order runge kutta

import numpy as np

class Pendulum:

  # define constants

  # gravity acceleration
  G = 9.8
  # length of the pendulum
  L = 1
  # time step
  dt = .01


  # variables
  # fd is driving force,
  # omegad is driving frequency
  # and q is damping constant
  fd = None
  omegad = None
  q = None

  # lists
  times = []
  thetas = []
  omegas = []

  # flags
  # reset theta keeps theta between 0 and 2*pi
  reset_theta = False


  def __init__(self, fDriving, fDamping, omegaDriving) -> None:
    self.set_params(fDriving, fDamping, omegaDriving)


  # getters and setters
  def get_theta_array(self):
    '''Returns an np.array of thetas from a simulation'''
    return np.array(self.thetas)
  
  def get_omega_array(self):
    '''Returns an np.array of omegas from a simulation'''
    return np.array(self.omegas)
  
  def get_time_array(self):
    '''Returns an np.array of times from a simulation'''
    return np.array(self.times)
  
  def set_length(self, length):
    '''sets the length of the pendulum'''
    self.L = length

  def set_dt(self, new_dt):
    '''set timestep for simulations'''
    self.dt = new_dt

  def set_reset_theta(self, new_bool):
    '''
    true means theta will be adjusted it gets outside
    the range of -pi to pi
    '''
    self.reset_theta = new_bool




  def set_params(self, fDriving, fDamping, omegaDriving):
    '''adjust the pendulum parameters'''
    self.fd = fDriving
    self.q = fDamping
    self.omegad = omegaDriving

  def periodic_driving_force(self, t):
    '''returns the driving force which depends on t,
    this function is used for rk2 simulation'''
    return self.fd * np.sin(self.omegad * t)
  
  def damping_force(self, omega):
    '''returns the damping force which depends on omega,
    this function is used for rk2 simulation'''
    return - self.q * omega
  
  def gravity_force(self, theta):
    '''returns pendulum's force due to gravity which
    depends on theta, used for rk2 simulation'''
    return - (self.G / self.L) * np.sin(theta)
  

  # RK2 methods
  def rk2_derivs(self, th_om_array, t):
    '''
    Takes in an array of [θ, ω], 
    and damping force Q
    
    and returns and array of [dθ/dt, dω/dt]
    '''
    # grab our theta and omega from the array.
    th = th_om_array[0]
    om = th_om_array[1]
    
    # dtheta/dt = omega
    th_deriv = om
    
    # domega/dt = acceleration aka sum of all the forces
    acceleration = (
      self.gravity_force(th) +
      self.damping_force(om) +
      self.periodic_driving_force(t)
    )
    
    om_deriv = acceleration

    return np.array([th_deriv, om_deriv])
  

  def runge_kutta2(self, th_om_array):
    '''
    Takes in an array of [θ, ω]
    performs a 2nd order runge-kutta to find the
    theta and omega at the next time t + dt
    returns updated [θ, ω] 
    '''
    k1 = self.dt * self.rk2_derivs(th_om_array, self.times[-1])
    k2 = self.dt * self.rk2_derivs(th_om_array + 1/2 * k1, self.times[-1])
    
    updated = th_om_array + k2
    return updated


  def reset(self):
    '''clears out the pendulum's lists to get ready for another run'''
    self.times.clear()
    self.thetas.clear()
    self.omegas.clear()


  def run_rk2(self, time, t_initial=0, th_initial=.2, om_initial=0):
    '''
    takes in time and initial conditions, and
    uses rk2 to fill the theta and omega lists
    '''

    # set initial conditions to the lists
    self.times.append(t_initial)
    self.thetas.append(th_initial)
    self.omegas.append(om_initial)

    # loop until we reach the desired time
    while self.times[-1] < time:

      # grab our theta and omega value from the lists
      current_th = self.thetas[-1]
      current_om = self.omegas[-1]

      # get the updated theta and omega from runge kutta function
      updated_array = self.runge_kutta2([current_th, current_om])

      theta = updated_array[0]
      omega = updated_array[1]

      # keep theta between -pi and pi if desired
      if self.reset_theta:
        if theta > np.pi:
          theta -= 2*np.pi
        if theta < -np.pi:
          theta += 2*np.pi

      # add the new theta and new omega to our thetas and omegas lists
      self.thetas.append(theta)
      self.omegas.append(omega)

      # add the time to the times list
      self.times.append(self.times[-1] + self.dt)



  def run_poincare(self, rounds, t_initial=0, th_initial=.2, om_initial=0):
    '''
    Takes in 'rounds' which is how many periods
    of the driving frequency (omegad) we want to run,
    then populates our lists with only the thetas and
    omegas when that omegad was in phase. aka
    when t = 2*n*pi/omegad where n = 1,2,3,...
    rounds is synonomous to n in this case.
    '''

    # step one: convert rounds into time.
    time = 2*np.pi*rounds/self.omegad

    # run an rk2 simulation with that specific time
    self.run_rk2(time, th_initial=th_initial)

    # now only save the data points when omegad is in phase
    #
    # initialize some lists to store our updated data
    poincare_thetas = []
    poincare_omegas = []

    # get the original rk2 arrays
    original_thetas = self.get_theta_array()
    original_omegas = self.get_omega_array()
    original_times = self.get_time_array()

    # start our our n variable
    n = 1

    # loop through times
    for i, time in enumerate(original_times):

      # check that time = n2pi/omegad (or close to equal)
      if abs(time - n*2*np.pi/self.omegad) < self.dt/2:

        # if so, add to our poincare data
        poincare_thetas.append(original_thetas[i])
        poincare_omegas.append(original_omegas[i])
        n += 1


    # save everything to our member variables
    self.thetas = poincare_thetas
    self.omegas = poincare_omegas

    