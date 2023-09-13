def outer_fun2():
    def outer_fun():
        def inner_fun():
            print(f"Local var: {x}")

        inner_fun()

    outer_fun()


x = 50
outer_fun2()
print(f"Global var: {x}")

