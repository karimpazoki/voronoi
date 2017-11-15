import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

N = 10
Matrix = [(random.random()*10,random.uniform(1, 10))  for x in range(N)]
points = np.array(Matrix)

vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()

