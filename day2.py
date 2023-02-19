print("\n\033[34m ~~Generation Identifier~~")
print()
myYear = int(input("\n\033[35m what year where you born?  "))
if myYear >= 1925 and myYear <=1946:
    print("--Traditionalist--")
elif myYear >= 1947 and myYear <=1964:
    print("--Baby Boomer--")
elif myYear >=1965 and myYear <=1981:
    print("--Gen X--")
elif myYear >=1981 and myYear <=1995:
    print("--Millennial")
elif myYear >=1995 and myYear<=2015:
    print('--Gen Z--')