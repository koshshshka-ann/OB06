# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
#
# Требования:
# - Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# - Игра должна быть реализована как консольное приложение.
#
# Классы:
#
# Класс Hero:
# Атрибуты:
# - Имя (name)
# - Здоровье (health), начальное значение 100
# - Сила удара (attack_power), начальное значение 20
# Методы:
# - attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# - is_alive(): возвращает True, если здоровье героя больше 0, иначе False
#
# Класс Game:
# Атрибуты:
# - Игрок (player), экземпляр класса Hero
# - Компьютер (computer), экземпляр класса Hero
# Методы:
# - start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.base_attack_power = 20  # Базовая сила атаки

    def attack(self, other):
        # Случайная сила атаки: от 15 до 25 (можно настроить диапазон)
        current_attack = random.randint(self.base_attack_power - 5, self.base_attack_power + 5)
        other.health -= current_attack
        print(f"{self.name} атакует {other.name} и наносит {current_attack} урона!")  # Выводим текущий урон

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра начинается!")
        print(f"{self.player.name} vs {self.computer.name}")
        print("Да начнётся битва!")

        current_turn = 0  # 0 - игрок, 1 - компьютер
        while self.player.is_alive() and self.computer.is_alive():
            print("\n" + "=" * 30)
            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}")
            print("=" * 30 + "\n")

            if current_turn == 0:
                input("Нажмите Enter для атаки...")
                self.player.attack(self.computer)
                current_turn = 1
            else:
                print("Компьютер атакует...")
                self.computer.attack(self.player)
                current_turn = 0

        self.declare_winner()

    def declare_winner(self):
        print("\n" + "=" * 30)
        if self.player.is_alive():
            print(f"{self.player.name} побеждает! Поздравляем!")
        else:
            print(f"{self.computer.name} побеждает. Попробуйте ещё раз!")
        print("=" * 30)


# Запуск игры
if __name__ == "__main__":
    name = input("Введите имя вашего героя: ")
    game = Game(name)
    game.start()
