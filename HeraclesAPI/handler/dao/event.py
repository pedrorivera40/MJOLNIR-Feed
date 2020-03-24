from .config.dbconfig import fb_config
from firebase import Firebase

''' 
    Data Access Object implementation for the MJOLNIR-Feed prototype.
    This class includes a set of methods to perform CRUD operations over
    the Firebase RTDB instance regarding Events information.
    @author pedrorivera40
'''


class EventDAO:

    def __init__(self):
        self.rtdb = Firebase(fb_config).database()

    # Retrieve events metadata to display in the Feed view.
    def get_events(self):
        return self.rtdb.child("v1").child("posts").child("posts-metadata").get().val()

    # Retrieve event content given its event_id.
    def get_event_by_id(self, event_id):
        return self.rtdb.child("v1").child("posts").child("posts-content").child(event_id).get().val()

    # Create new event given its content and metadata into a single dictionary.
    def create_event(self, post):
        event_info = self.rtdb.child("v1").child("posts").child(
            "posts-metadata").push(post['metadata'])
        return self.update_event_content(event_info['name'], post['content'])

    # Update metadata of an event given its event_id.
    def update_event_metadata(self, event_id, new_metadata):
        return self.rtdb.child("v1").child("posts").child("posts-metadata").child(event_id).set(new_metadata)

    # Update content of an event given its event_id.
    def update_event_content(self, event_id, new_content):
        return self.rtdb.child("v1").child("posts").child("posts-content").child(event_id).set(new_content)

    # Hide metadata of an event given its event_id.
    def fake_remove_event_metadata(self, event_id):
        return self.rtdb.child("v1").child("posts").child("posts-metadata").child(event_id).child("INVALID").set("true")

    # Hide content of an event given its event_id.
    def fake_remove_event_content(self, event_id):
        return self.rtdb.child("v1").child("posts").child("posts-content").child(event_id).child("INVALID").set("true")

    # Hide comments of an event given its event_id.
    def fake_remove_event_comments(self, event_id):
        return self.rtdb.child("v1").child("posts").child("comments").child(event_id).child("INVALID").set("true")

    # Add a comment entry under an event.
    def add_comment(self, event_id, comment):
        return self.rtdb.child("v1").child("posts").child("comments").child(event_id).push(comment)

    # Edit a comment entry under an event.
    def edit_comment(self, event_id, comment_id, new_comment):
        return self.rtdb.child("v1").child("posts").child("comments").child(event_id).child(comment_id).set(new_comment)

    # Hide a comment entry under an event.
    def fake_remove_comment_by_id(self, event_id, comment_id):
        return self.rtdb.child("v1").child("posts").child("comments").child(event_id).child(comment_id).child("INVALID").set("true")


if __name__ == '__main__':
    # Initializa event dao.
    event_dao = EventDAO()

    # Just checking if it works by doing a simple query...
    print(event_dao.get_events())

'''
# Examples for the remaining methods.

# Get event content by id.
event_id = 'post-id-1'
print(event_dao.get_event_by_id(event_id))

# Create evemt.
new_event = {
    'metadata': {
        'author': 'user-2',
        'date': '00009995',
        'image-url': 'www.apicture.com',
        'last-update': '00009995',
        'summary': 'Compartiendo algunas frases celebres que todo el mundo deberia utilizar.',
        'title': 'Posting an event for testing!',
    },
    'content': {
        'author': 'user-2',
        'date': '00009995',
        'image-url': 'www.mysuperpicturewepa.com',
        'last-update': '00009995',
        'text': 'Frases celebres: La vida es complicada, es que no leen, eso me recuerda a mi GPA.',
        'title': 'Posting an event for testing!',
    },
}
print(event_dao.create_event(new_event))

# Update metadata and content of an event.
print(event_dao.update_event_metadata(event_id, new_event['metadata']))
print(event_dao.update_event_content(event_id, new_event['content']))

# Hide event content & metadata.
print(event_dao.fake_remove_event_content(event_id))
print(event_dao.fake_remove_event_metadata(event_id))

# Hide comments.
print(event_dao.fake_remove_event_comments(event_id))

# Comments section.
comment = {
    'user': 'user-1',
    'text': 'Again posting in my post! :P'
}

comment_info = event_dao.add_comment(event_id, comment)
comment['text'] = 'NVM I won\'t comment again...'
print(event_dao.edit_comment(event_id, comment_info['name'], comment))
print(event_dao.fake_remove_comment_by_id(event_id, comment_info['name']))

'''
