from aocd import get_data
list = get_data(year=2022, day=2).split("\n")
rps_dict = {"A":"Rock","X":"Rock","B":"Paper","Y":"Paper","C":"Scissors","Z":"Scissors"}
beats_dict = {"Rock":"Scissors","Paper":"Rock","Scissors":"Paper"}
value_dict = {"Rock":1,"Paper":2,"Scissors":3}
total_score = 0

for round in list:
    opponent, your = round.split(" ")
    score = value_dict[rps_dict[your]]

    if(rps_dict[your] == rps_dict[opponent]):
        score += 3

    elif(beats_dict[rps_dict[your]] == rps_dict[opponent]):
        score += 6
    total_score += score

print(total_score)