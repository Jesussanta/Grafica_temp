import matplotlib.pyplot as plt
datos = []
with open('data.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        datos.append(line.split(' '))

print(datos)
temp=[]
for i in range (len(datos)):
    temp.append(datos[i][2])    
print(temp)

fig, ax = plt.subplots()
ax.plot(temp, linewidth=2.0)
plt.show()

