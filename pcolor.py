import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(5, 3))
ax.set(xlim=(-3, 3), ylim=(-3, 3))
x = np.linspace(-3, 3, 91)
t = np.linspace(0, 25, 30)
y = np.linspace(-3, 3, 91)
X3, Y3, T3 = np.meshgrid(x, y, t)
sinT3 = np.sin(2*np.pi*T3 / T3.max(axis=2)[..., np.newaxis])
G = (X3**2 + Y3**2)*sinT3
cax = ax.pcolormesh(x, y, G[:-1, :-1, 0], vmin=-1, vmax=1, cmap='Blues')
fig.colorbar(cax)

def animate_pcolormesh(i):
    cax.set_array(G[:-1, :-1, i].flatten())

anim_pcolormesh = FuncAnimation(fig, animate_pcolormesh, frames=len(t), interval=100)
plt.show()
anim_pcolormesh.save('filename_pcolormesh.mp4')
