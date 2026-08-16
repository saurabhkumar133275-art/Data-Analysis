import numpy as np
import matplotlib.pyplot as plt

# Sample data
people = ('G1','G2','G3','G4','G5','G6','G7','G8')
segments = 4
data = np.array([
    [3.40022085, 7.70632498, 6.4097905, 10.51648577, 7.5330039, 7.1123587, 12.77792868, 3.44773477],
    [11.24811149, 5.03778215, 6.65808464, 12.32220677, 7.45964195, 6.79685302, 7.24578743, 3.69371847],
    [3.94253354, 4.74763549, 11.73529246, 4.6465543, 12.9952182, 4.63832778, 11.16849999, 8.56883433],
    [4.24409799, 12.71746612, 11.3772169, 9.00514257, 10.47084185, 10.97567589, 3.98287652, 8.80552122]
])

# Positions for groups
ind = np.arange(len(people))

# Initialize bottom values for stacking
bottom = np.zeros(len(people))

# Colors for each segment
colors = ['skyblue', 'lightgreen', 'salmon', 'violet']

# Plot stacked bars
for i in range(segments):
    plt.bar(ind, data[i], bottom=bottom, label=f'Segment {i+1}', color=colors[i])
    
    # Add labels to each section
    for j in range(len(people)):
        plt.text(ind[j], bottom[j] + data[i][j]/2, 
                 f'{data[i][j]:.1f}', ha='center', va='center', fontsize=8, color='black')
    
    # Update bottom for next stack
    bottom += data[i]

# Labels and title
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Labels')
plt.xticks(ind, people)
plt.legend()

plt.show()






















plt.show()
