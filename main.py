import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def grafiks1():
  data = pd.read_csv("Capital.csv")
  spending = np.array(data)

  xpoints = spending[:,0] # Vārdi
  ypoints = spending[:,1] # Ienakums

  plt.subplot(2, 3, 1)
  plt.plot(xpoints, ypoints, marker = 'X')
  plt.title("Money")

  xpoints = spending[:,3]#Total
  ypoints = spending[:,0]#Vārdi

  plt.subplot(2,3,2)
  plt.plot(xpoints, ypoints, color = 'r', ls = ':')
  plt.title("Total (Month)")

  

  
  x1 = spending[:,0]
  y1 = spending[:,1]
  x2 = spending[:,0]
  y2 = spending[:,2]
  
  plt.subplot(2, 3, 3)
  plt.plot(x1, y1, x2, y2)
  plt.title("Comparison")



  plt.suptitle("Something")
  plt.show()
  

grafiks1()

