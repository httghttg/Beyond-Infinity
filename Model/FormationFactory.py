from abc import ABCMeta


class Formation(metaclass=ABCMeta):

    def __init__(self):
        self.name = None
        self.numberOfShips = None
        # placement is 2d array where number of arrays is number of ships, index 0 is represented as start,
        # middle and end sections as 0, 1, 2, index 1 is x offset and index 2 is y offset
        self.placement = None


class VFormation(Formation):
    def __init__(self):
        super().__init__()
        self.name = "VFormation"
        self.numberOfShips = 3
        self.placement = [[1, 0, 0], [0, 0, -64], [2, 0, -64]]


class CaretFormation(Formation):
    def __init__(self):
        super().__init__()
        self.name = "CaretFormation"
        self.numberOfShips = 3
        self.placement = [[1, 0, -64], [0, 0, 0], [2, 0, 0]]


class DiagonalOneFormation(Formation):
    def __init__(self):
        super().__init__()
        self.name = "DiagonalOneFormation"
        self.numberOfShips = 2
        self.placement = [[0, 0, 0], [2, -32, -64]]


class DiagonalTwoFormation(Formation):
    def __init__(self):
        super().__init__()
        self.name = "DiagonalTwoFormation"
        self.numberOfShips = 2
        self.placement = [[0, 0, -64], [2, -32, 0]]


class SquareFormation(Formation):
    def __init__(self):
        super().__init__()
        self.name = "SquareFormation"
        self.numberOfShips = 4
        self.placement = [[0, 0, 0], [2, 0, 0], [0, 0, -128], [2, 0, -128]]


class RhombusFormation(Formation):
    def __init__(self):
        super().__init__()
        self.name = "RhombusFormation"
        self.numberOfShips = 4
        self.placement = [[1, 0, 0], [2, 0, -96], [0, 0, -96], [1, 0, -192]]


class FactoryFormation:

    @staticmethod
    def create_formation(enemy_type):
        try:
            if enemy_type == "VFormation":
                return VFormation()
            elif enemy_type == "CaretFormation":
                return CaretFormation()
            elif enemy_type == "DiagonalOneFormation":
                return DiagonalOneFormation()
            elif enemy_type == "DiagonalTwoFormation":
                return DiagonalTwoFormation()
            elif enemy_type == "SquareFormation":
                return SquareFormation()
            elif enemy_type == "RhombusFormation":
                return RhombusFormation()
            raise AssertionError("Formation not found.")
        except AssertionError as _e:
            print(_e)
