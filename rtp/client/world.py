""" The world """

def generate_world(game):
    """
    Creates a world object

    World allows read-only access to game data.
    """

    class Car(object):

        @property
        def x(self):
            """ Returns car x position in game logical units """
            return game.car.position[0]

        @property
        def y(self):
            """ Returns car y position in game logical units """
            return game.car.position[1]

    car = Car()

    class World(object):

        @property
        def car(self):
            """ Return my car """
            return car

        def get_obstacle(self, pos):
            """
            Return the obstacle at position pos

            Arguments:
              pos: 2 tuple (x, y) using game logical units

            Accessing a position out of the world bounds will raise IndexError exception.
            """
            return game.track.get_obstacle(pos[0], pos[1])

    return World()
