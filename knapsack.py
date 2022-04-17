
def knapsack(capacity, itemList):
    
    '''Takes input of knapsack capacity as a maximum value and a list of items
    in the knapsack's weight and value, and checks if the knapsack is full.
    Capacity of the knapsack cannot be exceeded.'''

    if itemList == []:
        return [0,[]]

    if capacity == 0:
        return [0,[]]

    if capacity < itemList[0][0]:
        return knapsack(capacity, itemList[1:])

    useIt = knapsack(capacity - itemList[0][0], itemList[1:]) 
    newSum = itemList[0][1] + useIt[0]
    loseIt= knapsack(capacity, itemList[1:])

    if newSum > loseIt[0]:
        return [newSum, [itemList[0]] + useIt[1]]

    return loseIt       
