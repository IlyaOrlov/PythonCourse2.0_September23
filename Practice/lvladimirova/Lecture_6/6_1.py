def sort(s):
    for i in range(len(s)):
        min_i = i
        for x in range(i+1, len(s)):
            if s[x] < s[min_i]:
                min_i = x
        if min_i != i:
            s[i], s[min_i] = s[min_i], s[i]


if __name__ == "__main__":
    arr = [0, 3, 24, 2, 3, 7]
    sort(arr)
    print(arr)
