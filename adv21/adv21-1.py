from aocd import get_data
data = get_data(year=2022, day=21).split("\n")

d = {}

for line in data:
    split = line.split(" ")

    if len(split) == 2:
        d[split[0][:-1]] = [int(split[1])]

    elif len(split) == 4:
        m0 = split[0][:-1]
        m1, op, m2 = split[1:4]
        d[m0] = [m1, op, m2]

def evaluate(name, dicti):

    if(len(d[name]) == 1):
        return dicti[name][0]

    else:
        m1, op, m2 = dicti[name]

        if (op == "+"):
            return evaluate(m1, dicti) + evaluate(m2, dicti)

        elif (op == "-"):
            return evaluate(m1, dicti) - evaluate(m2, dicti)

        elif (op == "*"):
            return evaluate(m1, dicti) * evaluate(m2, dicti)

        elif (op == "/"):
            return evaluate(m1, dicti) // evaluate(m2, dicti)

print(evaluate("root", d))