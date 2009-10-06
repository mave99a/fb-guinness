import datetime
import sys
from google.appengine.ext import db

class Invite(db.Model):
  sender = db.StringProperty(required=True)
  invitee = db.StringProperty(required=True)
  when = db.DateTimeProperty(auto_now_add=True)
