import time, os, pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
# The file name you put in Sound() needs to exist in your project folder.
sound.play()
pygame.mixer.pause()

def pause():
  pygame.mixer.pause()

pause()

def play():
  os.system("clear")
  print("Playing some proper tunes!")
  pygame.mixer.unpause()
  while True:
    os.system("clear")
    stop = int(input("Press 2 to pause playback and go back to the menu "))
    if stop == 2:
      pygame.mixer.pause()
      return
    else:
      continue
  

while True:
  os.system("clear")
  print("MyPOD Music Player")
  time.sleep(2)
  print()
  print("Select to play a song: ")
  time.sleep(1)
  print("Press 1 to play")
  time.sleep(1)
  print("Press 2 to exit")
  time.sleep(1)
  print()
  print("Press anything else to see the menu again")
  press = int(input())
  if press == 1:
    play()
  elif press == 2:
    exit()
  else:
    os.system("clear")
    continue
