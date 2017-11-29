#fstquery.py
import csv
from databasecon import connection
conn,c=connection()
#top 10 most watched  movies in ascending order of their titles

c.execute("select movietable.movieid,title from movietable where movietable.movieid in(select movieid from ratings group by movieid order by count(*) desc limit 10) order by title asc");
top10MostWatchedmovies=[]
top10MostWatchedmovies=c.fetchall()
print(top10MostWatchedmovies)


import csv
def writetocsv():
	with open('fstquery.csv', 'w', newline='') as fp:
		a=csv.writer(fp, delimiter=',')
		a.writerow(('Movieid','MostWatchedMovie'))
		for i in range(len(top10MostWatchedmovies)):
	    
		    a.writerow(top10MostWatchedmovies[i])
		    
writetocsv()    
