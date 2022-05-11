from matplotlib import pyplot as plt
from matplotlib import pylab 
import cv2
import imutils
xa=30
xb=170
ya=160
yb=300

img1 = cv2.imread('pool.jpeg', 1)
Redimg1 = cv2.resize(img1, (400, 300))
area = Redimg1[xa:xb,ya:yb]
gris = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY) #
cambio = cv2.cvtColor(gris,cv2.COLOR_GRAY2BGR)
Redimg1[xa:xb,ya:yb] = cambio
Redimg1 = cv2.cvtColor(Redimg1, cv2.COLOR_BGR2RGB)
cv2.circle(Redimg1,(230,110),80,(255,0,0),4)
fig = plt.figure(figsize=(10,7), constrained_layout=True)
plt.imshow(Redimg1)
plt.axis('off')
plt.title("Imagen 1")
plt.show()