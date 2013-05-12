import pickle
from collections import Counter
from operator import itemgetter
stopwords =['N.','or','You\'re','It','I.','My','V','Are','n','V.','if','is','it','we','...and','do','X','It)','Q.','B','Z','That','Isn\'t','Of','of','The','the','',' ','II','W.','&amp.','and','F.','B.','A.','in']

def wordYrFreq(word):
  dts=range(1923,2013)
	f=open('./word_yrs.dict','r')
	ftup=pickle.load(f)
	pstring=[]
	if word not in ftup:
		print 'Cannot find ', word
		return []
	else:
		fdict={}
		for (yr, freq) in ftup[word]:
			fdict[yr]=freq
		for d in dts:
			if d in fdict.keys():
				pstring.append(fdict[d])
			else:
				pstring.append(0)
	return pstring
