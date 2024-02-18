while True:
    try:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        print(f"num1 / num2 = {int(num1 / num2)}")
        break
    except:
        print("Failed")
