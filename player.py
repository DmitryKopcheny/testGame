from random import randint

class Player:

    def __init__(cls):
        cls.health = 100

    def is_alive(cls):
        if cls.health > 0:
            return True
        else:
            return False

    def set_enemy(cls, enemy): 	#Игрок и компьютер содержат ссылки друг
        cls.enemy = enemy      	#на друга, чтобы при нанесении урона
                               	#влиять на прямую на здоровье противника
    def furious_damage(cls,
                       from_limit = 10,
                       to_limit = 35
                       ):
        damage = randint(from_limit, to_limit)
        cls.enemy.health -= damage
        if cls.enemy.health < 0:
            cls.enemy.health = 0
        return damage

    def accurate_damage(cls,
                        from_limit = 18,
                        to_limit = 25
                        ):
        damage = randint(from_limit, to_limit)
        cls.enemy.health -= damage
        if cls.enemy.health < 0:
            cls.enemy.health = 0
        return damage

    def heal(
            cls,
            from_limit = 18,
            to_limit = 25
            ):
        healing = randint(from_limit, to_limit)
        cls.health += healing
        if cls.health > 100:
            cls.health = 100
        return healing

    def random_choise(cls,
                      furious_chance = 20, 	#Вероятности каждого
                      accurate_chance = 40,	#действия в сумме должны
                      heal_chance = 40     	#составлять не больше 100
                      ):
        choise = randint(0,100)
        chance = furious_chance
        if choise <= chance:
            return ('furious', cls.furious_damage())
        chance += accurate_chance                   
        if choise <= chance:
            return ('accurate', cls.accurate_damage())
        chance += heal_chance
        if choise <= chance:
            return ('heal', cls.heal())
        return ('pass', ':)')
        #Метод возвращает тип действия и количество нанесенного урона или
        #восстановленого здоровья
