class Vehicle :
    def __init__(self, name_car: str, max_speed: int, price: int):
        self.name_car = name_car
        self.max_speed = max_speed
        self.price = price

    def __gt__(self, other):
        return self.max_speed > other.max_speed

    def __str__(self):
        return f"{self.name_car}, {self.max_speed}"


def sortt(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


mers = Vehicle("mers", 220,30000)
bmw = Vehicle('BMW', 230,35000)
audi = Vehicle("AUDI", 200, 25000)

b = [mers,bmw,audi]
sortt(b)
for i in b:
    print(i)
