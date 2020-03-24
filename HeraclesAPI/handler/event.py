from flask import jsonify
#TODO: Check if error messages need to use JSONIFY

from .dao.user import UserDAO
from .dao.event import EventDAO

class EventHandler:
    #FOR GET
    def getAllEvents(self):       
        dao = EventDAO()
        events_list = dao.get_events()

        for event in events_list:
            if events_list[event]['metadata']['INVALID']:
                events_list[event]['metadata']=None
            if events_list[event]['content']['INVALID']:
                events_list[event]['content']=None
        return jsonify(events_list)
    
    def getEventByID(self, event_id):
        dao = EventDAO()
        event = dao.get_event_by_id(event_id)
        if not event:
            return jsonify(Error="Event Not Found"),404
        else:
            if event['metadata']['INVALID']:
                event['metadata']=None
            if event['content']['INVALID']:
                event['content']=None
            return jsonify(event) 
   
    #POST 
    def insertEvent(self, form):
        if (len(form['metadata']) < 6) or (len(form['content']) < 6):
            return jsonify(Error="Malformed post request"), 400
        else:
            # TODO: remove unnecesary ones from validation
            author_name = form['metadata']['author']
            date = form['metadata']['date']
            meta_image_url = form['metadata']['image_url'] 
            last_update = form['metadata']['last_update']
            summary = form['metadata']['summary']
            title = form['metadata']['title']
            post_image_url = form['content']['image-url']
            text = form['content']['text']
    
            #what fields are obligatory? For now Author and Text and Date
            if author_name and text and date:
                dao_u = UserDAO()
                #vaidate existing user
                if not dao_u.get_user(author_name):
                    return jsonify(Error="Author User Not Found"),404
                dao = EventDAO()
                event_id = EventDAO().create_event(form)

                result = dao.get_event_by_id(event_id)
                return jsonify(result)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
    #UPDATE
    def updateEventContent(self, event_id, form):
        if len(form) < 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            #TODO: Remove unnecesary ones from validation
            author_name = form['author']
            date = form['date']
            image_url = form['image_url'] 
            last_update = form['last_update']
            text = form['text']
            title = form['title']
        dao = EventDAO()
        if not dao.get_event_by_id(event_id):
            return jsonify(Error="Event not found."), 404
        dao_u = UserDAO()
        if not dao_u.get_user(author_name):
            return jsonify(Error="Author User not found."), 404
        else:
            #validate any others?
            if author_name and text and date:
                event_id = dao.update_event_content(event_id,form)
                result = dao.get_event_by_id
                return jsonify(result)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateEventMetadata(self, event_id, form):
        if len(form) < 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            #TODO: remove any unnecesary ones from validation
            author_name = form['author']
            date = form['date']
            image_url = form['image_url'] 
            last_update = form['last_update']
            summary = form['summary']
            title = form['title']
        dao = EventDAO()
        if not dao.get_event_by_id(event_id):
            return jsonify(Error="Event not found."), 404
        dao_u = UserDAO()
        if not dao_u.get_user(author_name):
            return jsonify(Error="Author User not found."), 404
        else:
            #validate any others?
            if author_name and date:
                event_id = dao.update_event_metadata(event_id,form)
                result = dao.get_event_by_id
                return jsonify(result)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    # REMOVE operations
    # TODO: Verify
    def removeEventMetadata(self, event_id):
        dao = EventDAO()
        event = dao.get_event_by_id(event_id)
        if not event:
            return jsonify(Error="Event Not Found"),404
        else:
            result = dao.fake_remove_event_metadata(self,event_id)
            return jsonify(result)
    
    def removeEventContent(self, event_id):
        dao = EventDAO()
        event = dao.get_event_by_id(event_id)
        if not event:
            return jsonify(Error="Event Not Found"),404
        else:
            result = dao.fake_remove_event_content(self,event_id)
            return jsonify(result)

    #Comment Operations
    def removeEventComments(self,event_id):
        dao = EventDAO()
        event = dao.get_event_by_id(event_id)
        if not event:
            return jsonify(Error="Event Not Found"),404
        else:
            result = dao.fake_remove_event_comments(self,event_id)
            return jsonify(result)

    def addComment(self,event_id,comment):
        dao = EventDAO()
        event = dao.get_event_by_id(event_id)
        dao_u = UserDAO()
        if not event:
            return jsonify(Error="Event Not Found"),404
        else:
            if not dao_u.get_user(comment['user']):
                return jsonify(Error="Author User Not Found"),404
            else:
                result =dao.add_comment(self, event_id,comment)
                return jsonify(result)

    def updateComment(self,event_id,comment_id,new_comment):
        dao = EventDAO()
        event = dao.get_event_by_id(event_id)
        #check existing event
        if not event:
            return jsonify(Error="Event Not Found"),404
        else:
            #check existing comment
            if not event['comments'][comment_id]:
                return jsonify(Error="Comment Not Found"),404
            else:
                #check valid user editing
                if event['comments'][comment_id]['user'] != new_comment['user']:
                    return jsonify(Error="Invalid User."), 400
                else:
                    result = dao.edit_comment(self,event_id,comment_id,new_comment)
                    return jsonify(result)
    
    def removeCommentbyId(self,event_id,comment_id):
        dao = EventDAO()
        event = dao.get_event_by_id(event_id)
        #check existing event
        if not event:
            return jsonify(Error="Event Not Found"),404
        else:
             #check existing comment
            if not event['comments'][comment_id]:
                return jsonify(Error="Comment Not Found"),404
            else:
                result = dao.fake_remove_comment_by_id(self,event_id,comment_id)
                return jsonify(result)

                