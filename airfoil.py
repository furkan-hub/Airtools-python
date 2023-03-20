import matplotlib.pyplot as plt
import numpy as np

# Dosyayı okuyarak x ve y verilerini listelere kaydediyoruz
with open('NACA2412.txt', 'r') as file:
    data = file.readlines()

x = []
y = []

for line in data:
    line = line.split()
    x.append(float(line[0]))
    y.append(float(line[1]))

# Grafik boyutunu belirleme
plt.figure(figsize=(8,6))

# Profil çizimi
plt.plot(x, y, 'b', linewidth=2)

# Grafik özellikleri
plt.axis('equal')
plt.xlabel('x/c')
plt.ylabel('y/c')
plt.title('NACA 2412 Kanat Profili')
plt.grid(True)

plt.show()
