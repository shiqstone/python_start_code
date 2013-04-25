cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def findCity(themap, state):
    if state in themap:
        return themap[state]
    elif state == "all":
        print cities
        return "-------"
    else:
        return "Not found."

#ok pay attention!
cities['_find'] = findCity

while True:
    print "state?(Enter to quit)",
    state = raw_input(">")

    if not state:break

    #this line is the most important ever!
    cityFound = cities['_find'](cities,state)
    print cityFound
