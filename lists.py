myUniqueList = []
myLeftOver = []


def num(new):
    if new in myUniqueList:
        leftoverword(new)
        return False
    else:
        myUniqueList.append(new)
        return True


def leftoverword(new):
    myLeftOver.append(new)


print(myUniqueList)
print(num("Nissan"))
print(myUniqueList)
print(num("Volvo"))
print(myUniqueList)
print(num("Nissan"))
print(myUniqueList)
print(num("Toyota"))
print(myUniqueList)
print(myLeftOver)