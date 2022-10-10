import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
fig, ax = plt.subplots()

less_than_5 = norm.cdf(x=5, loc=3, scale=2)
# value is 0.8413447460685429 5i

x = np.arange(-4, 10, 0.001)
ax.plot(x, norm.pdf(x, loc=3, scale=2))
ax.set_title("Normal Distribution with \$mu=3, \$sigma=2")
ax.set_xlabel('X-Values')
ax.set_ylabel('PDF(x)')

px = np.arange(-4,5, 0.01)
ax.set_ylim(0, 0.25)
ax.fill_between(px, norm.pdf(px, loc=3, scale=2), alpha=0.5, color='r')

ax.text(-0.5, 0.02, round(less_than_5, 2), fontsize=20)
plt.show()


# Use to show sigma 1, sigma 2 & sigma 3