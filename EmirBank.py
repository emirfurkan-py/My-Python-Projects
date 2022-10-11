#CARD HOLDER
class cardHolder():
    def __init__(self,cardNum,pin,firstname,lastname,balance) :
        self.cardNum=cardNum
        self.pin=pin
        self.firstname=firstname
        self.lastname=lastname
        self.balance=balance

    #Getter methods    
    def get_cardNum(self):
        return self.cardNum
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance    


    #Setter methods
    def set_cardNum(self,newVal):
        self.cardNum=newVal
    def set_pin(self,newVal):
        self.pin=newVal
    def set_firstname(self,newVal):
        self.firstname=newVal
    def set_lastname(self,newVal):
        self.lastname=newVal
    def set_balance(self,newVal):
        self.balance=newVal 

    def print_out(self):
        print("Card #: ",self.cardNum)
        print("Pin #: ",self.pin)
        print("First Name #: ",self.firstname)
        print("Last Name #: ",self.lastname)
        print("Balance #: ",self.balance)

#ATM
def print_Menu():
    ### Print options to the user
    print("Please choose from one of the following options...")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Show Balance")
    print("4.Exit")

def deposit(cardHolder):
    try:
        deposit=float(input("How much would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance()+deposit)
        print("Your new balance is: ", str(cardHolder.get_balance()))


    except:  
        print("İnvalid İnput")  

def withDraw(cardHolder):
    try:
        withdraw=float(input("How much would you like to withdraw: "))
        ##Check if user enough money
        if(cardHolder.get_balance()>withdraw):
            cardHolder.set_balance(cardHolder.get_balance()-deposit)
            print("Your new balance is: ", str(cardHolder.get_balance()))
        else:
            print("İnsufficient balance")

    except:  
        print("İnvalid İnput")  

def check_balance(cardHolder):
    print("Your current balance is: ",cardHolder.get_balance())

if __name__== "__main__":
    
    current_user=cardHolder("","","","","")
    
    ### Create a repo of cardholders
    list_of_cardHolders=[]
    list_of_cardHolders.append(cardHolder("123456",1234,"John","Griffin",150))
    list_of_cardHolders.append(cardHolder("128926",1234,"John","Griffin",3000))
    list_of_cardHolders.append(cardHolder("136556",1234,"John","Griffin",1200))
    list_of_cardHolders.append(cardHolder("189456",1234,"John","Griffin",11050))
    list_of_cardHolders.append(cardHolder("121156",1234,"John","Griffin",144))

    #Prompt user for debit card number

    debitCardNum=""
    while True:
        try:
            debitCardNum=input("Please insert your debit card:")
            ###Check againtst repo
            debitMatch=[holder for holder in list_of_cardHolders if holder.cardNum==debitCardNum]
            if(len(debitMatch)>0):
                current_user=debitMatch[0]
                break
            else:
                print("Card number not recognized.Please try again...")

        except:
            print("Card number not recognized.Please try again")  

    ##Prompt for PIN
    while True:
        try:
            userPin=int(input("Please enter your PİN:").strip())
            if(current_user.get_pin()==userPin):
                break
            
            else:
                print("Invalid PİN.Please try again.")

        except:
            print("İnvalid PİN. Please try again.")

    ##Print options
    print("Welcome",current_user.get_firstname())
    option=0
    while(option!=4):
        print_Menu()
        try:
            option=int(input())
        except:
            print("İnvalid input. Please try again.")
        if  (option==1):
            deposit(current_user)
        elif(option==2):
            withDraw(current_user)  
        elif(option==3):
            check_balance(current_user) 
        elif(option==4):
            break
        else:
            option=0
    print("Have a nice day...")        