import web, json, random, threading, serial, time
from math import *

tempdata = [0,0,0,0,0,0,0,0,0,0]

urls = ('/', 'index', '/main.json','main', '/acq.json', 'acq')

app = web.application(urls, globals(), True)
print globals()
render = web.template.render('templates/')

class main:
	def GET(self):
		a = [{ "x_axis": 10, "y_axis": 10, "height": 20, "width":20, "color" : "green", "label" : "one" },
{ "x_axis": 40, "y_axis": 40, "height": 20, "width":20, "color" : "purple", "label" : "two" },
{ "x_axis": 70, "y_axis": 70, "height": 20, "width":20, "color" : "red", "label" : "three" }]
		web.header('Content-Type', 'application/json')
		return json.dumps(a)

class acq:
	def GET(self):
		global tempdata
		web.header('Content-Type', 'application/json')
		return json.dumps(tempdata)	

class index:
	def GET(self):
		return render.index()

lock = threading.Lock()

def init():
	global ser
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	
def acquire():
	global ser, tempdata
	ser.write("a")
	temp = float(ser.readline())
	print temp
	print tempdata
	lock.acquire()
	tempdata.append(dict(temperature=temp))
	tempdata.pop(0)
	lock.release()

def acquire_daemon():
	while True:
		acquire()
		time.sleep(5)

if __name__ == "__main__":
	init()
	t = threading.Thread(target=acquire_daemon)
	##t.daemon = True
	t.start()
	app.run()
