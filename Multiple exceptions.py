try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print("Result:", result)
    print("Result:", result1)

except ZeroDivisionError:
    print("Division by zero is not allowed.")    
except ValueError:
    print("lease enter numericalvalue")
except NameError as ex:
    print("The exception is:", ex)

except:
    print("Some error occurred.")
finally:
    print("I will execute no matter what happens.")