from pymongo import MongoClient
import urllib.parse
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        
     

        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            print("hello")
            self.client = MongoClient('mongodb://%s:%s@127.0.0.1:41259/AAC' % (username,password))
            
        else:
            self.client = MongoClient('mongodb://localhost:41259')
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary 
            if insert!=0:
                return True
            else:
                return False           
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    # Create method to implement the R in CRUD.
    def read(self,criteria = None):
       
        if criteria:
            data = self.database.animals.find(criteria,{"_id":False})
        else:
         
            data = self.database.animals.find( {} , {"_id":False})

        return data


    def readAll(self, data):
            found = self.database.animals.find({}).limit(35)    
            return(found)
    
    # Create a method to implement the U in CRUD
    def update(self,data):
        if data is not None:
            self.database.animals.save(data)
        else:
            raise Exception("Nothing to upate, because data parameter is empty")
    # Create a method to implement the U in CRUD
    def delete(self,data):
        if data is not None:
            self.database.animals.remove(data)
        else:
            raise Exception("Nothing to remove, because data parameter is empty")
            

    