urls = (
    "/", "welcome",
    "/hello", "hello"    )

class welcome:
    def GET(self):
        print "welcome blog"
class hello:
    def GET(self):
        print "hello blog"        