print("Wellcome to mansion in the woods ")
print("Do you want to play? ")

playGame = input(":")


if playGame == ("yes"):

    print("")
    print("""You are a journalist who has been assigned to investigate a mysterious mansion in the woods. You have heard rumors of strange noises, 
          disappearances, and paranormal activity in the area. You decide to spend the night in the mansion and see for yourself what is going on.""")
    
    print("")
    
    print("""You arrive at the mansion as the sun is setting. You park your car in front of the gate and grab your backpack.
           You see a large wooden door with a rusty knocker. You knock on the door, but there is no answer. 
          You try the handle, and find that it is unlocked. You enter the mansion.""")
    
    print("")
    
    print("""You are in a dark and dusty hallway. There are paintings on the walls, some of them covered with cobwebs.
           You see a staircase leading up, and a faint light coming from the end of the hall.  """)
    
    print("What do you want to do?")

    print("")

    print("Go upstairs")
    print("Go to the end of hall")

    q1 = input(":")

    if q1 == ("go upstairs"):
             print("")
             print("You walk upstairs and find an old piano that is covered in a white sheet")
             print("")
             print("behind the piano you see a figuer that you think to be a person, but upon further inspection you realise its a manneqin")
             print("")
             print("What do you do?")
             print("")
             print("Uncover the piano") 
             print("Go to the manneqin")  

             q2upstairs = input(":")

             if q2upstairs == ("uncover the piano"):
                  print("")
                  print("You wall to the piano and pull the white sheet off sturing up abunch of dust")
                  print("""from the corner of the room you hear a you see the manneqin move. you jump back and watch the manneqin but it's not moving anymore.
                        """)
                  print("What do you do?")
                  print("")
                  print("Go to the manneqin")
                  print("Leave the mansion")

                  q3upstairs = input(":")

                  if q3upstairs == ("go to the manneqin"):
                       print("")
                       print("You walk up to the manneqin and it attacks you. You are now dead game over")

                  elif q3upstairs == ("leave the mansion"):
                          print("")
                          print("You leave the mansion and go home to never retun angin. game over")

                  else:
                       print("Not a valid option")

             elif q2upstairs == ("go to manneqin"):
                  print("")
                  print("You walk up to the manneqin and it attacks you. You are now dead game over")
                                      

            
    elif q1 == ("go to the end of hall"):
        print("")
        print("""You walk towards the window, curious about the source of the light. You see a large garden behind the mansion, with a fountain, a gazebo, and a hedge maze. 
              The light is coming from a lantern hanging from the gazebo. You also notice a figure sitting on a bench near the fountain. It looks like a woman, wearing a white dress and a veil.
               She is holding something in her hands, but you can’t tell what it is""")
        print("")
        print("What do you do?")
        print("")
        print("Go back to car and leave")
        print("Call out to the woman")
        print("Go outside and approch the woman") 

        q2hall = input(":")

        if q2hall ==  ("go back to car and leave"):
             print("")
             print("You leave the mansion and go home to never retun angin. game over")

        elif q2hall == ("call out to the woman"):
            
             print("She doesn't not respont at all")
             print("What do you do?")
             print("")
             print("Go back to car and leave")
             print("go outside and approch the woman")

             q3hall = input(":")

             if q3hall == ("go back to car and leave"):
                  print("")
                  print("You leave the mansion and go home to never retun angin. game over")

             elif q3hall == ("go outside and approch the woman"):
                  print("")
                  print("""You decide to go outside and approach the woman, hoping to get some answers.
                         You open the door and step into the garden. You feel a cold breeze on your skin, and hear the sound of water from the fountain.
                         You walk towards the gazebo, where the woman is sitting""")
                  print("")
                  print("Once you get to the woman and say hello she attacks you. you are now dead. game over")
            
             else:
                  print("Not a valid option")


        elif q2hall == ("go outside and approch the woman"):
                print("")
                print("""You decide to go outside and approach the woman, hoping to get some answers.
                         You open the door and step into the garden. You feel a cold breeze on your skin, and hear the sound of water from the fountain.
                         You walk towards the gazebo, where the woman is sitting""")
                print("")
                print("Once you get to the woman and say hello she attacks you. you are now dead. game over")
    
    

    else:
         print("Not a valid option")
    

   
       
       
elif playGame == ("no"):
   print("Goodbye")
   
else :
    print("Not a valid option. Please say yes or no")