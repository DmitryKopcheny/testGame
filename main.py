from random import randint

from player import Player

#описания действий
ACTIONS = {             
    'furious': 'наносит противнику яростный урон: ',
    'accurate': 'наносит противнику точный урон: ',
    'heal': 'восстанавливает себе здоровье: ',
    'pass': 'пропускает ход '
    }
NAMES = [
    'Игрок',
    'Компьютер'
    ]

#вывод показателей здоровья и информации про действие
#совершенное за 1 ход
def print_turn(user, enemy, turn = None, choise = None, value = None):
    
    if turn != None and choise != None and value != None:
        print(NAMES[turn], ACTIONS[choise], value) 
    print('Здоровье %sа: ' % NAMES[0], user.health)
    print("Здоровье %sа: " % NAMES[1], enemy.health)

def main():
    
    user_player = Player()
    enemy_player = Player()
    user_player.set_enemy(enemy_player)
    enemy_player.set_enemy(user_player)
    print_turn(user_player, enemy_player)

    while user_player.is_alive() and enemy_player.is_alive():
        turn = randint(0,1)
        if turn:
            enemy_chances = (20,40,40)
            if enemy_player.health <35:
                enemy_chances = (20,20,60)		#увеличеный шанс на восстановление
                                          		#здоровья
            choise, value = enemy_player.random_choise(*enemy_chances)
        else:
            choise, value = user_player.random_choise() 
        print_turn(user_player, enemy_player, turn, choise, value)
        
    if user_player.is_alive():
        print('ПОБЕДА')
    else:
        print('ПОРАЖЕНИЕ')


if __name__ == "__main__":
    main();
