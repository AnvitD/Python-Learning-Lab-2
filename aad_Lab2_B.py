def main():
    
    gallons = float(input("Enter your water usage in gallons: "))

    if gallons <= 5999: 
        out = round(((gallons/1000) * 2.35), 2)
        print(f"Money owed: ${out}")
    elif gallons <= 20000:
        first = (gallons - 5999)
        out = round((((5999/1000) * 2.35) + ((first/1000) * 3.75)), 2)
        print(f"Money owed: ${out}")
    else:
        first = (gallons - 20000)
        out = round((((5999/1000) * 2.35) + (((20000-5999)/1000) * 3.75) + ((first/1000) * 6.00)), 2)
        print(f"Money owed: ${out}")

if __name__ == "__main__":
    main()

