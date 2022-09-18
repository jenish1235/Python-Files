#  Ridiculos Security System
known_users = ["Jenish", "Jaisiddh", "Abhishek", "Dhruv", "Pritesh", "Jay", "Devang"] 

while True:
    print("Hii , I am security guard ")
    name = input("Please enter your name to access the system : ").strip().capitalize()

    if name in known_users:
        print(f"Hello,{name} \n you have got the access to the system" )

        remove_user = input("Would you like to be removed from system, (y/n) : ").lower().strip()

        if remove_user == "y" : 
            known_users.remove(name)
            print(f"Okay! {name} You are now removed from my system")
        
        elif remove_user == "n" :
            print("I also don't want you to leave. Be Happy! Stay Cool!")
        
        else:
            break
    
    else:
        print(f"Sorry! {name} I am unable to recognize you.")
        add_me = input("Would you like to added to my system database ? (y/n) : ").strip().lower()

        if add_me == "y" :
            known_users.append(name) 
            print(f"Congratulations! {name} You are now a known users and can Access the system after reboot.")
        elif add_me == "n":
            print("No worries!!! Be Happy")
        else:
            break


