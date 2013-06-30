import web

urls = ('/','main')

app = web.application(urls, globals())

class main:
	def GET(self):
		return 'Hello wereld!'

if __name__ == "__main__":
	app.run()
