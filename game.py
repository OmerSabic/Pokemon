import map
import commands

layout = map.layout
coords = map.coords
spawn = [3,2]
coords.x = spawn[0]
coords.y = spawn[1]
covering_char = ' '

covering_char = layout[coords.y-1][coords.x-1]
layout[coords.y-1][coords.x-1] = 'P'

def writeMap():
  global layout

  layout = map.layout
  layout[coords.y-1][coords.x-1] = 'P'

  for i in layout:
    for j in i:
      print(j, end='')
    print()

writeMap()

while True:
  move = input('move ')

  if(move == 'w'):
    coords.y += 1
  elif(move == 'a'):
    coords.x -= 1
  elif(move == 's'):
    coords.y -= 1
  elif(move == 'd'):
    coords.x += 1
  
  commands.cs()
  writeMap()