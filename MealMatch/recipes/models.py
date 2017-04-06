from mongoengine import *

# Create your models here.
class ingredients(Document):
    amount = ListField(required=True)
    type = ListField(required=True)


class recipe(DynamicDocument):
    _id = StringField(required=True)
    rating = ListField(required=True) # has to be 1 by default
    title = ListField(required=True)
    ingredients = EmbeddedDocumentField('ingredients')
    servings = ListField()
    time = ListField()
    directions = ListField(required=True)
    meta = {'strict' : False}
