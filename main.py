import webapp2
from handlers.web import IndexHandler, TopicHandler


class HelloWorldHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')

app = webapp2.WSGIApplication([('/', IndexHandler),('/topic/(.*)',TopicHandler)],
    debug=True)

