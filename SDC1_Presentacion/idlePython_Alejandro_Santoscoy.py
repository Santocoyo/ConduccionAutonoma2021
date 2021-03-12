#importando matplotlib y pandas
import matplotlib.pyplot as plt
import pandas as pd

#Leyendo casos nuevos de COVID-19 en México (utlimas dos semanas)
data = pd.read_csv("datos/datos.csv")

#Vista previa de los primeras 5 lineas
print(data.head())

#Graficando las variables
data.plot(x = 'dia', y='casos', kind='line')
plt.show()
