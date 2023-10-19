class Duck:
    color = 'yellow'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def say():
        return 'Crack'

    @classmethod
    def colors(self):
        return self.color

    def name(self):
        return self.name

    def weight(self):
        return self.weight

    def __repr__(self):
        return f'<Duck name={self.name()} weight={self.weight()} color={self.color}>'

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __gt__(self, other):
        return self.weight() > other.weight()

    def __eq__(self, other):
        return self.weight() == other.weight()

    def __ne__(self, other):
        return self.weight() != other.weight()

    def __add__(self, other):
        newduck = Duck
        newduck.weight = self.weight() + other.weight()
        return newduck