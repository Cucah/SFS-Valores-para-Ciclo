# -- EPP --
# by @cucah (Discord / GitHub)

from math import pi
from time import sleep as to

def returno():
    to(4)
    print("return Menu? (Y/n)")
    rese = input("_").lower()
    if rese in ["y", "yes"]:
        print("\n" * 100)
        menu()
    else:
         quit()
         
# volta pro menu, é so isso.

def menu():
  print("----- MENU -----\n\nCustom Heightmap(CH/1)\nCycle Texture(CT/2)\nParachute Height(PH/3)\nCurve Atmosphere(NOT FINISHED)")
  start = input("\nselect:_").lower()
  
# menu inicial porra, tu é burro?
  
# -- IMAGE TO HEIGHTMAP --
  
  
  if start == "ch" or start == "1":
      print("\n" * 100)
      raioplanet = float(input('Planet Radius (ex: 45000.0) '))
      resultheight = pi * 2 * raioplanet
      print(f'result: {resultheight:.1f}')
      returno()
      
# informação de como fazer o calculo foi retirada do grupo oficial do Spaceflight Simulator dito por **4poll0**, agradenço o compartilhamento do calculo.
      
# -- CYCLE TEXTURE ERROR --

  elif start == "ct" or start == "2":
      print("\n" * 100)
      raiocycle = float(input("Planet Radius (ex: 86500.0) "))
      alturastart = float(input('StartHeight (ex: -2500.0) '))
      
      
# valores negativos
      if alturastart <= 0:
           menos = raiocycle -- alturastart # 86500 - 1000 = 85500 * 2pi = resultado
           resultcycle = menos * 2 * pi
           
           print(f'result: {resultcycle:.1f}')
           returno()
           
# valores possitivos                  
      elif alturastart > 0:
           menos = raiocycle + alturastart # 86500 + 1000 = 87500 * 2pi = resultado 
           resultcycle = menos * 2 * pi
           
           print(f'result: {resultcycle:.1f}')
           returno()

# se alterado, lembre de conferir se dá o mesmo resultado final. um valor fácil para lembrar é utilizar o raio da Moon (86500) e gravar o resultado emitido aqui e conferir na sua versão. c

# -- PARACHUTE DEPLOY HEIGHT -- u

  elif start == "ph" or start == "3":
      print("\n" * 100)
      esp = 2500
      alturapara = float(input('Parachute Height (ex: 2500.0 = 1.0) '))
      resultpara = alturapara / esp
      print(f'result: {resultpara:.1f}')
      returno()
      
# o valor padrão é 2500, então 0.1 = 250, resultando em 1.1 = 2750. c
    
# -- ATMOSPHERE CURVE (REENTRY START HEIGHT) -- a
      
  elif start == "ca" or start == "4":
      print("\n" * 100)
      print('get out')
      returno()
      
# ainda ta sendo feito, e testado essa parte sobre o curve. h
      
  else:
      print("incorrect option.")
      returno()
menu()

# by @cucah (Discord / GitHub)
