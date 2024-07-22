import matplotlib.pyplot as plt
import numpy as np

def quad_model(time):
  #hard variables
  a=0.1
  b=-2
  c=3

  temperature=a*time**2+b*time+c
  return temperature

def main():
  time_slot=np.linspace(0,20,50)
  temperature=quad_model(time_slot)

  plt.plot(time_slot,temperature,label="hardcoded")
  plt.xlabel("time")
  plt.ylabel("temperature")
  plt.legend()
  plt.title("Weather modeling with quadratic equation using hardcoded variables")
  plt.show()

if __name__=="__main__":
  main()

