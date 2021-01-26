
def minus(anonimys,dvadvavosem):
    return anonimys-dvadvavosem
def ymnozenie(vvv,mamont):
    return vvv*mamont
def delenie(bbb,mmm):
    return bbb/mmm
def plus(snus,horor):
    return snus+horor
def ostatok(snus,oed):
    return snus%oed
def polnoechislo(vvv,fff):
    return vvv//fff

d="yes"
while d=="yes":
    print("введите число")
    a = int(input())
    print("введите знак")
    c = input()
    print("введите число")
    b = int(input())
    print("ваш ответ:")

    if c == '-':
        print(minus(a, b))
    elif c == ':':
        print(delenie(a, b))
    elif c == '*':
        print(ymnozenie(a, b))
    elif c == '+':
        print(plus(a, b))
    elif c=='%':
        print(ostatok(a,b))
    elif c=='::':
        print(polnoechislo(a,b))
    print("если хотите продолжить напишите yes,если нет то no")
    d = input()

