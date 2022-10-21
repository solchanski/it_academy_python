teams = []
scores = []
winner = []

for i in range(0, 16):
   input_team = input('Enter the team: ')
   teams.append(input_team)

for i in range(0, 29):
   input_match = input('Enter the score ( : ): ')
   scores.append(input_match.split(':'))

x = teams[:len(teams)//2]
y = teams[len(teams)-1:len(teams)//2-1:-1]

for f, s in zip(x, y): # 1/8
    result_f = int(scores[0][0])+int(scores[1][0])
    result_s = int(scores[0][1])+int(scores[1][1])
    scores.pop(0)
    scores.pop(0)
    if result_f > result_s:
        winner.append(f)
        if s in teams:
            teams.remove(s)
    else:
        winner.append(s)
        if f in teams:
            teams.remove(f)

teams = winner
winner = []
x = teams[:len(teams)//2]
y = teams[len(teams)-1:len(teams)//2-1:-1]

for f, s in zip(x, y): # 1/4
    result_f = int(scores[0][0])+int(scores[1][0])
    result_s = int(scores[0][1])+int(scores[1][1])
    scores.pop(0)
    scores.pop(0)
    if result_f > result_s:
        winner.append(f)
        if s in teams:
            teams.remove(s)
    else:
        winner.append(s)
        if f in teams:
            teams.remove(f)

teams = winner
winner = []
x = teams[:len(teams)//2]
y = teams[len(teams)-1:len(teams)//2-1:-1]

for f, s in zip(x, y): # 1/2
    result_f = int(scores[0][0])+int(scores[1][0])
    result_s = int(scores[0][1])+int(scores[1][1])
    scores.pop(0)
    scores.pop(0)
    if result_f > result_s:
        winner.append(f)
        if s in teams:
            teams.remove(s)
    else:
        winner.append(s)
        if f in teams:
            teams.remove(f)

teams = winner
winner = []
x = teams[:len(teams)//2]
y = teams[len(teams)-1:len(teams)//2-1:-1]

for f, s in zip(x, y): # final
    result_f = int(scores[0][0])
    result_s = int(scores[0][1])
    if result_f > result_s:
        winner.append(f)
    else:
        winner.append(s)

print('Winner: ', winner)