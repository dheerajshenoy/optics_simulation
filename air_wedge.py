from diffractio import nm, um, mm, cm, degrees
from diffractio.scalar_sources_XY import Scalar_source_XY
import numpy as np

x0 = np.linspace(-1 * mm, 1 * mm, 100)
y0 = np.linspace(-1 * mm, 1 * mm, 100)
l1 = 589.6 * nm
l2 = 589.6 * nm

u1 = Scalar_source_XY(x=x0, y=y0, wavelength=l1, info='u1')
u2 = Scalar_source_XY(x=x0, y=y0, wavelength=l2, info='u2')

u1.gauss_beam(r0=(0, 0), w0=1 * mm, A=1, theta=0 * degrees, phi= 0 * degrees)
u2.plane_wave(A=1, z0=0, theta=90 * degrees, phi= 100 * degrees)

u_sum = u1 + u2
u_sum.draw(filename='air_wedge.png', has_colorbar='horizontal')
