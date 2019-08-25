#This program acts as the database
import json

class ActivityList:
    def __init__(self):
        with open('StoredData.json', 'r') as rf:
            try:
                data = json.load(rf)
                self.activity_list = self.get_activities(data)
                self.writeList()
            except:
                self.activity_list = []
                self.writeList()

    def get_activities(self, data):
        return_list = []
        for activity in data['activities']:
            return_list.append(Activity(activity['name'], activity['start_time']))
        return return_list
    
    def writeList(self):
        with open('output.json', 'w') as f:
            json.dump(self.serialize(), f, indent=4, sort_keys=True)

    def serialize(self):
        return {
            "activities": self.activities_to_json()
        }
    
    def activities_to_json(self):
        return_list = []
        for actv in self.activity_list:
            return_list.append(actv.serialize())
        return return_list

    def commitList(self):
        with open('storedData.json', 'w') as f:
            json.dump(self.serialize(), f, indent=4, sort_keys=True)

    def addActivity(self, name, start_time):
        found = False
        for actv in self.activity_list:
            if actv.name == name:
                found = True
        if found:
            pass
        else:
            self.activity_list.append(Activity(name, start_time))
            self.writeList()

    #def isActivity(self, name):
    #    return any(i['name'] == name for i in self.activity_list)

    

class Activity:
    def __init__(self, name, start_time):
        self.name = name
        self.start_time = str(start_time)

    def serialize(self):
        return {
            "name": self.name,
            "start_time": self.start_time
        }
    