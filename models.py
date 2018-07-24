from google.appengine.ext import ndb

class UserInfo(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    id = ndb.StringProperty(required=True)
    page_count = ndb.IntegerProperty(required=True)
