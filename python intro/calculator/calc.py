def main():
    var1 = input("Number One: ")
    var2 = input("Number Two: ")
    var3 = input("What would you like to calculate? ")

    sum = float(var1) + float(var2)
    product = float(var1) * float(var2)

    if var3 != "sum" or var3 != "difference" or var3 != "product" or var3 != "quotient":\
        print("Please calculate sum, difference, product or quotient.")

    if var3 == "sum":
        print(sum)

    if var3 == "difference":
        if var1 > var2:
            difference = float(var1) - float(var2)
        else:
            difference = float(var2) - float(var1)

        print(difference)

    if var3 == "product":
        print(product)

    if var3 == "quotient":
        if var1 > var2:
            quotient = float(var1) / float(var2)
        else:
            quotient = float(var2) / float(var1)

        print(quotient)

    var4 = input("Would you like to calculate more? ")

    if var4 == "yes":
        main()

    else:
        exit

main()


