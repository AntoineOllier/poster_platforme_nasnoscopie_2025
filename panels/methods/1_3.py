from matplotlib import pyplot as plt
import numpy as np

# Draw number form a gaussaian distribution in 2 dimensions

"""Draw n samples from a 2D Gaussian distribution with mean mu and covariance sigma."""
# Generate random samples
x = np.random.multivariate_normal(mean=[0, 0], cov=[[7500, 0], [0, 7500]], size=10000)

# Plot the samples
plt.figure()
plt.scatter(x[:, 0], x[:, 1], s=1)
plt.title("Samples from a 2D Gaussian distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("1_3_2d_gaussian_samples.pdf", bbox_inches='tight', dpi=300, transparent=True)

# Calculate the histogram and plot it
plt.figure()
plt.hist2d(x[:, 0], x[:, 1], bins=100, cmap='viridis')
plt.colorbar(label='Counts')
plt.title("2D Histogram of Samples from a 2D Gaussian distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("1_3_2d_gaussian_histogram.pdf", bbox_inches='tight', dpi=300, transparent=True)


# Plot a contour plot of the 2D Gaussian distribution

x1 = np.linspace(-300, 300, 100)
x2 = np.linspace(-300, 300, 100)
X1, X2 = np.meshgrid(x1, x2)
# Calculate the Gaussian distribution with mean [-40, 50] and covariance [[7500, 0], [0, 7500]]
mu = np.array([-10, 10])
sigma = np.array([[7400, 0], [0, 7300]])
def gaussian_2d(x1, x2, mu, sigma):
    d = np.dstack((x1, x2))
    diff = d - mu
    inv_sigma = np.linalg.inv(sigma)
    exponent = -0.5 * np.einsum('...i,ij,...j->...', diff, inv_sigma, diff)
    return (1 / (2 * np.pi * np.sqrt(np.linalg.det(sigma)))) * np.exp(exponent)
# Calculate the Gaussian distribution
Z = gaussian_2d(X1, X2, mu, sigma)
# Plot the contour plot
plt.figure()
plt.contourf(X1, X2, Z, levels=100, cmap='viridis')
plt.colorbar(label='Density')
plt.title("Contour plot of a 2D Gaussian distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#plt.savefig("1_3_2d_gaussian_contour.pdf", bbox_inches='tight', dpi=300, transparent=True)
plt.show()
