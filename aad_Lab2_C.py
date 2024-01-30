def main():

    print("Available Currencies: A)USD B)CAD C)YEN")

    amount = float(input("Enter transaction amount: "))
    Tcurrency = input("Transaction currency: ")
    Ccurrency = input("Currency to convert to: ")

    if Ccurrency == Tcurrency:
        print("Conversion not needed...")
    elif Tcurrency == "A" and Ccurrency == "B":
        out = round((amount * 1.24), 2)
        print(f"Converted value: {out} CAD")
    elif Tcurrency == "A" and Ccurrency == "C":
        out = round((amount * 108.59), 2)
        print(f"Converted value: {out} YEN")
    elif Tcurrency == "B" and Ccurrency == "A":
        out = round((amount/ 1.24), 2)
        print(f"Converted value: {out} USD")
    elif Tcurrency == "B" and Ccurrency == "C":
        out = (amount/1.24)
        out2 = round((out * 108.59), 220)
        print(f"Converted value: {out2} YEN")
    elif Tcurrency == "C" and Ccurrency == "A":
        out = round((amount/108.59), 2)
        print(f"Converted value: {out} USD")
    elif Tcurrency == "C" and Ccurrency == "B":
        out = (amount/108.59)
        out2 = round((out * 1.24), 2)
        print(f"Converted value: {out2} CAD")

if __name__ == "__main__":
    main()


    
