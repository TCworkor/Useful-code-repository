def get_positive_integer(prompt):
    """
    Prompts the user for input and ensures it is a positive integer.
    prompt: The input prompt message.
    提示用户输入，并确保是正整数。
    prompt: 输入提示信息
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("请输入一个正整数。 (Please enter a positive integer.)")
        except ValueError:
            print("非法输入，请输入一个正整数。 (Invalid input, please enter a positive integer.)")

# 获取商人和仆人的人数 (Get the number of merchants and servants)
GUI = get_positive_integer("请输入商人和仆人的人数 (Enter the number of merchants and servants): ")

# 获取船的载荷数 (Get the boat's capacity)
ZAI = get_positive_integer("请输入船的载荷数 (Enter the boat's capacity): ")

a = []   # 初始岸的所有变化情况 (All possible states on the initial shore)
b = []   # 船的载荷人数的变化情况 (Changes in the number of people the boat can carry)
# 商  仆 (Merchants, Servants)
# (a,b)
# 只考虑初始的一岸 (Only considering one shore initially)
for s in range(GUI+1):
    for p in range(GUI+1):
        if s >= p and (GUI-s)>=(GUI-p) or (s == 0 or (GUI-s) == 0):
            a.append((s,p))
print("初始岸的所有情况：", a, "(All possible states on the initial shore:)")

for i in range(ZAI+1):
    for j in range(ZAI+1):
        if 0 < i+j <= ZAI:
            b.append((i,j))
print("运载人数的所有情况：", b, "(All possible carrying capacities of the boat:)")

def futzy(zx, yu, eye, o):
    #print(eye)
    if zx == 0 and yu == 0:
        return 1
    for m, n in b:
        if o == 1:
            o = 0
            if (zx+m, yu+n) in a and (zx+m, yu+n, o) not in eye:
                eye.append((zx+m, yu+n, o))
                if futzy(zx+m, yu+n, eye, o) == 1:
                    return 1
                else:
                    eye.pop()
            o = 1
        else:
            o = 1
            if (zx - m, yu - n) in a and (zx - m, yu - n, o) not in eye:
                eye.append((zx - m, yu - n, o))
                if futzy(zx - m, yu - n, eye, o) == 1:
                    return 1
                else:
                    eye.pop()
            o = 0

    return 0

eye = [(GUI, GUI, 0)]
end = futzy(GUI, GUI, eye, 0)
if end == 1:
    print("可以实现 (Can be achieved)")
    for x, y, z in eye:
        if z == 1:
            print("({},{}) ___________⛵ ({},{})".format(x, y, GUI-x, GUI-y))
        else:
            print("({},{}) ⛵___________ ({},{})".format(x, y, GUI-x, GUI-y))
else:
    print("不可以实现 (Cannot be achieved)")

