import matplotlib.pyplot as plt

left = [2, 4, 6, 8]
height = [20, 40, 60, 80]

tick = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, color=['blue', 'orange'], width=0.8)


plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo graph - Bar graph')

plt.show()
