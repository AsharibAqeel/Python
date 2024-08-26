def divide_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError as e:
        print("Error: Division by zero is not allowed.")
        print(f"Exception details: {e}")

divide_by_zero()
