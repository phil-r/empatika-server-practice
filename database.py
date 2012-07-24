__author__ = 'Phil'

from google.appengine.ext import db


class Topic(db.Model):
    name = db.StringProperty()


class Comment(db.Model):
    text = db.TextProperty()
    topic = db.ReferenceProperty(Topic)