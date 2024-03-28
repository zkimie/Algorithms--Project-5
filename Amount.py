#Date: 02/15/2024
#Course: Algorithms


def amount(A, S):
    """Given a collection of amount values and sum, we find all the unique combinations in A where
     the amount values sum up to S. We then return these combinations in the form of a list.
     """
    A.sort() #"A" refers to the amount values and we need to make sure that they are in ascending order per instructions

    combo = [] #We need to make an empty list so that we store the combinations that equal the sum.

    def backtrack(current, remaining, start):
        """This function serves to backtrack and makes sure that the values/combinations equal the sum that is given
        to us.
        """
        # If the target sum is reached and the combination is not already in the result list, add it to the result
        if remaining == 0 and current not in combo: #if we reach 0 that means this is a combo and we make sure there is no duplicate
            combo.append(current)
            return #and we finished and we continue with the next


        for i in range(start, len(A)): #for when we didnt hit 0, starting from the start over the amounts in our sorted list

            if A[i] > remaining: #if the amount is greater than our remaining sum that means we went over and need to go back
                break #and we dont want to be in this loop
            backtrack(current + [A[i]], remaining - A[i], i + 1) #add the current amount to our current combination
            #our current amount, remaining sum, moving our index to the next amount
    backtrack([], S, 0) #generating all the combinations

    return combo

A = [11, 1, 3, 2, 6, 1, 5]
S = 8
result = amount(A, S)
print(result)
