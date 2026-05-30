# user input as a number
temperature = int(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("it is suitable for wearing light clothes")
else:
    print("it is not suitable for wearing light clothes")
if temperature > 35:
    print("it is too hot for wearing light jackets advised to wear light chlothes")
if temperature < 20:
    print("it is too cold for wearing light jackets advised to wear heavy chlothes")