# 2. Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
# умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.


class Car:
    def __init__(self, make, model, year, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def acceleration(self, speed_acceleration=5):
        return self.speed + speed_acceleration

    def stop(self, speed_stop=0):
        return self.speed * speed_stop

    def breaking(self, speed_breaking=5):
        return self.speed - speed_breaking

