from mongoengine import *

db = "hw_8"

connect(
    host="mongodb+srv://aaa1113341998825:2zNCrgJpCMgtZivG@cluster0.ylqzlor.mongodb.net/",
    db=db,
)


class Author(Document):
    fullname = StringField(max_length=150, required=True, unique=True)
    born_location = StringField()
    # born_date = DateTimeField()
    born_date = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    quote = StringField()
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
