import matplotlib.pyplot as plt

outer_sizes = [40, 35, 25]
inner_sizes = [20, 20, 15, 20, 10, 15]

outer_labels = ['Cars', 'Bikes', 'Buses']
inner_labels = [
    'Audi', 'BMW',
    'Yamaha', 'Honda',
    'Volvo', 'Mercedes'
]

fig, ax = plt.subplots(figsize=(8,8))

ax.pie(
    outer_sizes,
    radius=1,
    labels=outer_labels,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

ax.pie(
    inner_sizes,
    radius=0.7,
    labels=inner_labels,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

plt.title("Nested Pie Chart")
plt.show()
