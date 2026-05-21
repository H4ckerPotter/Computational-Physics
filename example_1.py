import numpy as np
import matplotlib.pyplot as plt
length=1.0
g=9.81
dt=0.04
total_time=10

n_steps=int(total_time/dt)
t=np.zeros(n_steps)
theta=np.zeros(n_steps)
omega=np.zeros(n_steps)

t[0]=0.0
theta[0]=0.2
omega[0]=0.0

for i in range(n_steps-1):
    omega[i+1]=omega[i]-(g/length)*theta[i]*dt
    theta[i+1]=theta[i]+omega[i]*dt
    t[i+1]=t[i]+dt
    

plt.plot(t, theta, color="black")
plt.title('Simple Pendulum [Euler Method]\nLength=1 m, time step==0.04s')
plt.xlabel('time(s)')
plt.ylabel('theta(radians)')
plt.xlim(0,10)
plt.axhline(0,color='grey',linestyle='--')
plt.show()
