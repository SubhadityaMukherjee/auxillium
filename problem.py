import json
import extractIssue
import random
from firebase import firebase
import time


# print(result)
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

def getissue():
	fireba = firebase.FirebaseApplication('https://auxilium-android.firebaseio.com/', None)
	result = fireba.get('/reports', None)
	print('entered')
	
	f = open('issues.json','w+')
	d = []
	for a in result:
		if(len(result[a]['crimeType'])==0):

			# d.append([result[a],extractIssue.extract(result[a]['phrase'])])
			# print(result[a]['phrase'])
			# print(a,extractIssue.extract(result[a]['phrase'])[0])
			result[a]['crimeType'] = extractIssue.extract(result[a]['phrase'])[0]
			# print(result)
			fireba.put('/reports',a,result[a])
	print('Done')

# getissue()
		

def connect_iss_to_ngo():
	isp = getissue()
	print(isp)
	issf = isp[-1]
	iss = issf[1][0]
	# print(iss) 
	ng = ngo()
	toconn = []
	# print(ng)

	for a in ng:
		l = ng[a]
		for b in ng[a]:
			if(iss==b):
				toconn.append([iss,a,l[0]])
	# print(toconn)
	ch = random.choice(toconn)
	result['crimeType']=ch[0]


# connect_iss_to_ngo()

while True:
	time.sleep(0.5)
	getissue()