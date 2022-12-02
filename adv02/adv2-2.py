from aocd import get_data
list = get_data(year=2022, day=2).split("\n")
rps_dict = {"A":"Rock","B":"Paper","C":"Scissors"}
beats_dict = {"Rock":"Scissors","Paper":"Rock","Scissors":"Paper"}
loses_dict = {"Rock":"Paper","Paper":"Scissors","Scissors":"Rock"}
value_dict = {"Rock":1,"Paper":2,"Scissors":3}
total_score = 0

for round in list:
    opponent, outcome = round.split(" ")
    your = ""
    score = 0

    if(outcome == "X"):
        your = beats_dict[rps_dict[opponent]]

    elif(outcome == "Y"):
        your = rps_dict[opponent]
        score += 3

    elif(outcome == "Z"):
        your = loses_dict[rps_dict[opponent]]
        score += 6

    score += value_dict[your]
    total_score += score

print(total_score)