class Duck:
    color = 'yellow'

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    @staticmethod
    def say():
        return 'Crack'

    @classmethod
    def colors(cls):
        return cls.color

    def name(self):
        return self.name

    def weight(self):
        return self.weight

    def __repr__(self):
        return f'<Duck name={self.name} weight={self.weight} color={self.color}>'

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        newduck = Duck(f"{self.name + other.name}", 0)
        newduck.weight = self.weight + other.weight

        return newduck