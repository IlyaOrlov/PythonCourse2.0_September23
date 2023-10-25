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
        return self._name

    def weight(self):
        return self._weight

    def __repr__(self):
        return f'<Duck name={self._name} weight={self._weight} color={self.color}>'

    def __lt__(self, other):
        return self._weight < other._weight

    def __gt__(self, other):
        return self._weight > other._weight

    def __eq__(self, other):
        return self._weight == other._weight

    def __ne__(self, other):
        return self._weight != other._weight

    def __add__(self, other):
        newduck = Duck(f"{self._name + other._name}", self._weight + other._weight)
        return newduck


d1 = Duck("первая", 22)
d2 = Duck("вторая", 32)
if d1 < d2:
    d3 = d1 + d2
    print(d3)