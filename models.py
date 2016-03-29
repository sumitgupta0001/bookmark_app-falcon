import os
from mongoengine import *

final_mongo_host = "mongodb://admin:f2A57AI_dLqg@%s:%s/" % (os.environ['OPENSHIFT_MONGODB_DB_HOST'], os.environ['OPENSHIFT_MONGODB_DB_PORT'])
connect('falconapp', host=final_mongo_host)


class registration_db(Document):
    
    
    u_id=StringField(required=True)
    name_db=StringField(required=True)
    email_db=EmailField(required=True)
    create_password=StringField(required=True)

    
    

class Bookmark_db(Document):
    name=StringField(required=True)
    location=StringField(required=True)
    labels=StringField(required=True)
    notes=StringField(required=True)
    u_id2=StringField(required=True)
