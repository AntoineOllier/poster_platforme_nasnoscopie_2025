from matplotlib import pyplot as plt
import numpy as np

# Draw number form a gaussaian distribution in 2 dimensions

"""Draw n samples from a 2D Gaussian distribution with mean mu and covariance sigma."""
# Generate random samples
x = np.random.multivariate_normal(mean=[0, 0], cov=[[7500, 0], [0, 7500]], size=1000)

# Plot the samples and axes with the same size
plt.figure(figsize=(8, 6))
plt.plot(0,0, 'x', markersize=10, label='Mean')
plt.scatter(x[:, 0], x[:, 1], s=3)
plt.title("Samples from a 2D Gaussian distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')  # <- fixe l'échelle sans modifier les limites
plt.xlim(-300, 300)
plt.ylim(-300, 300)
plt.savefig("1_3_2d_gaussian_samples.svg", bbox_inches='tight', transparent=True)
# Calculate the histogram and plot it
plt.figure(figsize=(8, 6))
plt.plot(0,0, 'x', markersize=10, label='Mean')
plt.hist2d(x[:, 0], x[:, 1], bins=50, cmap='hot', rasterized=True)
plt.colorbar(label='Counts')
plt.title("2D Histogram of Samples from a 2D Gaussian distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')  # <- fixe l'échelle sans modifier les limites
plt.xlim(-300, 300)
plt.ylim(-300, 300)
plt.savefig("1_3_2d_gaussian_histogram.svg", bbox_inches='tight', transparent=True)


# Plot a contour plot of the 2D Gaussian distribution
x1 = np.linspace(-300, 300, 1000)
x2 = np.linspace(-300, 300, 1000)
X1, X2 = np.meshgrid(x1, x2)
# Calculate the Gaussian distribution with mean [-40, 50] and covariance [[7500, 0], [0, 7500]]
def gaussian_2d(x1, x2, mu, sigma):
    """Calculate the 2D Gaussian distribution."""
    d = np.dstack((x1, x2))
    d = d - mu
    Z = np.exp(-0.5 * np.einsum('...i,ij,...j->...', d, np.linalg.inv(sigma), d))
    return Z / (2 * np.pi * np.sqrt(np.linalg.det(sigma)))
# Mean and covariance matrix
mu = np.array([-40, 50])
sigma = np.array([[7500, 0], [0, 7500]])
# Calculate the Gaussian distribution
Z = gaussian_2d(X1, X2, mu, sigma)
# Plot the contour plot
plt.figure(figsize=(8, 6))
plt.imshow(Z, extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin='lower', cmap='viridis', aspect='auto')
plt.plot(mu[0], mu[1], 'o', markersize=10, label='Mean')
plt.colorbar(label='Density')
plt.title("Contour plot of a 2D Gaussian distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("1_3_2d_gaussian_contour.svg", bbox_inches='tight', transparent=True)
plt.show()
