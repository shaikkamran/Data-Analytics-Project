from databasecon import connection
from operator import itemgetter
conn,c=connection()

def putmissingvalues(dc):
	for i in dc.keys():
		if len(dc[i])<3:
			x=[1,2,3]
			for k in range(len(dc[i])):
				if dc[i][k][0] in x:
					x.remove(dc[i][k][0])
			for h in x:
				dc[i].append([h,0])
		dc[i]=sorted(dc[i],key=itemgetter(0))
				
	return dc			

def returnallnewtablesforthrdquery(views):
	
	#quer='select u.occupation,u.age,avg(r.stars)  from userswatchingmovie u,ratings r ,movietable m where m.movieid =r.movieid and r.userid=u.userid and m.{}=1 and u.age in (1,2,3) group by u.occupation,u.age'.{}format(views)
	c.execute('select u.occupation,u.age,avg(r.stars)  from userswatchingmovie u,ratings r ,movietable m where m.movieid =r.movieid and r.userid=u.userid and ({})=1 and u.age in (1,2,3) group by u.occupation,u.age'.format(views))
	x=c.fetchall()
	
	from collections import defaultdict
	dc=defaultdict(list)
	for i in range(len(x)):
		dc[x[i][0]].append([x[i][1],x[i][2]])

	return putmissingvalues(dc)
