from config.dbconfig import fb_config
from firebase import Firebase


class EventDAO:

    def __init__(self):
        self.rtdb = Firebase(fb_config).database()
        self.posts = self.rtdb.child("v1").child("posts")

    def get_events(self):
        return self.posts.child("posts-metadata").get().val()

    def get_event_by_id(self, event_id):
        return self.posts.child("posts-content").child(event_id).get().val()

    def create_event_content(self, post_content):
        return self.posts.child("posts-content").push(post_content)

    def create_event_metadata(self, post_metadata):
        return self.posts.child("posts-metadata").push(post_metadata)

    def update_event_metadata(self, event_id, new_metadata):
        return self.posts.child("posts-metadata").child(event_id).set(new_metadata)

    def update_event_content(self, event_id, new_content):
        return self.posts.child("posts-content").child(event_id).set(new_content)

    # TODO -> Implement DELETE functions...
    def fake_remove_event(self, event_id):
        return self.posts.child(event_id).child("INVALID").set("true")


if __name__ == '__main__':
    # Initializa event dao.
    event_dao = EventDAO()

    # Just checking if it works by doing a simple query...
    print(event_dao.get_events())
