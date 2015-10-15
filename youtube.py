import urllib2

def findnum(stri,startpt,endpt):
	i=0
	min=1000000
	for i in range(0,9):
		if stri.find(str(i))<min:
			min=stri.find(str(i),startpt,endpt)
	return min

def mintosec(minstr):
	if(len(minstr)==5):
		return int(minstr[0:2])*60+int(minstr[3:4])
	elif(len(minstr)==8):
		return int(minstr[0:2])*3600+int(minstr[4:5])*60+minstr[6:7]

opener = urllib2.build_opener(
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.ProxyHandler({'https': '10.3.100.207:8080'}))
urllib2.install_opener(opener)
link = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id="
m=raw_input("Enter Video ID: ")
link=link+m
link=link+"&fields=items/snippet/description&key=AIzaSyAyVelJHPNdG9TLccqN2L_w9kKZsl0hm84"
a=urllib2.urlopen(link).read()
a=a[53:len(a)-16]
c=0
b=0
d=a.split('\\n')
t=[]
time=[]
for i in d:
	#print i
	t.append(i.find(':'))
for i in range(0,len(t)):
	if t[i]!=-1:
		b=d[i].find(':')
		if d[i][b-1].isdigit():
			if d[i][b+3]==':':
				#print d[i]
				if d[i][b-2].isdigit()==0:
					d[i]=d[i][:b-3]+'0'+d[i][b-1:]
				hh=int(d[i][b-1])
				mm=int(d[i][b+1])*10+int(d[i][b+2])
				ss=int(d[i][b+4])*10+int(d[i][b+5])
				time.append(hh*3600+mm*60+ss)

				
			else:
				#print d[i]
				if d[i][b-2].isdigit()==0:
					d[i]=d[i][:b-3]+'0'+d[i][b-1:]
				mm=int(d[i][b-2])*10+int(d[i][b-1])
				ss=int(d[i][b+1])*10+int(d[i][b+2])
				time.append(mm*60+ss)

fo = open("links.txt", "r+")
i=0
while i<len(time):
	link="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
	if i!=len(time)-1:
		link=link+m+"&start="+str(time[i])+"&end="+str(time[i+1])+" "
	else:
		link=link+m+"&start="+str(time[i])
	fo.write(link),
	i=i+1

print fo.read()

fo.close()
