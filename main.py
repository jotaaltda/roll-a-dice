import shutil, keyboard, random, os, time, dados
from colorama import init, Style, Back, Fore

init(autoreset=True)

# PEGA LARGURA TOTAL DA TELA
largura = shutil.get_terminal_size().columns

total = 0

def rolar(evento): 
     
  global total

  print('\033[H', end='')

  # GERA ANIMAÇÃO DO DADO "ROLANDO"
  for n in range(1, 6):
    print('\033[H', end='')
           
    print(dados.faces[random.randint(0, 5)].center(largura))
    print((Style.BRIGHT + 'PONTOS - ' + Fore.RED + f'{total}').center(largura))
    time.sleep(0.2)

  print('\033[H', end='')
 
  resultado = random.randint(0, 5)
      
  total += (resultado + 1)

  # IMPRIME RESULTADO FINAL DO DADO
  print(dados.faces[resultado].center(largura))

  print((Style.BRIGHT + 'PONTOS - ' + Fore.RED + f'{total}').center(largura))

keyboard.on_press_key('space', rolar)

while True:
  ... 