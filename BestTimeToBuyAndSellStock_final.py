def bestTimeToBuyAndSellStock(myList):
    maxDiff = 0 
    minItem = myList[0]

    for i in range(len(myList)):
        if myList[i] < minItem:
            minItem = myList[i]
            
        maxDiff = max(maxDiff, myList[i] - minItem)

    return maxDiff 

print(bestTimeToBuyAndSellStock([21,22,10,15,1,3]))