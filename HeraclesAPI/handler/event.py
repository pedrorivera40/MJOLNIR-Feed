#from flask import jsonify

#Now we have:
#Login 
#Register
#Event
#Event/EventID
#Event/EventID/Comment
#Event/EventID/Comment/CommentID

# DELETE TESTING SOON
# Need to use this since otherwise returns surface level...
# https://ivan-site.com/2011/08/counting-leaves-with-python/ # Simple Method Recursive
# Probably not accurate! since we also have comments...and that growssss
def leafcounter(node):
    if isinstance(node, dict):
        return sum([leafcounter(node[n]) for n in node])
    else:
        return 1

#==========TESTING GENERAL DICT CODE===============
#leafcounter(tree) # returns 6
# x = dict(Error = "x",Kill="nope",something=345, dead="")
# y = dict(redx = x, nope = x)
# print(x)
# print("oook")
# print(y)
# print("TEST GROUND")
# #print(y['fiofe'])
# print(y['nope']['Kill'])
# print(y['nope']['dead'])
# if x['Kill']:
#     print("Yeah") 
# else:
#     print("Again No") #If None or empty string will return empty....
# print("Lenght of it is: ",len(x)) # len returns the number even if empty
# print("Length of Double is....",len(y))
# print(y)
# print("Leaves is: ",leafcounter(y))
#=======================================

# ====TEST FILTER METHOD =================================
# def getAllEvents2():
#     yt = dict(text = "blahblah", INVALID = True)
#     yf = dict(text = "blahblah", INVALID = False)
#     zt = dict(summary="nuecieuvnrtiv", INVALID=True)
#     zf = dict(summary="nuecieuvnrtiv", INVALID=False)
    
#     xtt = dict(metadata = yt, content = zt)
#     xtf = dict(metadata = yt, content = zf)
#     xff = dict(metadata = yf, content = zf)
#     xft = dict(metadata = yf, content = zt)
    
#     events_list = dict(e1 = xtt, e2 = xtf, e3 = xff, e4 = xft)
#     print("Original")
#     print(events_list)
#     for event in events_list:
#         if events_list[event]['metadata']['INVALID']:
#             events_list[event]['metadata']=None
#         if events_list[event]['content']['INVALID']:
#             events_list[event]['content']=None
#     print(events_list)
# #Call Test
# getAllEvents2() 
# ===================================

class EventHandler:
    #FOR GET
    def getAllEvents(self):
        #firebase returns dict? or is it JSON? Either way need to filter it...
        #need to check all of the returned events that are NOT hidden, so need to purge that JSON
        # for each node, check if invalid, if so change to None
       
        dao = EventsDAO()
        events_list = dao.get_events()
     
        #=====ORIGINAL CODE=======
        #Since Firebase returns JSON dont need this anymore
        # results_list = []
        # for row in events_list:
        #     result = Event().build_dict_from_row(row)
        #     result_list.append(result)
        # return jsonify(result_list)
        #=========================

        for event in events_list:
            if events_list[event]['metadata']['INVALID']:
                events_list[event]['metadata']=None
            if events_list[event]['content']['INVALID']:
                events_list[event]['content']=None
        return events_list
    
    def getEventByID(self, event_id):
        dao = EventsDAO()
        event = dao.get_event_by_id(event_id)
        if not event:
            #=====ORIGINAL CODE=======
            #return jsonify(Error = "Event Not Found"), 404
            #check, do we need to jsonify this?
            #==================
            return dict(Error="Event Not Found"),404
        else:
            if event['metadata']['INVALID']:
                event['metadata']=None
            if event['content']['INVALID']:
                event['content']=None
            return event 
            #event = Event().build_dict_from_row(row)
            #return jsonify(event)
   
    #POST 
    def insertEvent(self, form):
        #TODO:  verify what the appropiate len should be 
        # assuming all of form should be present, so will have len as all (6)
        # for now assuming 12 since its Metadat+Content, but if need/have comment will be longer...
        if leafcounter(form) < 12:
            #return jsonify(Error="Malformed post request"), 400
            return dict(Error="Malformed post request"), 400
        else:
            #QUESTIONS!
            #-are there two image ids
            #-how do we divide content/metadata here?
            #only reason to do this is to validate, otherwise we just pass the form...
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
                dao_u = UsersDAO()
                #vaidate existing user
                if not dao_u.get_user(author_name):
                    return dict(Error="Author User Not Found"),404
                dao = EventsDAO()
               
                # So here's the thing, just pass the form to the DAO
                #event_id = EventsDAO().insert(authorId,text,meta_image_url,summary,title,post_image_url)
                event_id = EventsDAO().insert(form)

                #result = Event().build_dict_from_row(dao.getEventById(event_id))
                #return jsonify(result), 201
                result = dao.getEventById(event_id)
                return result
            else:
                return dict(Error="Unexpected attributes in post request"), 400
    #UPDATE
    def updateEventContent(self, event_id, form):
        #TODO SAME AS ABOVE
        if leafcounter(form) < 6:
            return dict(Error="Malformed post request"), 400
        else:
            author_name = form['author']
            date = form['date']
            image_url = form['image_url'] 
            last_update = form['last_update']
            text = form['text']
            title = form['title']
        dao = EventsDAO()
        if not dao.get_event_by_id(event_id):
            return dict(Error="Event not found."), 404
        dao_u = UsersDAO()
        if not dao_u.get_user(author_name):
            return dict(Error="Author User not found."), 404
        else:
            #does it even need to be validated at this point?
            if author_name and text and date:
                # this is updating both, can be split into two methods if needed....
                event_id = dao.update_event_content(event_id,form)
                result = dao.get_event_by_id
                return result
                # result = Event().build_dict_from_row(dao.getEventById(event_id))
                # return jsonify(result), 201
            else:
                return dict(Error="Unexpected attributes in post request"), 400
    def updateEventMetadata(self, event_id, form):
        #TODO SAME AS ABOVE
        if leafcounter(form) < 6:
            return dict(Error="Malformed post request"), 400
        else:
            author_name = form['author']
            date = form['date']
            image_url = form['image_url'] 
            last_update = form['last_update']
            summary = form['summary']
            title = form['title']
        dao = EventsDAO()
        if not dao.get_event_by_id(event_id):
            return dict(Error="Event not found."), 404
        dao_u = UsersDAO()
        if not dao_u.get_user(author_name):
            return dict(Error="Author User not found."), 404
        else:
            #does it even need to be validated at this point?
            if author_name and date:
                # this is updating both, can be split into two methods if needed....
                event_id = dao.update_event_metadata(event_id,form)
                result = dao.get_event_by_id
                return result
                # result = Event().build_dict_from_row(dao.getEventById(event_id))
                # return jsonify(result), 201
            else:
                return dict(Error="Unexpected attributes in post request"), 400

    def removeEventMetadata(self, event_id):
        dao = EventsDAO()
        event = dao.get_event_by_id(event_id)
        if not event:
            return dict(Error="Event Not Found"),404
        else:
            event_id =  dao.fake_remove_event_metadata(self,event_id)
            return event_id
    
    def removeEventContent(self, event_id):
        dao = EventsDAO()
        event = dao.get_event_by_id(event_id)
        if not event:
            return dict(Error="Event Not Found"),404
        else:
            event_id = dao.fake_remove_event_content(self,event_id)
            return event_id

    def removeEventComments(self,event_id):
        dao = EventsDAO()
        event = dao.get_event_by_id(event_id)
        if not event:
            return dict(Error="Event Not Found"),404
        else:
            return dao.fake_remove_event_comments(self,event_id)

    def addComment(self,event_id,comment):
        dao = EventsDAO()
        event = dao.get_event_by_id(event_id)
        dao_u = UsersDAO()
        if not event:
            return dict(Error="Event Not Found"),404
        else:
            if not dao_u.get_user(comment['user']):
                return dict(Error="Author User Not Found"),404
            else:
                comment_id =dao.add_comment(self, event_id,comment)
                return comment_id

    def updateComment(self,event_id,comment_id,new_comment):
        dao = EventsDAO()
        event = dao.get_event_by_id(event_id)
        #check existing event
        if not event:
            return dict(Error="Event Not Found"),404
        else:
            #check exiting comment
            if not event['comments'][comment_id]:
                return dict(Error="Comment Not Found"),404
            else:
                #check valid user editing
                if event['comments'][comment_id]['user'] != new_comment['user']:
                    return dict(Error="Invalid User."), 400
                else:
                    comment_id = dao.edit_comment(self,event_id,comment_id,new_comment)
                    return comment_id
    def removeCommentbyId(self,event_id,comment_id):
        dao = EventsDAO()
        event = dao.get_event_by_id(event_id)
        #check existing event
        if not event:
            return dict(Error="Event Not Found"),404
        else:
             #check exiting comment
            if not event['comments'][comment_id]:
                return dict(Error="Comment Not Found"),404
            else:
                comment_id = dao.fake_remove_comment_by_id(self,event_id,comment_id)
                return comment_id

                