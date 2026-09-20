import shutil, keyboard, random, os, time, dados

largura = shutil.get_terminal_size().columns

def rolar(evento):
  print('\033[H\033[J', end='')

  for n in range(1, 6):
    print(dados.faces[random.randint(0, 5)])
    print('\033[H\033[J', end='')
    time.sleep(0.2)

  print(dados.faces[random.randint(0, 5)].center(largura))

keyboard.on_press_key('space', rolar)

while True:
  ...