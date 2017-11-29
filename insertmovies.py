from databasecon  import connection
import numpy as np
import csv
''' Action
	* Adventure
	* Animation
	* Children's
	* Comedy
	* Crime
	* Documentary
	* Drama
	* Fantasy
	* Film-Noir
	* Horror
	* Musical
	* Mystery
	* Romance
	* Sci-Fi
	* Thriller
	* War
	* Western
'''
def markgenres(string,s):
	if 'Action' in string:
		s[2]=1
	if	'Adventure' in string:
		s[3]=1
	if 'Animation' in string:
		s[4]=1
	if	"Children's" in string:
		s[5]=1
	if 'Comedy' in string:
		s[6]=1
	if	'Crime' in string:
		s[7]=1
	if 'Documentary' in string:
		s[8]=1
	if	'Drama' in string:
		s[9]=1
	if 'Fantasy' in string:
		s[10]=1
	if	'Film-Noir' in string:
		s[11]=1
	if 'Horror' in string:
		s[12]=1
	if	'Musical' in string:
		s[13]=1
	if 'Mystery' in string:
		s[14]=1
	if	'Romance' in string:
		s[15]=1
	if 'Sci-Fi' in string:
		s[16]=1
	if	'Thriller' in string:
		s[17]=1
	if 'War' in string:
		s[18]=1
	if	'Western' in string:
		s[19]=1
		
	return s


def printnos(str):
	i=-2;s=[0]*20
	for j in range(3):
		i+=2
		#print()
		f=''
		while (i<len(str)) :
			if str[i]!=':':
				#print(str[i],end=" ");
				f+=str[i];i+=1;
			else:
				break
		if j==0:
			s[j]=int((f));print(int(f))		
		if j!=2:

			s[j]=f
		else:
			s=markgenres(f,s)	
	s[0]=int(s[0])	
	return s

conn,c=connection()


for line in open('movies.dat', 'r'):
    item = line.rstrip()

    c.execute('insert into movietable values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',printnos(item))
    #print(printnos(item));break

conn.commit()

	#

    #print(item,type(item))
    
     # strip off newline and any other trailing whitespace
conn.close()    