import urllib2
import gtk


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
link=link+"8h2M4eQygBs"
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
				print d[i]
				if d[i][b-2].isdigit()==0:
					d[i]=d[i][:b-3]+'0'+d[i][b-1:]
				hh=int(d[i][b-1])
				mm=int(d[i][b+1])*10+int(d[i][b+2])
				ss=int(d[i][b+4])*10+int(d[i][b+5])
				time.append(hh*3600+mm*60+ss)
					
			else:
				print d[i]
				if d[i][b-2].isdigit()==0:
					d[i]=d[i][:b-3]+'0'+d[i][b-1:]
				mm=int(d[i][b-2])*10+int(d[i][b-1])
				ss=int(d[i][b+1])*10+int(d[i][b+2])
				time.append(mm*60+ss)


class Buglump:
    
    def on_window1_destroy(self, object, data=None):
    	print "quit with cancel"
    	gtk.main_quit()

    def __init__(self):
    	self.gladefile = "type.glade"
    	self.builder = gtk.Builder()
    	self.builder.add_from_file(self.gladefile)
    	self.builder.connect_signals(self)
    	self.window = self.builder.get_object("window1")
    	self.window.show()

    def on_download_clicked(self, button, data=None):
    	self.entry1 = self.builder.get_object("entry1")
    	self.link1 = self.builder.get_object("link1")
    	self.link2 = self.builder.get_object("link2")
    	self.link3 = self.builder.get_object("link3")
    	self.link4 = self.builder.get_object("link4")
    	self.link5 = self.builder.get_object("link5")
    	self.link6 = self.builder.get_object("link6")
    	self.link7 = self.builder.get_object("link7")
    	self.link8 = self.builder.get_object("link8")
    	self.link9 = self.builder.get_object("link9")
    	self.link10 = self.builder.get_object("link10")
    	self.result1 = self.builder.get_object("result1")
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[0])
    	web=web+"&end="+str(time[1])
    	self.link1.set_text="agv"
    	self.abc="avfa"
    	self.result1.set_text=self.abc
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[1])
    	web=web+"&end="+str(time[2])
    	self.link2.set_uri=web
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[2])
    	web=web+"&end="+str(time[3])
    	self.link3.set_uri=web
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[3])
    	web=web+"&end="+str(time[4])
    	self.link4.set_uri=web
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[4])
    	web=web+"&end="+str(time[5])
    	self.link5.set_uri=web
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[5])
    	web=web+"&end="+str(time[6])
    	self.link6.set_uri=web
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[6])
    	web=web+"&end="+str(time[7])
    	self.link7.set_uri=web
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[7])
    	web=web+"&end="+str(time[8])
    	self.link8.set_uri=web
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[8])
    	web=web+"&end="+str(time[9])
    	self.link9.set_uri=web
    	web="http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v="
    	web=web+self.entry1.get_text()
    	web=web+"&start="+str(time[9])
    	web=web+"&end="+str(time[10])
    	self.link10.set_uri=web

if __name__ == "__main__":
	main = Buglump()
	gtk.main()




