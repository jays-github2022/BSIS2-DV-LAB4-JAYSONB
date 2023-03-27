

# Logical Operators
# and, or, not
# used to check if two or more conditional statements is true or false
#evaluates if temperature is greater than equal to 0 and less than or equal to 30 
#try to enter values from equal to 0 or greater than 0
#try to enter values less than or equal to 30
#first condition >= 0 is false but the second condition <=30 is true
#it will print the desired output having a good temperature

temperature = int(input("Enter the temperature outside to check the condition: "))

if temperature  >= 0 and temperature <= 30: 
  print("The temperature is good today") 
  print("You may go outside!")
elif temperature >= 31 or temperature >= 40:
    print("The temperature is bad today")
    print("Please bring an umbrella or any protection")
