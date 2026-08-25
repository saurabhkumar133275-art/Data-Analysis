from matplotlib import pyplot as plt

cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]

plt.figure(figsize=(8,6))
plt.pie(data, labels=cars)
plt.title("Car Distribution")
plt.show()
