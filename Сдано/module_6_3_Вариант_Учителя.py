

class Horse:
    """
    A class representing a horse.

    Attributes
    ----------
    x_distance : int, optional
        The current horizontal distance traveled by the horse. Default is 0.
    sound : str, optional
        The sound the horse makes. Default is 'Frrr'.

    Methods
    -------
    run(dx: int)
        Updates the horse's horizontal distance by adding dx.
    """

    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    """
    A class representing an eagle.

    Attributes
    ----------
    y_distance : int, optional
        The current vertical distance traveled by the eagle. Default is 0.
    sound : str, optional
        The sound the eagle makes. Default is 'I train, eat, sleep, and repeat'.

    Methods
    -------
    fly(dy: int)
        Updates the eagle's vertical distance by adding dy.
    """

    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    """
    A class representing a pegasus, which is a combination of a horse and an eagle.

    Methods
    -------
    __init__()
        Initializes a pegasus object. Calls the super class constructors of Horse and Eagle.

    move(dx: int, dy: int)
        Updates the pegasus's horizontal and vertical distances by adding dx and dy respectively.
        Calls the run and fly methods of the Horse and Eagle classes.

    get_pos() -> tuple
        Returns the current horizontal and vertical distances of the pegasus as a tuple.

    voice()
        Prints the sound the pegasus makes. Calls the voice method of the Horse class.
    """

    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())


p1.voice()





