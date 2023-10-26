import pickle

with open("human.data", "rb") as f:
    p = pickle.load(f)
    print(p)
