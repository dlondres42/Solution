# auxiliary function which returns the sum of the dictionary
def new_sum(dic):
    somma = 0
    for k, v in dic.items():
        somma += k * v  # sum is equal to the key times its value

    return somma


track = []  # global variable which will be returned by the main function


# This is the main function
def makeChange(coins: list[int], target: int, so_far=None):
    # It is a generalized solution which works with any set of coins and any target
    if so_far is None:
        so_far = {i: 0 for i in coins[::-1]}  # This line will create a dictionary
        # keys = coins
        # values = coin's quantities

    somma = new_sum(so_far)  # It sums the content of the dictionary (keys * values)

    if somma == target:  # If the sum equals the target, it will be added to the global track
        if so_far not in track:
            track.append(so_far)
        return
    elif somma > target:  # Else, it does nothing
        return

    for i in coins:
        temp = so_far.copy()
        temp[i] += 1

        makeChange(coins, target, temp)  # Recursive call to return the same calculations with the temporary array

    return [list(i.values()) for i in track]
    # The function returns a list of dictionaries in which I needed to convert yet again to a list of lists
    # The solution is not optimized since I coded in a hurry, but it generalizes to any set of coins


# Here are some examples:

print(makeChange([1, 5, 10, 25], 12))
track = []
# Every time the functions is called, track needs to be manually reset, hence the not optimized solution
print(makeChange([3, 6], 12))
