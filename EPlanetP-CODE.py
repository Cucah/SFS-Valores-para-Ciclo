# -- EPP --
# by @cucah (Discord / GitHub)
# codigo limpo e diminuido, agora ta melhor de visualizar

from math import pi
from time import sleep as to
import os

def limpa():
    os.system("cls" if os.name == "nt" else "clear")
def pausa():
     to(2)
     input("Return menu (Enter)")

def menu():
  while True:
# MENU inicial porra, tu é burro?
          limpa()
          print("----- MENU -----\n\nCustom Heightmap(CH/1)\nCycle Texture(CT/2)\nParachute Height(PH/3)\nCurve Atmosphere(NOT FINISHED)\nExit(Ex/5)")
          start = input("\nselect:_").lower()

# -- IMAGE TO HEIGHTMAP --
          if start in ["ch", "1"]:
              limpa()
              raio_planet = float(input('Planet Radius (ex: 45000.0) '))
              result_height = pi * 2 * raio_planet
              print(f'result: {result_height:.1f}')
              pausa()
# informação de como fazer o calculo foi retirada do grupo oficial do Spaceflight Simulator dito por **4poll0**, agradenço o compartilhamento do calculo.

# -- CYCLE TEXTURE ERROR --
          elif start in ["ct", "2"]:
              limpa()
              raio_cycle = float(input("Planet Radius (ex: 86500.0) "))
              altura_start = float(input('StartHeight (ex: -2500.0) '))
# valores negativos e positivos

              adisub = raio_cycle + altura_start 
# 86500 +/- 1000 = 85500/87500 * 2pi = resultado
              result_cycle = adisub * 2 * pi
              print(f'result: {result_cycle:.1f}')
              pausa()

# se alterado, lembre de conferir se dá o mesmo resultado final. um valor fácil para lembrar é utilizar o raio da Moon (86500) e gravar o resultado emitido aqui e conferir na sua versão. c

# -- PARACHUTE DEPLOY HEIGHT -- u
          elif start in ["ph", "3"]:
              limpa()
              padrao = 2500
              altura_para = float(input('Parachute Height (ex: 2500.0 = result 1.0) '))
              result_para = altura_para / padrao
              print(f'result: {result_para:.1f}')
              pausa()

# o valor padrão é 2500, então 0.1 = 250, resultando em 1.1 = 2750. c

# -- ATMOSPHERE CURVE (REENTRY START HEIGHT) -- a
# ainda ta sendo feito, e testado essa parte sobre o curve. h
          elif start in ["ca", "4"]:
              limpa()
              print('get out')
              pausa()


          elif start in ["ex", "5"]:
                    limpa()
                    print("bye...")
                    print(":(")
                    break
                    

          else:
              print("incorrect option.")
menu()


# by @cucah (Discord / GitHub)