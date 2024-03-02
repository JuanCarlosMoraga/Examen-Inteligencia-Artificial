from sklearn.linear_model import LinearRegression
from os import system as system

#Datos de entrenamiento:
x_train = [[1],[2],[3],[4],[5],[6],[7],[8]] #kilometros en este caso

#Etiquetas
y_train = [1000,2000,3000,4000,5000,6000,7000,8000]# Equivalente a metros

#Crear y entrenar el model de regresion lineal
model = LinearRegression()
model.fit(x_train, y_train)

#Limpiar la consola
system("cls")
#pedir el valor en kilometros
km = int(input("Ingrese el valor en kilometros: "))

#Realizar predicciones
km_to_convert = [[km]]
predicted_m = model.predict(km_to_convert)

#Imprimir resultado
print(f"{km} Kilomtetros equivalen aproximadamente a {predicted_m[0]} Metros")