N = int(input())


def fanc(s):
    if len(s) == N:
        print(s)
        return
    fanc(s + "a")
    fanc(s + "b")
    fanc(s + "c")


fanc("")
