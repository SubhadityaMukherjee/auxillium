import json
d = {'domestic':['domestic','slapping','strangle','locking out','weapons','punching'],'financial':['theft','money','buying','financial'],'emotional':['emotional','yelling','insulting','stalking','suicide','online','refusing sex'],'social':['spying','in front of','monitor','social media','email','call','phone','socials',],'sexual':['rape','pain','forcing sex','porn','naked','strip','sex','private parts','sex jokes','touch']}
with open('problems.json','a+') as f:
    json.dump(d,f)
