import player, enemy
import time
import termcolor
from os import system, name
import Inventory

c = termcolor.colored
turn = 1
enemy = enemy.Enemy
player = player.Player
default = player(100,100,40,50)
defaultEnemy = enemy(200,50,10,35)

inv = Inventory.Inventory(5,3)


magicCount = 0

Fire = ('Fire',70, 40)
Water = ('Water', 60, 30)
Wind = ('Wind',50 , 25)

def clear():
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For Linux/Mac
    else:
        _ = system('clear')


def showEnemy():
    clear()
    print(c("===================================================",'red'))
    print('=============These are Your Enemy Stats============')
    print(c("===================================================",'red'))
    print(f'{defaultEnemy.getEnemyHP()} Health Points')
    print(f'{defaultEnemy.getEnemyMP()} Magic Points')
    print(f'{defaultEnemy.getEnemyPower()} Power Points')
    print("===================================================")
    time.sleep(2)
    battle()


def start():
    print(f'Welcome to Test Command Line Game!')
    print(f'Are you a new player?      (Y/N)')
    newPlayer = input('-->')

    if newPlayer == 'y':
        clear()
        print(c("===================================================",'blue'))
        print('Congrats! You start the game with default settings.')
        print(c("===================================================",'blue'))
        print(f'{default.getPlayerHP()} Health Points')
        print(f'{default.getPlayerMP()} Magic Points')
        print(f'{default.getPlayerPower()} Power Points')
        print("===================================================")
        time.sleep(2)
        print('Are you ready to start?!')
        time.sleep(2)
        showEnemy()

    else:
        pass

def chooseMagic():
    clear()
    print(c('What kind of magic would you like to use?', 'red'))
    print(f'1. {Fire[0]}          Power - {Fire[1]}    MP -  {Fire[2]}')
    print(f'2. {Water[0]}          Power - {Water[1]}    MP - {Water[2]}')
    print(f'3. {Wind[0]}          Power - {Wind[1]}    MP - {Wind[2]}')
    magicChoise = input('-->')
    if magicChoise == "1":
        playerMagicAttack(Magic=Fire)
    elif magicChoise == "2":
        playerMagicAttack(Magic=Water)
    elif magicChoise == "3":
        playerMagicAttack(Magic=Wind)
    else:
        print("Try again")
        chooseMagic()

def playerMagicAttack(Magic):
    clear()
    enemyTakeDmg = defaultEnemy.getEnemyHP() - Magic[1]
    defaultEnemy.hp = enemyTakeDmg

    if enemyTakeDmg <= 0:
        default.mp -= Magic[2]
        defaultEnemy.hp = 0
        time.sleep(1)
        print('Enemy Died.')
        exit()
    else:
        default.mp -= Magic[2]
        time.sleep(1)
        print(c('=============================================================================','red'))
        print(f'You used {Magic[0]} magic and attacked with {Magic[1]}!       Mana cost - {Magic[2]}')
        print(c(f'Current mana - {default.getPlayerMP()}','cyan'))
        print(c('=============================================================================','red'))
        time.sleep(2)
        print(f'Enemy has {enemyTakeDmg} Health Points!\n')

        enemyAttack()
    pass



def playerAttack():
    dmg = default.getPlayerDMG()
    enemyTakeDmg = defaultEnemy.getEnemyHP() - dmg
    defaultEnemy.hp = enemyTakeDmg

    if enemyTakeDmg <= 0:
        defaultEnemy.hp = 0
        time.sleep(1)
        print(c('\n\n\n\n\n\n=============================================================================', 'red'))
        print('Enemy Died.')
        exit()
    else:
        time.sleep(1)
        print(c('=============================================================================', 'red'))
        print(f'You attacked for {dmg}')
        print(f'Enemy has {enemyTakeDmg} Health Points!\n')
        print(c('=============================================================================', 'red'))
        enemyAttack()

def enemyAttack():
    dmg = defaultEnemy.getEnemyDMG()
    playerTakeDmg = default.getPlayerHP() - dmg
    default.hp = playerTakeDmg
    if playerTakeDmg <= 0:
        default.hp = 0
        time.sleep(2)
        print('You Died.')
        exit()
    else:
        time.sleep(1)
        print(f'Enemy attacked for {dmg}')
        print(f'You have {playerTakeDmg} Health Points!\n')
        time.sleep(3.5)

def playerInventory():
    print(c('Inventory list:','yellow'))
    print(f'1. HP Potions - {inv.potions}  left.               50 HP')
    print(f'2. Mana Potions - {inv.mana}  left.               50 MP')
    print(f'Which item would you like to use?         (Write "N" to quit)')
    invAns = input('-->')
    if invAns == '1':
        if inv.potions > 0:
            inv.potions -= 1
            if (default.hp + 50) >= default.maxhp:
                clear()
                default.hp = default.maxhp
                print(c('=============================================================================', 'red'))
                print(f'You have {inv.potions} HP Potions left.')
                print(f'\nNow you have {default.getPlayerHP()} Health points !')
                print(c('=============================================================================', 'red'))
            else:
                clear()
                print(c('=============================================================================', 'red'))
                print(f'You have {inv.potions} HP Potions left.')
                default.hp += 50
                print(f'\nNow you have {default.getPlayerHP()} Health points !')
                print(c('=============================================================================', 'red'))
        else:
            print('ERROR - You have no potions left')
            battleChoise()
    if invAns == '2' and inv.mana>0:
        if inv.mana >0:
            inv.mana -= 1
            if (default.mp + 50) >= default.maxmp:
                clear()
                default.mp = default.maxmp
                print(c('=============================================================================', 'cyan'))
                print(f'You have {inv.mana} Mana Potions left.')
                print(f'\nNow you have {default.getPlayerMP()} Mana points !')
                print(c('=============================================================================', 'cyan'))
            else:
                clear()
                print(c('=============================================================================', 'cyan'))
                print(f'You have {inv.mana} Mana Potions left.')
                default.mp += 50
                print(f'\nNow you have {default.getPlayerMP()} Mana points !')
                print(c('=============================================================================', 'cyan'))
        else:
            print('ERROR - You have no potions left')
            battleChoise()
    if invAns == 'N' or invAns == 'n':
        battleChoise()
    else:
        playerInventory()



def battleChoise():
    while True:
        global turn
        print(c(f"=======================Turn {turn}======================", 'green'))
        print(f'Choose carefully..')
        print(f'1. Attack')
        print(f'2. Magic Attack')
        print(f'3. Inventory')
        choise = input('--> ')

        if choise == '1':
            clear()
            playerAttack()
            turn += 1
        else:
            pass
        if choise == '2':
            chooseMagic()
        else:
            pass
        if choise == '3':
            playerInventory()
        else:
            pass


def battle():
    clear()
    print(c("===================================================", 'green'))
    print('================The Battle Begins...===============')
    battleChoise()


try:
    start()
except KeyboardInterrupt:
    pass