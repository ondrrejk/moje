import matplotlib.pyplot as plt
y = 0
x = 0
vy = 1
vx = 1
xpoints = []
ypoints = []
while y > 0:
    x += vx
    y += vy
    xpoints.append(x)
    ypoints.append(y)
    vy -= 0.05
plt.plot(x,y)
plt.show()