import web

urls = (
    '/', 'index'
)

app = web.application(urls,globals())

render = web.template.render('templates/')

class index(object):
    def GET(self):
    	greeting = "Hello World"
        #return render.index(greeting = greeting)
        #return render.index(greeting = 'a')
        #return render.index(None)
        return render.foo(123)

if __name__ == "__main__":
    app.run()