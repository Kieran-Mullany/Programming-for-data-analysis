# Learning how to shade and to use and calculate probabilites using the program
# Script id from the printout I have 
# https://integratedmlai.com/normal-distribution-an-introduction-guide-to-pdf-and-cdf


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
fig, ax = plt.subplots()

#less_than_5 = norm.cdf(x=5, loc=3, scale=2)
# value is 0.8413447460685429 5i

x = np.arange(-6, 8, 0.001)
ax.plot(x, norm.pdf(x, loc=1, scale=2))
ax.set_title("Normal Distribution with mean 1, std_dv=2")
ax.set_xlabel('X-Values')
ax.set_ylabel('PDF(X)')

px = np.arange(0.2,5, 0.01)
ax.set_ylim(0, 0.25)
ax.fill_between(px, norm.pdf(px, loc=1, scale=2), alpha=0.5, color='c')

pro=norm(1,2).cdf(5) - norm(1,2).cdf(0.2)
ax.text(0.2, 0.02, round(pro, 2), fontsize=20)
plt.show()


# Use to show sigma 1, sigma 2 & sigma 3