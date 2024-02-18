while True:
    try:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        print(f"num1 / num2 = {int(num1 / num2)}")
        break
    except Exception as e:
        print("Failed OW master")
