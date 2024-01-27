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
    return np.array(self.thetas)
  
  def get_omega_array(self):
    return np.array(self.omegas)
  
  def get_time_array(self):
    return np.array(self.times)
  
  def set_length(self, length):
    self.L = length

  def set_dt(self, new_dt):
    self.dt = new_dt

  def set_reset_theta(self, new_bool):
    self.reset_theta = new_bool




  def set_params(self, fDriving, fDamping, omegaDriving):
    self.fd = fDriving
    self.q = fDamping
    self.omegad = omegaDriving

  def periodic_driving_force(self, t):
    return self.fd * np.sin(self.omegad * t)
  
  def damping_force(self, omega):
    return - self.q * omega
  
  def gravity_force(self, theta):
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
    
    # domega/dt = acceleration aka all the forces
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
    which the derivs function needs
    
    returns updated [θ, ω] after rk2
    '''
    k1 = self.dt * self.rk2_derivs(th_om_array, self.times[-1])
    k2 = self.dt * self.rk2_derivs(th_om_array + 1/2 * k1, self.times[-1])
    
    updated = th_om_array + k2
    return updated


  def reset(self):
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

    while self.times[-1] < time:
      current_th = self.thetas[-1]
      current_om = self.omegas[-1]

      updated_array = self.runge_kutta2([current_th, current_om])

      theta = updated_array[0]
      omega = updated_array[1]

      # keep theta between -pi and pi if desired
      if self.reset_theta:
        if theta > np.pi:
          theta -= 2*np.pi
        if theta < -np.pi:
          theta += 2*np.pi

      self.thetas.append(theta)
      self.omegas.append(omega)

      self.times.append(self.times[-1] + self.dt)