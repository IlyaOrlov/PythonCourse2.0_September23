import pickle
from kod import People

p = People

with open("human.data", "wb") as f:
    pickle.dump(p, f)
    