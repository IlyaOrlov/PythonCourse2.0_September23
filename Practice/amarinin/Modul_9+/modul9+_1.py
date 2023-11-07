if __name__ == "__main__":
    lst = ['10', '5', 'a', '3', 'b']
    print([x * x for i in lst if i.isdecimal() and ((x := int(i)) % 5 == 0)])
