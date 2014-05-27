urls = (
    "/", "welcome",
    "/hello", "hello"    )

class welcome:
    def GET(self):
        print "welcome wiki"
class hello:
    def GET(self):
        print "hello wiki"