
import os
import discord
import csv
### Management Commands ##
#  ^Clear [GroupName]
#  ^AssignGroup Auto / [GroupName] [Group (CSV Only!)]
#  ^dq [IGN]
#  ^Fight [Start] [END [Winner] [Optional: ID]] 
#  ^groupstart [GROUP]
#  ^substitute [PLAYER OUT] [PLAYER IN]
#  ^nextmatch
#  ^matchhistory [FIGHT ID]
#  ^displaygroup [GROUP ID]
#  ^matchwhen [FIGHT ID]
#  ^displaymatches [GROUP ID]
#  ^addplayer [IGN] [GROUP ID]
#  ^setup [GROUP QUANTITY] [GROUP SIZE] [ASSIGN: AUTO/OFF]
###

# \Hugo_Portal_Source\plugin\discord_bot\data

## DATA STRUCTURE ##


GroupB = []
GroupA = []


fightsA = []
fightsB = [] 

##

#####################
#  Fights A Group   #
#####################




def updateAFight():
   

    with open('\Hugo_Portal_Source\plugin\discord_bot\data\FightA.csv',mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                i = 0
                while i != len(row):
                    i = i + 1
                    playerNum = row[int(len(row) - 1)]
                    IGN = row[0]
                    DISCT = row[1]
                    line_count += 1
                fightsA.insert(i,[IGN,DISCT,playerNum])
                
        print(f'Processed {line_count} lines.')
        rowsA=len(fightsA) #finding the max number of rows in the matrix, in this case 3
        columnsA=len(fightsA[0])

#####################
#  Fights B Group   #
#####################
def updateBFight():
    

    with open('\Hugo_Portal_Source\plugin\discord_bot\data\FightB.csv',mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                i = 0
                while i != len(row):
                    i = i + 1
                    playerNum = row[3]
                    IGN = row[0]
                    DISCT = row[1]
                
                    
                    line_count += 1
                fightsB.insert(i,[IGN,DISCT,playerNum])
                
        print(f'Processed {line_count} lines.')
        rowsB=len(fightsB) #finding the max number of rows in the matrix, in this case 3
        columnsB=len(fightsB[0])


#####################
#   Create Group    #
#####################

#####################
#    READ A Group   #
#####################
def UpdateA():
    
    with open('GroupA.csv',mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                i = 0
                while i != len(row):
                    i = i + 1
                    playerNum = row[3]
                    IGN = row[0]
                    DISCT = row[1]
                    TZONE = row[2]
                    WINS = row[4]
                    LOSSES = row[5]
                    TWINS = row[6]
                    TLOSSES = row[7]
                    LBPLACE = row[8]
                    GROUP = row[9]
                    
                    line_count += 1
                GroupA.insert(i,[IGN,DISCT,TZONE,playerNum,WINS,LOSSES,TLOSSES,TWINS,LBPLACE,GROUP])
                
        print(f'Processed {line_count} lines.')
        rowsGA=len(GroupA) #finding the max number of rows in the matrix, in this case 3
        columnsGA=len(GroupA[0])
        return rowsGA


#####################
#    READ B Group   #
#####################
def UpdateB(rowsGB):
    

    with open('\Hugo_Portal_Source\plugin\discord_bot\data\GroupB.csv',mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                i = 0
                while i != len(row):
                    i = i + 1
                    playerNum = row[3]
                    IGN = row[0]
                    DISCT = row[1]
                    TZONE = row[2]
                    WINS = row[4]
                    LOSSES = row[5]
                    TWINS = row[6]
                    TLOSSES = row[7]
                    LBPLACE = row[8]
                    GROUP = row[9]
                    
                    line_count += 1
                GroupB.insert(i,[IGN,DISCT,TZONE,playerNum,WINS,LOSSES,TLOSSES,TWINS,LBPLACE,GROUP])
                
        print(f'Processed {line_count} lines.')
        rowsGB=len(GroupB) #finding the max number of rows in the matrix, in this case 3
        columnsGB=len(GroupB[0])
        return rowsGB

async def dq(ctx, ign: discord.message):
    
    pass





### Groups ###
async def Auto(ctx):

    pass

async def AssignGroup(ctx,IGN=None,Group=None):
    if Group == "A":
        print(f"Manager@AssignGroup - [{IGN}] Added to Group [{Group}]!")
        ctx.send(f"Manager@AssignGroup - [{IGN}] Added to Group [{Group}]!")

        i = rowsGA + 1
        GroupA.append(i,[IGN,IGN,'NILL',i,0,0,0,0,i,Group])
        rowsGA = i

    if Group == "B":
        print(f"Manager@AssignGroup - [{IGN}] Added to Group [{Group}]!")
        ctx.send(f"Manager@AssignGroup - [{IGN}] Added to Group [{Group}]!")

        i = rowsGB + 1
        GroupB.append(i,[IGN,IGN,'NILL',i,0,0,0,0,i,Group])
        rowsGB = i
    pass



if __name__ == "__main__":
    UpdateA()
    UpdateB()
    updateAFight()
    updateBFight()