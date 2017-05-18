import csv
while True : 
	inputType = input("Select your input type (csv or manual) : ")
	if (inputType == 'csv') :
		#GAME TO PREDICT
		game = []
		with open("dota2game.csv", 'r') as f:
		    reader = csv.reader(f, delimiter=';')
		    r = list(reader)
		    rownum = 0
		    for row in r :
		        if rownum ==1 :
		            for elem in row:
		                game.append(elem)
		        rownum+=1
		break
	elif (inputType == 'manual') : 
		temp = 0
		game = []
		while temp <= 112 :
			game.append("0")
			temp +=1
		i = 1
		print("----- RADIANT -----")
		while i <= 5:
			hero = input ("Hero n°" +str(i) +" : ")
			if (int(hero) >112 or int(hero) < 0):
				print ("Your hero doesn't exists !")
			elif (game[int(hero)] == "0") : 
				game[int(hero)] = "1"
				i+=1
			
			else :
				print ("Chose an another hero, this one has already been picked")
		i = 1
		print("----- Dire -----")
		while i <= 5:
			hero = input ("Hero n°" +str(i) +" : ")
			if (int(hero) >112 or int(hero) < 0):
				print ("Your hero doesn't exists !")
			elif (game[int(hero)] == "0") : 
				game[int(hero)] = "-1"
				i+=1
			else :
				print ("Chose an another hero, this one has already been picked")

		break

#HEROES LIST
heroes = []
with open("dota2heroes.csv", 'r') as f:
    reader = csv.reader(f)
    r = list(reader)
    for row in r :
        heroes.append(row[0])

# #GAME TO PREDICT
# game = []
# with open("dota2game.csv", 'r') as f:
#     reader = csv.reader(f, delimiter=';')
#     r = list(reader)
#     rownum = 0
#     for row in r :
#         if rownum ==1 :
#             for elem in row:
#                 game.append(elem)
#         rownum+=1

#MATCH HISTORY
game_history = []
with open("dota2.csv", 'r') as f:
    reader = csv.reader(f, delimiter=';')
    r = list(reader)
    for row in r :
        game_history.append(row)

# GAME SCORING
stats_game = []
score_max = 0
rownum = 0
for row in game_history :
    row.append(0)
    row.append(0)
    indice_hero = 0
    for hero in game :
        if hero != '0' :
            if row[indice_hero+1] == hero :
                row[len(row)-2]+=1
        indice_hero += 1
        indice_hero =0
    for hero in game :
        if hero != '0' :
            if row[indice_hero+1] == str(- int(hero)) :
                row[len(row)-1]+=1
        indice_hero += 1
    score_max = row[len(row)-2]
    stats_game.append([row[0],row[len(row)-2],rownum])
    score_max = row[len(row)-1]
    stats_game.append([- int(row[0]),row[len(row)-1],rownum])
#PREDICTION
victories = 0
defeats = 0
for row in stats_game :
    if row[0]==1:
        if row[1]==score_max:
            victories+=512
        if row[1]==score_max-1:
            victories+=256
        if row[1]==score_max-2:
            victories+=128
        if row[1]==score_max-3:
            victories+=64
        if row[1]==score_max-4:
            victories+=32
        if row[1]==score_max-5:
            victories+=16
        if row[1]==score_max-6:
            victories+=8
        if row[1]==score_max-7:
            victories+=4
        if row[1]==score_max-8:
            victories+=2
        if row[1]==score_max-9:
            victories+=1
    else :
        if row[1]==score_max:
            defeats+=512
        if row[1]==score_max-1:
            defeats+=256
        if row[1]==score_max-2:
            defeats+=128
        if row[1]==score_max-3:
            defeats+=64
        if row[1]==score_max-4:
            defeats+=32
        if row[1]==score_max-5:
            defeats+=16
        if row[1]==score_max-6:
            defeats+=8
        if row[1]==score_max-7:
            defeats+=4
        if row[1]==score_max-8:
            defeats+=2
        if row[1]==score_max-9:
            defeats+=1
prediction = (victories-defeats)/(victories+defeats)*100
#PRINT PREDICTION
radiant_team = []
dire_team = []
colnum = 0
for hero in game :
    if hero == '1' :
        radiant_team.append(heroes[colnum])
    if hero == '-1' :
        dire_team.append(heroes[colnum])
    colnum+=1
print('Radiant Team :')
for hero in radiant_team :
    print('  - '+str(hero))
print('Dire Team :')
for hero in dire_team :
    print('  - '+str(hero))
if prediction > 0 :
    print ('Dire Victory '+str(int(prediction*100)/100)+'%')
elif prediction < 0 :
    print ('Radiant Victory '+str(int(prediction*100)/100+100)+'%')
else :
    print ('Draw')


print (game)
