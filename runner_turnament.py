class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(*participants)# в исходном коде отсутствовала звёздочка

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name# в исходном коде не хватало '.name' - выводило весь объект
                    place += 1
                    self.participants.remove(participant)
                    break

        return finishers


r_1 = Runner('Усейн', 10)
r_2 = Runner('Андрей', 9)
r_3 = Runner('Ник', 3)

t_1 = Tournament(90, (r_1, r_3))
