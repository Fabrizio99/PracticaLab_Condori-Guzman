#Autor: Condori Guzman, Fabrizio Raul
texto = input('Escriba el texto: ')
contador = 0
for letra in texto:
  if(letra != ' '):
    contador = contador + 1

print('Cantidad letras: ',contador)
