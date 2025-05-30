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

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра 'Битва героев' начинается!")
        print(f"{self.player.name} (Здоровье: 100) vs {self.computer.name} (Здоровье: 100)")

        current_attacker = self.player  # Первым атакует игрок

        while self.player.is_alive() and self.computer.is_alive():
            print("\n" + "=" * 30)

            # Атака
            defender = self.computer if current_attacker == self.player else self.player
            current_attacker.attack(defender)

            # Вывод информации об атаке
            print(f"{current_attacker.name} атакует {defender.name}!")
            print(f"У {defender.name} осталось {defender.health} здоровья")

            # Смена хода
            current_attacker = self.computer if current_attacker == self.player else self.player

        # Определение победителя
        print("\n" + "=" * 30)
        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")
        print("=" * 30)


# Запуск игры
if __name__ == "__main__":
    name = input("Введите имя вашего героя: ")
    game = Game(name)
    game.start()
    