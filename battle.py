import random
import bad
from commands import cs as cs
import pokemonList
import pokemonart
import moves

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[36m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

## picking pokemon ##
while True:
  print(bcolors.WARNING + bcolors.BOLD + "List of pokemon: " + bcolors.ENDC)
  print(bcolors.OKGREEN + '\n'.join(pokemonList.pokemons) + bcolors.ENDC)
  pokemon = input("Input your pokemon's name: ").lower()
  try:
    pk = pokemonList.pokemons[pokemon]
    break
  except:
    print(bcolors.FAIL + "That's not a pokemon you dumbass." + bcolors.ENDC)



print(bcolors.OKBLUE + bcolors.BOLD + bcolors.UNDERLINE + "\n" + str(pk) + ", i choose you!\n" + bcolors.ENDC)
pika = pokemonart.art[pokemon]


print(pika)

tbDelay = 0


health = pk['health']
pp = pk['pp']
defense = pk['baseDef']

ehealth = 100
epp = 100
edefense = 5

enemyMissTurn = 0
missTurn = 0

## variable to save the selected pokemon's moves ##
attacks = [pk['move1']['name'], pk['move2']['name'], 'PP drain', pk['move4']['name']]

### simple function to prompt the user to press enter once they're ready to proceed to the next part of the fight and clear the screen ###
def makeScreen():
  input('Press Enter to continue!')
  cs()
  print(pika)

### function to make a message with a cool frame ###
def message(msg, color):
  a = ''
  for i in range(len(msg)):
    a += ('-')
  
  print("""{2}
  |{0}|
  |{1}|
  |{0}|
  {3}""".format(a, msg, color, bcolors.ENDC))

### function to print the status of the player and the enemy ###
def printStats():
  message('Health: ' + str(health) + '  Pp: ' + str(pp) + '  Defense: ' + str(defense), bcolors.OKGREEN)
  message('Enemy health: ' + str(ehealth) + '  Enemy pp: ' + str(epp) + '  Enemy defense: ' + str(edefense), bcolors.OKGREEN)
  

printStats()

### function to check if the player or enemy have gone under 1hp to end the game ###
def checkHealth():
  global ehealth
  global health

  if(ehealth <= 0):
    message('You win, good job.', bcolors.BOLD + bcolors.WARNING)
    exit()
  elif(health <= 0):
    message("Fkn dumbass, lost to a rolling dice.", bcolors.FAIL)
    exit()


  ##### Main attack function for the player attacking #####
 
def atk():
  global epp
  global ehealth
  global edefense
  global enemyMissTurn
  global missTurn
  global pp
  global tbDelay

  #### Prompt for player attacks ####
  atks = attacks[0] + ' - ' + attacks[1] + ' - ' + attacks[2] + ' - ' + attacks[3]
  message(atks, bcolors.WARNING)
  atek = input('select attack 1/2/3/4 : ')
  
  #### check if the user input is valid ####
  try:
    int(atek)
  except:
    print(bcolors.FAIL + bad.threat + bcolors.ENDC)
    atk()
  # variable to save attack choice #
  attack = int(atek)

  try:
    attacks[attack -1]
  except:
    print('\n' + bcolors.FAIL + bad.threat + bcolors.ENDC)
    atk()

  #### executing attack ####
  if(not missTurn):
    if(attack == 1):
      ehealth -= round(10 / edefense, 0)
      message(pokemon + " used {0}, it did {1} damage!".format(attacks[0], round(10/edefense,0)), bcolors.OKBLUE)
    elif(attack == 2):
      if(pp >= 5):
        pp -= 5
        if(random.randint(1,4) == 4):
          enemyMissTurn = 1
          message(pokemon + " used {0}, the enemy was confused!".format(attacks[1]), bcolors.OKBLUE)
        else:
          message(pokemon + ' used {0}, the enemy is not confused!'.format(attacks[1]), bcolors.OKBLUE)
      else:
        message(pokemon + " doesn't have enough pp!", bcolors.OKBLUE)
    elif(attack == 3):
      drain = random.randint(5,20)
      epp -= drain
      pp += drain
      message(pokemon + " used {0}, you drained {1} mana!".format(attacks[2], drain), bcolors.OKBLUE)
    elif(attack == 4):
      if(pp >= 10):
        if(tbDelay == 0):
          tbDelay = 3
          pp -= 10
          dmg = random.randint(1,3)
          ehealth -= round(20*dmg / edefense, 0)
          message(pokemon + " used {0}, you did {1} damage!".format(attacks[3], round(20*dmg/edefense,0)), bcolors.OKBLUE)
          if(random.randint(0,1) == 1 and edefense > 1):
            edefense -= 1
        else:
          message('Thunderbolt has a cooldown of 3 rounds, you have {0} left!'.format(tbDelay), bcolors.FAIL)
          atk()
      else:
        message(pokemon + " doesn't have enough pp!", bcolors.FAIL)
        atk()
  else:
    message(pokemon + " was confused, it did no damage.", bcolors.FAIL)
    missTurn = 0

  if(tbDelay > 0):
    tbDelay -= 1
  checkHealth()
  eatk()

possible_moves = [1,2,3,4]
def eatk():
  global pp
  global health
  global defense
  global enemyMissTurn
  global missTurn
  global epp
  global possible_moves

  attack = random.randint(1,4)

  if(not enemyMissTurn):
    if(attack == 1):
      health -= round(10 / edefense, 0)
      message("The enemy used {0}, it did {1} damage!".format(attacks[0], round(10/edefense, 0)), bcolors.OKBLUE)
    elif(attack == 2):
      pp -= 5
      message("The enemy used {0}.".format(attacks[1]), bcolors.OKBLUE)
      if(random.randint(1,4) == 4):
        missTurn = 1
    elif(attack == 3):
      drain = random.randint(5,20)
      pp -= drain
      epp += drain
      message("The enemy used {0}, they drained {1} mana!".format(attacks[2], drain), bcolors.OKBLUE)
    elif(attack == 4):
        pp -= 10
        dmg = random.randint(1,3)
        health -= round(20*dmg / edefense,0)
        message("The enemy used {0}, they did {1} damage!".format(attacks[3], round(20*dmg/defense),0), bcolors.OKBLUE)
        if(random.randint(0,1) == 1 and defense > 1):
          defense -= 1
  else:
    message("The enemies pokemon is confused, it did no damage.", bcolors.FAIL)
    enemyMissTurn = 0
  

  
  makeScreen()
  checkHealth()
  printStats()
  atk()

atk()