# # Cinema Booking System # #

films = {
    "Toy Story" : [3,5],
    "Bahubali" : [18 , 5],
    "Interstellar" : [15,5],
    "Ghost Rider" : [12, 5]
}
while True :
    choice = input("Which Movie Would You Like To Watch : ").strip().title()

    if choice in films:
        age = int(input("How Old are you ? ").strip())
    # Check User Age
        if age >= films[choice][0]:
            # Check Seats Availability
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy The Movie")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry!!!! All the Tickets For this movie is sold")
        else:
            print("Sorry You are under aged")
    else:
        print("Sorry We dont Have that Movie")


