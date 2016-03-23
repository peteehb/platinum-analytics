import matplotlib.pyplot as plt

plt.axes()

circle = plt.Circle((0, 0), radius=50, alpha =.4, fc='r')
plt.gca().add_patch(circle)

rectangle = plt.Rectangle((-2,-2), 4, 4, fc='black')
plt.gca().add_patch(rectangle)

circle1 = plt.Circle((50, 50), radius=50, alpha=.4, fc='b')
plt.gca().add_patch(circle1)

rectangle1 = plt.Rectangle((48,48), 4, 4, fc='black')
plt.gca().add_patch(rectangle1)

circle2 = plt.Circle((50, -20), radius=20, alpha=.4, fc='g')
plt.gca().add_patch(circle2)

rectangle2 = plt.Rectangle((48, -22), 4, 4, fc='black')
plt.gca().add_patch(rectangle2)


plt.axis('scaled')
plt.show()
