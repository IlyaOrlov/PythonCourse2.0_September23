import pickle
from userfile import User


# with open("1", "rb") as f:
#     s = f.read()
#     u = pickle.loads(s)
#     print(u)
#     u.show()

with open("2", "rb") as f:
    u = pickle.load(f)
    print(u)
    u.show()
