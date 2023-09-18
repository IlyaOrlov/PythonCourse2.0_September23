def zam(t, dik1):
    n = len(t)
    k = t.count('дождь')
    for i in range(0, k):
        d = t.find('дождь')
        t2 = t[0:d] + dik1['дождь'] + t[d+5:n]
        t = t2
    return t


t = 'Вчера был дождь, и завтра будет дождь.'
dik = {'Вчера': 'Завтра', 'дождь': 'ветер'}
print(t)
t = zam(t, dik)
print(t)
