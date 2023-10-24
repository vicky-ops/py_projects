try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator/denominator

except ValueError as ve:
    # Handling a specific exception (ValueError)
    print(f"Error: {ve}. Please Enter a valid number")

except ZeroDivisionError as zd:
    # Handling another specific exception (ZeroDivisionError)
    print(f"Error: {zd}. Division by zero is not allowed")

except Exception as e:
    # Handling a more general exception
    print(f"An error occurred: {e}. Please try again")

else:
    # Code to execute if no exception occured
    print(f"Result: {result}")

finally:
    print("Execution complete")