import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10, 0.01)
y = 3.0 * x
noise = np.random.normal(0.0, 1.0, (len(x)))

plt.plot(x, y + noise, 'g.',label='Actual Data')
plt.plot(x,y, 'b-', label='Fitted Model')


plt.title("Average speed vs. Distance covered over time")
plt.xlabel("Average speed (km/h)")
plt.ylabel("Distance covered (km)")
plt.legend()

plt.show()