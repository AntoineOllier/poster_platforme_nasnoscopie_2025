import numpy as np
import matplotlib.pyplot as plt

# Paramètres communs
sigma = 1
amplitude = 1.0

# Centres des deux gaussiennes (légèrement espacés)
mu1 = 1.5
mu2 = 8

# Axe des x assez large pour couvrir les deux
x = np.linspace(0, 10, 1000)

# Deux fonctions gaussiennes
y1 = amplitude * np.exp(-(x - mu1)**2 / (2 * sigma**2))
y2 = amplitude * np.exp(-(x - mu2)**2 / (2 * sigma**2))

# Tracé
plt.plot(x, y1, color='darkorange', label='Gaussienne 1')
plt.fill_between(x, y1, color='darkorange', alpha=0.2)

plt.plot(x, y2, color='darkorange', label='Gaussienne 2')
plt.fill_between(x, y2, color='darkorange', alpha=0.2)

# Esthétique
plt.title('Deux gaussiennes proches mais séparées')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.legend()
plt.savefig("1_2_gaussian.svg", bbox_inches='tight', transparent=True)
