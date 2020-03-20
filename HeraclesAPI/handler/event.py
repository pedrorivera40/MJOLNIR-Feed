from flask import jsonify

class EventHandler:
    #FOR GET
    def getAllEvents(self):
        dao = EventsDAO()
        events_list = dao.getAllEvents()
        #Since Firebase returns JSON dont need this anymore
        # results_list = []
        # for row in events_list:
        #     result = Event().build_dict_from_row(row)
        #     result_list.append(result)
        # return jsonify(result_list)
        return events_list
    
    def getEventByID(self, eventId):
        dao = EventsDAO()
        event = dao.getEventById(catId)
        if not event:
            return jsonify(Error = "Event Not Found"), 404
        else:
            return event 
            #event = Event().build_dict_from_row(row)
            #return jsonify(event)
    #POST 
    def insertEvent(self, form):
            #TODO:  verify what the appropiate len should be 
            if len(form) != 1:
                return jsonify(Error="Malformed post request"), 400
            else:
                #QUESTIONS!
                #-are there two image ids
                #-how do we divide content/metadata here?
                
                authorId = form['metadata']['userId']
                meta_image_url = form['metadata']['image_url'] 
                summary = form['metadata']['summary']
                title = form['metadata']['title']
                post_image_url = form['content']['image-url']
                text = form['content']['text']
        
                #what fields are obligatory? For now Author and Text
                if authorId and text:
                    dao_u = UsersDAO()
                    #vaidate existing user
                    if not dao_u.getUserById(authorId):
                        return jsonify(Error="Author User Not Found"),404
                    dao = EventsDAO()
                    # this is assuming it just passes NONE in those cases where it's empty in the form (say, no image)
                    eventId = EventsDAO().insert(authorId,text,meta_image_url,summary,title,post_image_url)
                    #result = Event().build_dict_from_row(dao.getEventById(eventId))
                    #return jsonify(result), 201
                    result = dao.getEventById(eventId)
                    return result
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400
    #UPDATE
    def updateEvent(self, eventId, form):
            #TODO SAME AS ABOVE
            if len(form) != 1:
                return jsonify(Error="Malformed post request"), 400
            else:
                authorId = form['metadata']['userId']
                meta_image_url = form['metadata']['image_url'] 
                summary = form['metadata']['summary']
                title = form['metadata']['title']
                post_image_url = form['content']['image-url']
                text = form['content']['text']
            dao = EventsDAO()
            if not dao_u.getEventById(eventId):
                return jsonify(Error="Event not found."), 404
            dao_u = UsersDAO()
            if not dao_u.getUserById(userId):
                return jsonify(Error="Author User not found."), 404
            else:
                #same as above, check len
                if len(form) != 1:
                    return jsonify(Error="Malformed update request"), 400
                else:
                    if meta_image_url:
                        #do we want to allow to change post author? prob not...
                        # this is again that an empty dic means None...check...
                        eventId = dao.update(eventId, meta_image_url,summary,title,post_image_url,text)
                        result = dao.getEventByID
                        return result
                        # result = Event().build_dict_from_row(dao.getEventById(eventId))
                        # return jsonify(result), 201
                    else:
                        return jsonify(Error="Unexpected attributes in post request"), 400
