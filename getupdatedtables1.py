
genres=['action','romance','horror','thriller','western']

from putvalueswhicharenotthere1 import returnallnewtablesforthrdquery

from collections  import defaultdict
def returnupdatedtables():

	dct=defaultdict(list)
	for i in genres:
		dct[i]=returnallnewtablesforthrdquery(i)
	return dct	
	
		