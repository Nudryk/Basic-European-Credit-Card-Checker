def CheckCB(card_number):
    card_number = [int(i) for i in card_number if i.isdigit()]
    card_number.reverse()
    total = 0
    for i, num in enumerate(card_number):
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
        total += num
    return total % 10 == 0

def main():
    card_number = input("Enter a credit card number: ").replace(" ", "")
    isValid = True
    
    if len(card_number) != 16:
        isValid = False
    else:
        for number in card_number:
            if number.isalpha():
                isValid = False
                break
    
    if isValid:
        isValid = CheckCB(card_number)
    
    if isValid:
        print("✅ Valid card number")
    else:
        print("❌ Invalid card number")
    
if __name__ == "__main__":
    main()
