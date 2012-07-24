from database import Topic

__author__ = 'Phil'

import webapp2, jinja2, os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        topics = Topic.all()


        self.response.out.write(template.render({"topics":topics}))
    def post(self):
        name = self.request.get('name')
        if name:
            topic = Topic()
            topic.name = name
            topic.put()
            self.get()
        else:
            self.response.out.write('no name :(')

