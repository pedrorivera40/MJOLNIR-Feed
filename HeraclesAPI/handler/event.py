from flask import jsonify

class EventHandler:
    def getAllEvents(self):
        dao = EventsDAO()
        events_list = dao.getAllEvents()
        results_list = []
        for row in events_list:
            result = Event().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(result_list)
    
    def getEventByID(self, eventId):
        dao = dao.getEventbyId(eventId)
        if not row:
            return jsonify(Error = "Category Not Found"), 404
        else: 
            event = Event().build_dict_from_row(row)
            return jsonify(category)
    

