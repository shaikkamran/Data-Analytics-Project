from getupdatedtables1 import returnupdatedtables
from operator import itemgetter
import csv
dctionary=returnupdatedtables()
liststr=[]
for i in dctionary.keys():
	liststr.append(i)
dictlist=[]
for i in range(21):
	for j in range(3):
		for k in range(1):
			
			dictlist.append([i,dctionary[liststr[0]][i][j][k],(dctionary[liststr[0]][i][j][k+1],'Action'),(dctionary[liststr[1]][i][j][k+1],'Romance'),(dctionary[liststr[2]][i][j][k+1],'Horror'),(dctionary[liststr[3]][i][j][k+1],'Thriller'),(dctionary[liststr[4]][i][j][k+1],'Western')] )
			

for i in range(63):
	dictlist[i][2:]=sorted(dictlist[i][2:],key=itemgetter(0),reverse=True)

def markoccupation(dictlist):
        
    for i in range(63):
        if dictlist[i][0]==0:
                dictlist[i][0]='others'
        elif dictlist[i][0]==1:
                dictlist[i][0]='academic/educator'
                
        elif dictlist[i][0]==2:
                dictlist[i][0]='artist'
                
        elif dictlist[i][0]==3:
                dictlist[i][0]='clerical/admin'
                
        elif dictlist[i][0]==4:
                dictlist[i][0]='college/grad student'
                
        elif dictlist[i][0]==5:
                dictlist[i][0]='customer service'
                
        elif dictlist[i][0]==6:
                dictlist[i][0]='doctor/health care'
                
        elif dictlist[i][0]==7:
                dictlist[i][0]='executive/managerial'
                
        elif dictlist[i][0]==8:
                dictlist[i][0]='farmer'
                
        elif dictlist[i][0]==9:
                dictlist[i][0]='homemaker'
                
        elif dictlist[i][0]==10:
                dictlist[i][0]=' "K-12 student'
        elif dictlist[i][0]==11:
                dictlist[i][0]='lawer'

                
        elif dictlist[i][0]==12:
                dictlist[i][0]='programmer'
                
        elif dictlist[i][0]==13:
                dictlist[i][0]='retired'
                
        elif dictlist[i][0]==14:
                dictlist[i][0]='sales/marketting'
        elif dictlist[i][0]==15:
                dictlist[i][0]='scientist'
                
        elif dictlist[i][0]==16:
                dictlist[i][0]='self-employed'
                
        elif dictlist[i][0]==17:
                dictlist[i][0]='technician/engineer'
        elif dictlist[i][0]==18:
                dictlist[i][0]='tradesman/craftsman'
                
        elif dictlist[i][0]==19:
                dictlist[i][0]='unemployed'
                
        elif dictlist[i][0]==20:
                dictlist[i][0]='writer'
                
        if dictlist[i][1]==1:
        	dictlist[i][1]='18-35'
        elif dictlist[i][1]==2:
        	dictlist[i][1]='36-50'
        elif dictlist[i][1]==3:
        	dictlist[i][1]='50+'


               
            
            
    
    return dictlist

dictlist=markoccupation(dictlist)
print(dictlist[0])

def writetocsv():
	with open('thirdquery2.csv', 'w', newline='') as fp:
		a=csv.writer(fp, delimiter=',')
		a.writerow(('Occupation','Age','Rank1 and avg(rating)','Rank2 and avg(rating)','Rank3 and avg(rating)','Rank4 and avg(rating)','Rank5 and avg(rating)'))
		for i in range(63):
	    
		    a.writerow(dictlist[i])

writetocsv()


