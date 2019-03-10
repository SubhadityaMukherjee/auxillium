import json
import extractIssue
import random

def probs():
	d = {'domestic':['domestic','slapping','strangle','locking out','weapons','punching'],'financial':['theft','money','buying','financial'],'emotional':['emotional','yelling','insulting','stalking','suicide','online','refusing sex'],'social':['spying','in front of','monitor','social media','email','call','phone','socials',],'sexual':['rape','pain','forcing sex','porn','naked','strip','sex','private parts','sex jokes','touch']}
	with open('problems.json','a+') as f:
		json.dump(d,f)

def ngo():
	f = open('NGOsData.txt','r').readlines()
	d = {}
	for a in f:
		p = a.split(',')
		p = [x.strip().lower() for x in p]
		d[p[0]] = p[1:]

	return(d)


def issues():
	# f = open('issues.csv','r').readlines()
	f2 = json.load(open('issues.json','r'))
	

	for a in f2:
		iss = extractIssue.extract(f2[a])
		# print(iss)
		if(len(iss)>0):
			return iss
			break

# issues()

def connect_iss_to_ngo():
	iss = issues()[0]
	ng = ngo()
	toconn = []
	# print(ng,iss)
	# print(ng)

	for a in ng:
		l = ng[a]
		for b in ng[a]:
			if(iss==b):
				toconn.append([a,l[0]])
	print(random.choice(toconn))
	return random.choice(toconn)


connect_iss_to_ngo()