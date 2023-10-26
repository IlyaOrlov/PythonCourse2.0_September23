import pickle
from userfile import User


u = User("Ivan", "Ivanov")
# with open("1", "wb") as f:
#     f.write(pickle.dumps(u))

with open("2", "wb") as f:
    pickle.dump(u, f)
