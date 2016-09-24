while True:
    try:
        count= raw_input("Please enter the first number:")
        count= int(count)
        break
    except ValueError:
        print("Not a valid integer! Please try again..... ")

while True:
    try:
        counter= raw_input("Please enter the second number:")
        counter= int(counter)
        break
    except ValueError:
        print("Not a valid integer! Please try again..... ")

for num in range(counter):

    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)
print "Great, you successfully entered an integer!"
