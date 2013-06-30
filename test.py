import web, json

urls = ('/', 'index', '/main.json','main')

app = web.application(urls, globals())
render = web.template.render('templates/')

class main:
	def GET(self):
		a = [{ "x_axis": 10, "y_axis": 10, "height": 20, "width":20, "color" : "green", "label" : "one" },
{ "x_axis": 40, "y_axis": 40, "height": 20, "width":20, "color" : "purple", "label" : "two" },
{ "x_axis": 70, "y_axis": 70, "height": 20, "width":20, "color" : "red", "label" : "three" }]
		web.header('Content-Type', 'application/json')
		return json.dumps(a)

class index:
	def GET(self):
		return render.index()

if __name__ == "__main__":
	app.run()
