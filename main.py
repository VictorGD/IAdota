import csv

with open("dota2.csv", 'r') as f:
    reader = csv.reader(f, delimiter=';')
    r = list(reader)

    # INITIALISATION
    rownum =0
    game_history = []
    for row in r :
        if rownum == 0 :
            heroes = row # Heroes Table
        elif rownum == 1 :
            game = row # The table to compare
        else :
            game_history.append(row) # The match history table
        rownum+=1
    del game[0]
    del heroes[0]

    stats_game = []

    # GAME SCORING
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

        if row[len(row)-2] >= score_max :
            score_max = row[len(row)-2]
            stats_game.append([row[0],row[len(row)-2],rownum])
        if row[len(row)-1] >= score_max :
            score_max = row[len(row)-1]
            stats_game.append([- int(row[0]),row[len(row)-1],rownum])

        rownum +=1

    # CLEANING STATS
    rownum =0
    for row in stats_game :
        if row[1]<score_max :
            del stats_game[rownum]
        rownum+=1

    #PREDICTION
    victories = 0
    defeats = 0
    for row in stats_game :
        if row[0]==1:
            victories+=1
        else :
            defeats+=1
    prediction = (victories-defeats)/(victories+defeats)*100

    #PRINT PREDICTION
    if prediction > 0 :
        print ('Victory '+str(prediction)+'%')
    elif prediction < 0 :
        print ('Defeat '+str(prediction+100)+'%')
    else :
        print ('Draw')

    # print ('############# HEROES ###########')
    # for row in heroes :
    #     print(row)
    # print ('\n################# GAME ###############')
    # for row in game :
    #     print(row)
    # print ('\n################# GAME_HISTORY ##################')
    # for row in game_history :
    #     print(row)

    # print (r[1][0])
    # for row in reader:
    #     print(row)
