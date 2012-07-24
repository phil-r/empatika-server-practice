__author__ = 'Phil'

from google.appengine.ext import db


class Topic(db.Model):
    name = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)


class Comment(db.Model):
    text = db.TextProperty()
    topic = db.ReferenceProperty(Topic)
    created_at = db.DateTimeProperty(auto_now_add=True)