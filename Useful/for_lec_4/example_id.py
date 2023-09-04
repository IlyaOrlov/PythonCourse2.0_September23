x = 50
print(f"{x=}, {id(x)=}")
y = 10
print(f"{y=}, {id(y)=}")
x = 100
print(f"{x=}, {id(x)=}")
y = x
print(f"{y=}, {id(y)=}")
x = 1
print(f"{x=}")  # 1
print(f"{y=}")  # 100
