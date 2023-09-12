def decor_fun(fun):
    def decor():
        print("===========")

    def decor_speed(*args, **kwargs):
        decor()
        fun(*args, **kwargs)
        decor()

    return decor_speed


@decor_fun
def av_speed(distance, time):
    av_sp = distance / time
    print(f"Средняя скорость автомобиля: {av_sp}")


av_speed(100, 20)

