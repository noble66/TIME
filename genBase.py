# generates word_frequency dictionary
def word_freq(filepointer):
  d={}
	for line in filepointer:
		lsp=line.split('\t')
		print 'Processing..', lsp[0]
		if len(lsp)>2:
			tagsl=lsp[2]
			tg=tagsl.split(' ')
			for tag in tg:
				t=tag.strip('\"\'\n,')
				if t in d.keys():
					d[t]+=1
				else:
					d[t]=1
	with open('./word_freq.dict','w') as fw:
		pickle.dump(d,fw)
		print 'Save complete..'	
	return d

def remove_duplicates(dict):
	newd={}
	for d in dict.keys():
		newd[d]=list(set(dict[d]))
	return newd

def word_titles_freq(dict):
	s={}
	for d in dict.keys():
		s[d]=len(dict[d])
	return s

def dict_sort(d):
	s=sorted(d.iteritems(), key=itemgetter(1))
	return s
				
def inverted_index(filepointer):
	dtimes={}
	dtitles={}
        for line in filepointer:
                lsp=line.split('\t')
                print 'Processing..', lsp[0]
                if len(lsp)>2:
                        tagsl=lsp[2]
                        tg=tagsl.split(' ')
                        for tag in tg:
                                t=tag.strip('\"\'\n,')
                                if t in dtimes.keys():
                                        dtimes[t].append(lsp[0])
					dtitles[t].append(lsp[1])
                                else:
                                        dtimes[t]=[lsp[0]]
					dtitles[t]=[lsp[1]]
        with open('./inverted_index_times.dict','w') as fw:
                pickle.dump(dtimes,fw)
	with open('./inverted_index_titles.dict','w') as fw:
                pickle.dump(dtitles,fw)
                print 'Save complete..'
        return dtimes, dtitles

