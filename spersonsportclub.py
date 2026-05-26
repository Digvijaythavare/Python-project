class Persson:
    def accept_person_detial(self):
        self.name = input("Enter person Name: ")
        self.Contact = int(input("Enter Contact Number: "))
        self.dob = input("Enter DOB: ")

    def show_person_detial(self):
        print("Person Name is: ",self.name)    
        print("Contact Number is: ",self.Contact)    
        print("Date of birth is: ",self.dob)    

class SportClub(Persson):
    def accept_sport_clube_detail(self):
        self.sports = input("Enter Sports Name: ")
        self.coach = input("Enter Coach Name: ")
        self.fee = int(input("Enter Coach Fee: "))

    def show_sport_clube_detail(self):
        print("Sports Name is: ",self.sports)    
        print("Coach Name is: ",self.coach)    
        print("Coach Fee is: ",self.fee)        


sportman1 = SportClub()
sportman2 = SportClub()

sportman1.accept_person_detial()
sportman1.accept_sport_clube_detail()

sportman2.accept_person_detial()
sportman2.accept_sport_clube_detail()

print("Sportman 1 Detail: ")
sportman1.show_person_detial()
sportman1.show_sport_clube_detail()


print("Sportman 2 Detail: ")
sportman2.show_person_detial()
sportman2.show_sport_clube_detail()