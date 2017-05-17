import csv

with open("dota2.csv", 'r') as f:
    reader = csv.reader(f, delimiter=';')
    r = list(reader)

    rownum =0
    game_history = []
    for row in r :
        if rownum == 0 :
            h = row
            print('header')
        elif rownum == 1 :
            game = row
        else :
            game_history.append(row)
        rownum+=1

    print ('############# HEADER ###########')
    for row in h :
        print(row)
    print ('\n################# GAME ###############')
    for row in game :
        print(row)
    print ('\n################# GAME_HISTORY ##################')
    for row in game_history :
        print(row)

    # print (r[1][0])
    # for row in reader:
    #     print(row)
