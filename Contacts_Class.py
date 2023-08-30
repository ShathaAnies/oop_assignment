class Contacts:
    def __init__(self,name , phone ,email ):
        self.name = name
        self.phone =phone
        self.email =email 

    def __str__(self) :
        return f"Contact name is: {self.name} ===> Contact phone number is: {self.phone} ==> Contact E-mail is: {self.email}"

class Contact_Manager (Contacts):
    def __init__(self ):

        self.contactsList =[] 

    def Add (self , contact):
        self.contactsList.append(contact) 

    def Delete (self ,contact):
        if contact in self.contactsList:
            self.contactsList.remove(contact)
            print("contact deleted:) ")
        else :
            return "There is no Contact with This name:("
       
    def search(self , name):
        
        for contact in self.contactsList:
            if contact.name.lower()== name.lower():
                return contact
            else:
                return "None"
                
    def display(self):
        for contact in self.contactsList:
            print (contact)




def List_choises():
    
    print("Contact Manager: \n1. Add Contact \n 2. Remove Contact \n 3. Search Contact \n 4. Display Contact \n 5. Exit ")


contact_Manager=Contact_Manager()
var = True
while var == True:
    List_choises()
    numOperation = input("Enter your choice: ")
    if numOperation == "1":
        name = input("Enter the Contact name: ")
        phone = input("Enter the Contact phone number: ")
        email= input("Enter the Contact E-mail: ")
        contact=Contacts(name,phone,email)
        contact_Manager.Add(contact)
        print ("Contact Added successfully")
    elif numOperation == "2":
        name = input("Enter the name of the contact that you want to remove: ")
        contact=contact_Manager.search(name)

        if contact:
            contact_Manager.Delete(contact)
        else :
            print ("Contact not founded")
    elif numOperation == "3":
        name = input("Enter the name of the contact that you want to search for: ")
        if contact:
            contact=contact_Manager.search(name)
            print("Contact Founded:) ")
            print (contact)
        else :
            print ("Contact not founded")    
    elif numOperation == "4":
        contact_Manager.display()
    elif numOperation == "5":
        break
    else:
        print("Error please enter number from the list, try another number:) ")