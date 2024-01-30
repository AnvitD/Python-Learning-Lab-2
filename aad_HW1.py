import sys

def main():

    print("Available movies today:")
    print("A)12 Strong:  1)2:30  2)4:40  3)7:50  4)10:50")
    print("B)Coco:       1)12:40  2)3:45")
    print("C)The Post:   1)12:45  2)3:35  3)7:05  4)9:55")

    choice = input("Movie choice: ")

    showtime = int(input("Showtime: "))
    if choice != "A" and choice != "B" and choice != "C":
        print("Invalid option; please restart app...")
        sys.exit()

    if showtime != 1 and showtime != 2 and showtime != 3 and showtime != 4:
        print("Invalid option; please restart app...")
        sys.exit()

    if choice =="B" and showtime ==3:
        print("Invalid option; please restart app...")
        sys.exit()
    
    if choice =="B" and showtime ==4:
       print("Invalid option; please restart app...")
       sys.exit()
    

    Atickets = int(input("Adult tickets: "))
    Ktickets = int(input("Kid tickets: "))
    if (Atickets + Ktickets) > 30: 
        print("Invalid option; please restart app...")
        sys.exit()



    if choice =="A" and showtime ==1:
        price = round((Atickets * 11.17) + (Ktickets * 8.00), 2)
        print(f"Total cost: $ {price}")

    elif choice =="A" and showtime ==2:
        price = round((Atickets * 12.45) + (Ktickets * 9.68), 2)
        print(f"Total cost: $ {price}")
    
    elif choice =="A" and showtime ==3:
        price = round((Atickets * 12.45) + (Ktickets * 9.68), 2)
        print(f"Total cost: $ {price}")
    
    elif choice =="A" and showtime ==4:
        price = round((Atickets * 12.45) + (Ktickets * 9.68), 2)
        print(f"Total cost: $ {price}")
    
    elif choice =="B" and showtime ==1:
        price = round((Atickets * 11.17) + (Ktickets * 8.00), 2)
        print(f"Total cost: $ {price}")

    elif choice =="B" and showtime ==2:
        price = round((Atickets * 12.45) + (Ktickets * 9.68), 2)
        print(f"Total cost: $ {price}")
    
    elif choice =="C" and showtime ==1:
        price = round((Atickets * 11.17) + (Ktickets * 8.00), 2)
        print(f"Total cost: $ {price}")

    elif choice =="C" and showtime ==2:
        price = round((Atickets * 12.45) + (Ktickets * 9.68), 2)
        print(f"Total cost: $ {price}")
    
    elif choice =="C" and showtime ==3:
        price = round((Atickets * 12.45) + (Ktickets * 9.68), 2)
        print(f"Total cost: $ {price}")
    
    elif choice =="C" and showtime ==4:
        price = round((Atickets * 12.45) + (Ktickets * 9.68), 2)
        print(f"Total cost: $ {price}")
     

if __name__ == "__main__":
    main()