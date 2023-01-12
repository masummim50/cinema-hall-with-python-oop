class Star_Cinema:
    __hall_list = []
    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__hall = {}
        self.__hall['rows'] = rows
        self.__hall['cols'] = cols
        self.__hall['hall_no'] = hall_no
        self.__hall['seats'] ={}
        self.__hall['show_list'] = []
        self.entry_hall(self.__hall)
    
    def entry_show(self, movie_name, id, time):
        self.show = {"name": movie_name, "id": id, "time": time}
        self.seat = []
        r = 65
        for i in range(self.__hall['rows']):
            c = 0
            a = ["False" for j in range(self.__hall['cols'])]
            r+=1
            self.seat.append(a)

        self.__hall['seats'][id] = self.seat
        self.__hall['show_list'].append(self.show)
    
    def book_seats(self):
        self.name = input("enter your name: ")
        self.phone = input("enter your phone: ")
        self.show_id = input("enter show id: ")
        if any(d['id'] == self.show_id for d in self.__hall['show_list']):

            self.tickets = int(input("how many tickets: "))
            self.approved = []
            r = 1
            while(len(self.approved)!=self.tickets):
                    s = input("enter seat: ")

                    ro = ord(s[0])-65
                    co = int(s[1:])
                    # print(ro, co)
                    if(ro>self.__hall['rows']-1 or ro<0 or co>self.__hall['cols'] or co<1):
                        print("That is an invalid seat number")
                    elif(s in self.approved):
                        print("You already selected this seat")
                    elif(self.__hall['seats'][self.show_id][ro][co-1]=='False'):
                        # print("seat empty")
                        self.__hall['seats'][self.show_id][ro][co-1] = 'True'
                        self.approved.append(s)
                    else:
                        print("This seat is not available")
            print()
            print(f"{len(self.approved)} seat booked successfull")
            print()
        else:
            print()
            print("Show id does not match to any available show")
            print()


    def view_show_list(self):
        list = self.__hall['show_list']
        print()
        print(f"Movie Name \t\t Movie id \t\t Time")
        print(f"{'-'*55}")
        for l in list:
            print(f"{l['name']} \t\t {l['id']} \t\t\t {l['time']}")
        print()


    def view_available_seats(self):
        id = input("enter id of show: ")
        if any(d['id'] == id for d in self.__hall['show_list']):
            print()
            print(f"{'#'*15} Seats for this show {'#'*15}")
            print()
            seat_list = self.__hall['seats'][id]
            r = 65
            for i in seat_list:
                c = 1
                for j in i:
                    if(j == 'True'):
                        print("X", end = "\t")
                    else:
                        print(f"{chr(r)}{c}", end="\t")
                    c+=1
                r+=1
                print()
        else:
            print()
            print("Show id does not match to any")
            print()


    

s = Hall(4,8,'DH8')
s.entry_show("Black Adam", "BA", "12pm")
s.entry_show("The Good Nurse", "TGN", "2pm")

run = 1
while(run!=0):
    print("0. To quit this loop")
    print("1. View the show list")
    print("2. View available seats")
    print("3. Buy tickets")
    print()
    choice = input("enter your choice: ")
    if(choice.isdigit()):
        choice = int(choice)
    else:
        print("Not an available choice")
        continue

    if(choice == 1):
        s.view_show_list()
    elif(choice == 2):
        s.view_available_seats()
    elif(choice == 3):
        s.book_seats()
    elif(choice == 0):
        run = 0
    else:
        print("Not an available choice")

# # print(s.hall['show_list'])
# s.view_available_seats()
# s.book_seats()
# s.view_available_seats()
# # s.view_show_list()
# # print(s.hall['seats'])
