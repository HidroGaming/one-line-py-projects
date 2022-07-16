#Circle made with trigonometry. I used MatPlotLib (https://matplotlib.org) and NumPy (https://numpy.org).

import numpy as np;import matplotlib.pyplot as ppl;pi = 3.141592653589793;a = np.linspace(0,2*pi,55);x = np.cos(a);y=np.sin(a);ppl.plot(x,y);ppl.axis("equal");ppl.show()
