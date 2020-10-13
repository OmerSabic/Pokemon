import random
import bad

pokemon = input("Input your pokemon's name: ")

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


print("\nfuck it, it's pikachu!\n")
pika = """`;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /____.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \
    
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
         (_,'"""


print(pika)

tbDelay = 0

health = 100
pp = 100
defense = 5

ehealth = 100
epp = 100
edefense = 5

enemyMissTurn = 0
missTurn = 0

attacks = ['Scatch', 'Sleep', 'Mana drain', 'Thunderbolt']

def message(msg, color):
  a = ''
  for i in range(len(msg)):
    a += ('-')
  
  print("""{2}
  |{0}|
  |{1}|
  |{0}|
  {3}""".format(a, msg, color, bcolors.ENDC))

def cs():
  print(chr(27) + '[2j')
  print('\033c')
  print('\x1bc')

  
def printStats():
  message('Health: ' + str(health) + '  Pp: ' + str(pp) + '  Defense: ' + str(defense), bcolors.OKGREEN)
  message('Enemy health: ' + str(ehealth) + '  Enemy pp: ' + str(epp) + '  Enemy defense: ' + str(edefense), bcolors.OKGREEN)
  

printStats()

def checkHealth():
  global ehealth
  global health

  if(ehealth <= 0):
    message('You win, faggot, good job.', bcolors.BOLD + bcolors.WARNING)
    exit()
  elif(health <= 0):
    message('Fkn dumbass, lost to a rolling dice.', bcolors.FAIL)
    exit()


def atk():
  global epp
  global ehealth
  global edefense
  global enemyMissTurn
  global missTurn
  global pp
  global tbDelay


  atks = attacks[0] + ' - ' + attacks[1] + ' - ' + attacks[2] + ' - ' + attacks[3]
  message(atks, bcolors.WARNING)
  atek = input('select attack 1/2/3/4 : ')
  
  try:
    int(atek)
  except:
    print(bcolors.FAIL + bad.threat + bcolors.ENDC)
    atk()

  attack = int(atek)

  try:
    attacks[attack -1]
  except:
    print('\n' + bad.threat)
    atk()

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
      drain = random.randint(1,20)
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
          if(random.randint(0,1) == 1):
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

  if(epp < 7):
    possible_moves.pop(2)
  if(epp < 10):
    possible_moves.pop(4)

  attack = random.choice(possible_moves)

  if(not enemyMissTurn):
    if(attack == 1):
      health -= round(10 / edefense, 0)
      message("The enemy used {0}, it did {1} damage!".format(attacks[0], round(10/edefense, 0)), bcolors.OKBLUE)
    elif(attack == 2):
      pp -= 5
      if(random.randint(1,4) == 4):
        missTurn = 1
        message("The enemy used {0}.".format(attacks[1]), bcolors.OKBLUE)
    elif(attack == 3):
      drain = random.randint(1,20)
      pp -= drain
      epp += drain
      message("The enemy used {0}, they drained {1} mana!".format(attacks[2], drain), bcolors.OKBLUE)
    elif(attack == 4):
        pp -= 10
        dmg = random.randint(1,3)
        health -= round(20*dmg / edefense,0)
        message("The enemy used {0}, they did {1} damage!".format(attacks[3], round(20*dmg/defense),0), bcolors.OKBLUE)
        if(random.randint(0,1) == 1):
          defense -= 1
  else:
    message("The enemies pokemon is confused, it did no damage.", bcolors.FAIL)
    enemyMissTurn = 0
  
  printStats()
  checkHealth()
  atk()

atk()