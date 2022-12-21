from aocd import get_data
from z3 import *
data = get_data(year=2022, day=21).split("\n")

vars = {}
s = Solver()

for line in data:
    split = line.split(" ")
    name = split[0][:-1]
    vars[name] = Int(name)
    s.add(vars[name] > 0)

for line in data:
    split = line.split(" ")
    name = split[0][:-1]

    if len(split) == 2 and name != "humn":
        s.add(vars[name] == int(split[1]))
        
    elif len(split) == 4:
        m1, op, m2 = split[1:4]
        
        if(name == "root"):
            s.add(vars[m1] == vars[m2])

        elif(name != "humn"):

            if(op == "+"):
                s.add(vars[name] == vars[m1] + vars[m2])

            elif(op == "-"):
                s.add(vars[name] == vars[m1] - vars[m2])

            elif(op == "*"):
                s.add(vars[name] == vars[m1] * vars[m2])

            elif(op == "/"):
                s.add(vars[name] * vars[m2] == vars[m1])

s.check()
answer = s.model()[vars['humn']]
print(answer)