# Using the following camera model:
#                                       x' = K_in * K_ex * X
# X: 3D world coordinates of the form [x, y, z, 1] (4x1)
# K_ex: extrinsic parameters of the camera using 3D rotation and translation (3x4)
# K_in: intrinsic parameters of the camera using focal length, resolution and principal point offset (3x3)
# x': estimated 2D pixel coordinates of the form [hx, hy, h] (3x1)

# Estimate the real world coordinates from the first image's pixel coordinates:
#                                    X = (K_ex_1)^-1 * (K_in)^-1 * x

# Using this estimate project the first image's pixel coordinates to the second image's pixel coordinates:
#                              x_2 = K_in * K_ex_2 * (K_ex_2)^-1 * (K_in)^-1 * x_1

from intrinsic import inMat
from extrinsic import exMat
import numpy as np
