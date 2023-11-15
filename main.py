def ingresar_puntuacion():
  while True:
      print('Por favor, introduzca una puntuación en una escala de 1 a 5')
      point = input()
      if point.isdecimal():
          point = int(point)
          if 1 <= point <= 5:
              print('Introduzca sus comentarios.')
              comment = input()
              post = f'punto: {point} comentario: {comment}'
              with open("data.txt", 'a') as file_pc:
                  file_pc.write(f'{post}\n')
              break
          else:
              print('Indíquelo en una escala de 1 a 5')
      else:
          print('Por favor ingrese su punto de calificacion en numeros.')

def mostrar_resultados():
  print('Resultados hasta la fecha.')
  with open("data.txt", "r") as read_file:
      print(read_file.read())

# Otras funciones según sea necesario

while True:
  print('Seleccione el proceso que desea aplicar')
  print('1: ingresar punto de calificacion y comentario.')
  print('2: Comprueba los resultados hasta ahora.')
  print('3: Terminar.')
  num = input()

  if num.isdecimal():
      num = int(num)

      if num == 1:
          ingresar_puntuacion()
      elif num == 2:
          mostrar_resultados()
      elif num == 3:
          print('Terminación.')
          break
      else:
          print('Introduzca de 1 a 3')
  else:
      print('Introduzca de 1 a 3')