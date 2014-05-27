import web

db = web.database(dbn='postgres', user='postgres', pw='1234', db='postgres')


urls = (
	#'/(.*)','index'
	'/', 'index',
	'/add', 'add'
	)

render = web.template.render('templates/')

class index():
	def GET(self):
	#def GET(self,name):
		#name = 'Bob'
		#return render.index(name)
		#i = web.input(name = None)
		#return render.index(i.name)
		#return render.index(name)
		todos = db.select('todo')
		return render.index(todos)

class add:
	def POST(self):
		i = web.input()
		n = db.insert('todo', title=i.title)
		raise web.seeother('/')
		

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()