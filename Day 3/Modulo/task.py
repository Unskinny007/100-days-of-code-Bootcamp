from selenium.webdriver.common.devtools.v85.debugger import continue_to_location

number_to_check = int(input("Give me a number: "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")
    
