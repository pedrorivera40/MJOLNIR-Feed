from config.dbconfig import fb_config
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
            "posts-content").push(post['metadata'])
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
