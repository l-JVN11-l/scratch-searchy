import scratchattach as scratch3
from scratchattach import Encoding
import os
from better_profanity import profanity

print(Encoding.decode('11834737333321'))

session = scratch3.Session("randomId", username="username")



conn = session.connect_cloud(project_id=679684393)

events = scratch3.CloudEvents(679684393)

@events.event
def on_set(event): 
    if event.var == 'TO_HOST':
      print(event.value)
      
      type = Encoding.decode(event.value).split('-')
      if type[0] == "1":
        print ("Create Requested")
        print (type[1])
        check = type[1]      
        bad_word = profanity.contains_profanity(check)
        if bad_word == True:
          to_project = Encoding.encode('Bad word detected!')

          with open('bw-log.txt', 'a') as bwlogs:
            bwlogs.write(f'\n"{event.value}" written by {event.user} >:(')
        
          conn.set_var("FROM_HOST", to_project)
        else:
          with open('database.txt', 'a') as file:
            file.write(f"\n{type[1]}")

            conn.set_var("FROM_HOST",Encoding.encode("Added, If anything is false a Searchy mod will change it")())
          #make it add type[1] to database.txt


        
      elif type[0] == "2":
        print ("Get data")
        print (type[1])  
        f = open('database.txt',  "r")
        found_data = "a"
        for x in f:         
          if type[1] in x:
            print("this statement works")
            found_data = "b"
            info = x
         
        print (found_data)
        if found_data == "a":
          to_project = Encoding.encode('FROM_HOST : ERROR 404')
          print("Error 404")
          conn.set_var("FROM_HOST", to_project)

        elif found_data == "b":
          print("Found")
          conn.set_var("FROM_HOST", Encoding.encode(info))
          
@events.event 
def on_ready():
   print("Event listener ready!")

events.start() 
