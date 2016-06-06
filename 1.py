# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list

def double_elemets_of_list(listofelements):
    if type(listofelements) == list:
        newlist = []
        for elements in listofelements:
            newlist.append(elements)
            newlist.append(elements)
        return newlist
    else:
        return 'This is not a list!'
