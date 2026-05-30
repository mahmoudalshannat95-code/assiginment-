print('Hi ALL')
#Question 1:Ask the user to enter a number, then print its multiplication table from 1 to 10
number = int(input("enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
print(50*'==')



#Question 2: Count Even Numbers 
#Write a program that prints all even numbers from 1 to 30. 
#At the end, print how many even numbers were found.
for i in range(1, 31):
    if i % 2 == 0:
        print(i)
        print(f"total even numbers from 1 to 30 is: {i//2}")


print(50*'==')


#Question 3: Password Attempts 
#Write a program that asks the user to enter a password. 
correct_password = "python123"
is_not_logged_in = True
while is_not_logged_in:
    password = input("enter your password: ")
    if password == correct_password:
        print("Correct Password! you are authorized!")
        is_not_logged_in = False
    else:
        print("Login failed!")
        print("The user has only 3 attempts to enter the correct password.")

print(50*'==')


#Question 4: Calculate Average Marks 
#Ask the user how many marks they want to enter. 
#Then ask them to enter the marks one by one. 
#Finally, print the average mark. 

is_valid_input = True
is_number_of_marks=4
while is_valid_input:
   number_of_marks=float(input(" How Many Marks Want to Ener:"))
   if (is_number_of_marks==number_of_marks):
      print ('you can enter your marks now')
      is_valid_input=False
   else:
      print('try againe')

is_mark1=True

while is_mark1:
      
      mark1=int(input("Enter mark 1: "))
      
      mark1<=100
      mark1>=0
      if (mark1==mark1):
        print(0<=mark1<=100)
         
        print ('you can enter  mark2 now')
        
        is_mark1=False
      else:
            print('enter correct mark1')

is_mark2=True

while is_mark2:
      mark2=int(input("Enter mark 2: "))
      
      mark2<=100
      mark2>=0
      if (mark2==mark2):
        print(0<=mark2<=100)
         
        print ('you can enter  mark3 now')
        
        is_mark2=False
      else:
         
         print('enter correct mark2')

is_mark3=True

while is_mark3:
      mark3=int(input("Enter mark 3: "))
      
      mark3<=100
      mark3>=0
      if (mark3==mark3):
        print(0<=mark3<=100)
         
        print ('you can enter  mark4 now')
        
        is_mark3=False
      else:
         
         print('enter correct mark3')

is_mark4=True
while is_mark4:
    mark4=float(input("Enter mark 4: "))
    if (mark4<=100):
        print('you enterd all marks')
    elif(mark4>100):
            print ('correct mark4')
    is_mark4=False

    if(mark4<0):
        print('correct mark4')
        is_mark4=False
    else:
    
        print('correct mark4')
marks=(mark1+mark2+mark3+mark4)/4
print("averge:", marks, "%")
print(50*'==')   
print(50*'==')

#Question 5: Number Guessing Game 
#Create a number guessing game. 
#Use this fixed secret number: 
secret_number=7
is_guess=True

while is_guess:
        guess_number=int(input('Enter your guess numbe:'))
        if guess_number<secret_number:
            print ('Too low')
        
        if guess_number>secret_number:
              print('Too Hight')
              is_guess=True   
        if guess_number==secret_number:
           print('correcr:') 
           break  
                   
print(50*'==')           
#Question 6: Simple ATM Menu 
#Create a simple ATM program. 
#Start with this balance: 
print('WELLCOME IN AL SHON BANK')
print('Your Balance is 1000 USD')
print('THE MENU')
print('1-Check the Balance:')
print('2-Deposit Money:')
print('3-Withdraw Money:')
print('4-Exit:')
balance=1000

Check_the_Balance="balance"
while True:
    
    value=float(input(' Enter Number of your opporation:'))
    print('WELLCOME IN AL SHON BANK')
    print('THE MENU')
    print('1-Check the Balane:')
    print('2-Deposit Money:')
    print('3-Withdraw Money:')
    print('4-Exit:')
    is_value_balance=1
    is_value_deposit=2
    is_value_withdraw=3
    is_value_exit=4
    if (is_value_balance==value):
        
        print("Your Balance is")
        print(balance,"USD")
    if (is_value_deposit==value):
     
     deposit=float (input('how many you want to doposite:')) 
     
     print(f"{deposit} + {balance} = {deposit+balance }")
     print("Your Balance is")
     balance=deposit+balance
     print(balance,"USD")
    if (is_value_withdraw==value):
       
        withdraw=float(input('how money to want to withdraw:'))
        print(f" {balance}-{withdraw} = {balance -withdraw}")
        print("Your Balance is")
        balance=balance-withdraw
        print(balance,"USD")
    if (is_value_exit==value):
       print ("Thank you to use our bank")   

print(50*'==')
print(50*'==')
print(50*'==')      
 #Bonus Questions 
how_many_students=int(input("Enter the number of students: "))
the_name_of_students=[]

for i in range(0,how_many_students):
    the_name_of_students.append(input("Enter the name of student: "))   
    subjects=int(input("Enter the number of subjects: "))

    for x in range (0,subjects):
     number_of_subjects=(input(" subject number : "))
     the_marks=int(input("Enter the marks of the subject: "))
     average_marks=the_marks/subjects
     
    print("The average marks of the student is: ",average_marks) 
    if average_marks>=50:
         print("The student is: pass") 
    elif average_marks<50: 
         print("The student is: fail") 

print("The names of students are: ",the_name_of_students)
print("The total number of students is: ",how_many_students)
print("passed students are: ",the_name_of_students[0:how_many_students])
print("failed students are: ",the_name_of_students[0:how_many_students])
print("the highest marks is: ",the_marks)
print("the lowest marks is: ",the_marks)
print("the top student is: ",the_name_of_students[0])
the_top_student_marks=average_marks
print("the top student marks is: ",the_top_student_marks)


