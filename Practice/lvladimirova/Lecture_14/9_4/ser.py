import pickle
from kod import create_instances

people = create_instances(5)
for instance in people:
    instance.print_name()

with open("human.data", "wb") as f:
    pickle.dump(people, f)
