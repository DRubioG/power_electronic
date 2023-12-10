import numpy as np
import matplotlib.pyplot as plt
from transformations import *
from binary_fractions import Binary

x = np.linspace(0,np.pi*2, 460)    #70, 1000)

a = np.sin(x)*230


j=[]

# for i in a:
#     j.append(str(Binary(i)))


j = [str(Binary(i).lfill(10).rfill(8)).split('b')[1][:19] for i in a]

h = []

h = [float(Binary(i)) for i in j]

# b = np.sin(x- 2*(np.pi)/3)
# c = np.sin(x+ 2*(np.pi)/3)



plt.stem(x,a)
# plt.plot(x,b)
# plt.plot(x,c)

# alfa_beta = []


# for i in range(len(x)):
#     alfa_beta.append(abc_2_ab([a[i], b[i], c[i]]))

# plt.figure()
# plt.plot(x,alfa_beta)
plt.show()