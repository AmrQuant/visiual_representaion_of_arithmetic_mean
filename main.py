import numpy as np
import matplotlib.pyplot as plt

# القيم في المجموعة
values = [2, 8, 32]

# حساب المتوسط الهندسي
geometric_mean = np.prod(values) ** (1/len(values))

# طباعة المتوسط الهندسي
print("المتوسط الهندسي:", geometric_mean)

# تمثيل القيم والمتوسط الهندسي بصرياً
plt.figure(figsize=(10, 6))
plt.bar(['Value 1', 'Value 2', 'Value 3', 'Geometric Mean'], [values[0], values[1], values[2], geometric_mean], color=['blue', 'blue', 'blue', 'red'])
plt.title('Geometric Mean Calculation')
plt.ylabel('Values')
plt.show()
