import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(
        	"<html><head></head><body><p>Hello World</p></body></html>")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)