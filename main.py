import scratchattach as scratch3
from scratchattach import Encoding
import os
from better_profanity import profanity

session = scratch3.login("STCSchoolAccount", os.environ['PASSWORD'])

conn = session.connect_cloud(project_id=os.environ['PID'])

events = scratch3.CloudEvents(os.environ['PID'])

@events.event
def on_set(event): 
    if event.var == 'TO_HOST':
      type = Encoding.decode(event.value).split('-')
      if type[0] == "1":
        print ("Create Requested")
        print (type[1])
        check = type[1]      
        bad_word = profanity.contains_profanity(check)     # 
        if bad_word == "True":
          print (bad_word)
        else:
          print (bad_word)
          


        
      elif type[0] == "2":
        print ("Get data")
        print (type[1])  
        f = open('database.txt',  "r")
        found_data = 0
        for x in f:
          if type[1] in x:
            found_data = 1
            info = x

        print (found_data)
        if found_data == 0:
          to_project = Encoding.encode('FROM_HOST : ERROR 404')

        elif found_data == 1:
          to_project = Encoding.encode(info) 
        
        conn.set_var("FROM_HOST", to_project)
          
@events.event 
def on_ready():
   print("Event listener ready!")

events.start() 
