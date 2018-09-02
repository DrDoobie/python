def main ():
    import random
    dice = random.randint(1, 6)
    print("Result: ", dice)

    input1 = input("Roll again? ")

    if input1 == "yes":
        main()
    else:
        exit

main()
