# %% Sphere
from vedo import Sphere, show

sphere = Sphere()  # יצירת כדור
show(sphere, "My First Sphere")  # הצגה בחלון אינטראקטיבי

# %% Cube, Cylinder
from vedo import Cube, Cylinder, show

cube = Cube() # קובייה אדומה
cube.color('purple')
cylinder = Cylinder() # גליל כחול
cylinder.color('blue')


show(cube, cylinder,  "Basic Shapes")

# %% Points
import numpy as np
from vedo import Points, show

points = np.random.rand(100, 3)  # 100 נקודות אקראיות בתלת-ממד
cloud = Points(points, r=5).c("green")  # ענן נקודות ירוק

show(cloud, "Point Cloud Example")

# %% Volume
from vedo import Volume, show

vol = Volume("path_to_your_volume.vti")  # To-Do
show(vol, "3D Volume")

# %% Cube rotate
from vedo import Cube, show

cube = Cube().pos(2, 2, 2).rotate(45).scale(1.5)  # קובייה עם הזזה, סיבוב והגדלה
show(cube, "Transformed Cube")

# %% Animation

