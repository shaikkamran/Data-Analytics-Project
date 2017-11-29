from databasecon  import connection
import numpy as np
import csv

'''def typecast(col_list,arr,st):
	for i in col_list:
	
		for j in range (len(arr)):
			if st=='i':
				if arr[j][i]!='-' and arr[j][i]!='':

					arr[j][i]=int(arr[j][i])
				else:
					arr[j][i]=None
			elif st=='f':
				if arr[j][i]!='-' and arr[j][i]!='':

					arr[j][i]=float(arr[j][i])
				else:
					arr[j][i]=None	
				
			#print(arr[0][j])
	return arr
'''			
def printnos(str):
	i=-2;s=[]
	for j in range(4):
		i+=2
		#print()
		f=''
		while (i<len(str)) :
			if str[i]!=':':
				#print(str[i],end=" ");
				f+=str[i];i+=1;
			else:
				break
		#print(int(f))
		s.append(int(f))
	return s

conn,c=connection()


for line in open('ratings.dat', 'r'):
    item = line.rstrip()
    c.execute('insert into ratings values (?,?,?,?)',printnos(item))
    #print(printnos(item));break

conn.commit()

	#

    #print(item,type(item))
    
     # strip off newline and any other trailing whitespace
conn.close()    