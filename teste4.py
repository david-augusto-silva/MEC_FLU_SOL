import matplotlib.pyplot as plt
from shapely.geometry import LineString
point_list = [(0,3), (1,0), (2,1), (3, 2), (5, 3),
              (7,4), (8,4), (10,3), (11,1), (12,1),
              (15,2), (17, 3), (18, 3), (20, 2)]

original = LineString(point_list)
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(20, 5)
ax.plot(*original.xy, color='red',
        label='input', marker='o')
ax.set_title('Original Line Segment', fontsize=20)
ax.legend()
plt.savefig('line.png', bbox_inches='tight', dpi=300)
plt.show()

