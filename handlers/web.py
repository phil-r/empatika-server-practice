from database import Topic, Comment

__author__ = 'Phil'

import webapp2, jinja2, os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        topics = Topic.all()

        self.response.out.write(template.render({"topics": topics}))

    def post(self):
        name = self.request.get('name')
        if name:
            topic = Topic()
            topic.name = name
            topic.put()
            self.get()
        else:
            self.response.out.write('no name :(')


class TopicHandler(webapp2.RequestHandler):
    def get(self, topicid):
        template = jinja_environment.get_template('templates/topic.html')
        topic = Topic.get_by_id(int(topicid))
        if topic:
            comments = Comment.all().filter('topic',topic)
            self.response.out.write(template.render({"topic": topic,"comments":comments}))
        else:
            self.response.out.write("no topic")

    def post(self, topicid):
        topic = Topic.get_by_id(int(topicid))
        text = self.request.get('text')
        if topic and text:
            Comment(text=text,topic=topic).put()
            self.get()
        else:
            self.response.out.write('no text or invalid topic id :(')

