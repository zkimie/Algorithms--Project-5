#course:Algorithms
#Date: 02/15/2024


def feedDog(hunger_level, biscuit_size):
    """utilizes two parameters: being hunger_level and biscuit size to determine how many dogs we can satisfy"""
    hunger_level.sort() #we need to go ahead and sort in ascending order for both
    biscuit_size.sort()

    satisfied_dogs_count = 0  #need to make a 0 counter for how many dogs are satisfied so we can keep track
    #we have the pointer for both our hunger level and biscuit size array
    i = 0 #hunger level pointer
    j = 0 #biscuit size pointer

    while i < len(hunger_level) and j < len(biscuit_size): #when they are still within the array bounds between lenght of our two parammeters
        if hunger_level[i] <= biscuit_size[j]: #if the the hunger level is less than the biscuit size then dog is satisfied
            satisfied_dogs_count += 1 #increase dog counter
            i += 1  #so then we move to the next dog's hunger level
        j += 1 #and we move the next biscuit size

    return satisfied_dogs_count #return our satisfied dog count

#Example 1
hunger_level1 = [1, 2, 3]
biscuit_size1 = [1, 1]
print(feedDog(hunger_level1, biscuit_size1))  # Output: 1

#Example 2
hunger_level2 = [1, 2]
biscuit_size2 = [1, 2, 3]
print(feedDog(hunger_level2, biscuit_size2))  # Output: 2
