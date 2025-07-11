from math import sqrt 
print("Este programa calcula la distancia manhattan y euclidiana")

# pedimos las cordenadas una por una
x1 = int(input("ingresa la cordenada x del punto de origen: "))
y1 = int(input("ingresa la cordenada y del punto de origen: "))

x2 = int(input("ingresa la cordenada x del punto final: "))
y2 = int(input("ingresa la cordenada y del punto final: "))

# agregamos las cordenadas en tuplas
origen = (x1, y1)
final = (x2, y2) 

# calculamos distancias
distancia_x = abs(final[0] - origen[0])
distancia_y = abs(final[1] - origen[1])
manhattan = distancia_x + distancia_y
print("Distancia manhattan:", manhattan)

euclidiana = sqrt((final[0] - origen[0])**2 + (final[1] - origen[1])**2)
print("Distancia euclidiana:", euclidiana)
