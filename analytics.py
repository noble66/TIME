import pickle
from collections import Counter
from operator import itemgetter
stopwords =['N.','or','You\'re','It','I.','My','V','Are','n','V.','if','is','it','we','...and','do','X','It)','Q.','B','Z','That','Isn\'t','Of','of','The','the','',' ','II','W.','&amp.','and','F.','B.','A.','in']

# generates frequency of word occurence in each yr from 1923-2013
# example input: 'Communism'
# example output: [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 2, 1, 1, 2, 1, 1, 1, 5, 3, 1, 0, 0, 0, 2, 1, 1, 3, 2, 3, 3, 4, 1, 4, 2, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 5, 0, 2, 4, 5, 1, 1, 3, 0, 4, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# dependencies: word_yrs.dict 
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
	
# return the yrs in which these words were detected 
# example input: ['Vitamins', 'Leak']
# example output: {'Leak': [2003], 'Vitamins': [1992]}
# dependency: inverted_index_times.dict
def findYrs(trkWords):
	doccur={}
	f=open('./inverted_index_times.dict','r')
	times=pickle.load(f)
	for w in trkWords:
		yrs=[]
		if w in times:
			print 'Processing: ',w,
			for issue in times[w]:
				if len(issue.split(','))>1:
					try:
						yr=int(issue.split(',')[1].strip(' '))
						yrs.append(yr)
					except:
						print '.. error'
		doccur[w]=yrs
	return doccur
	
