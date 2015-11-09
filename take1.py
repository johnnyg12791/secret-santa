import random



def main():
    name_families = {"John": 1, "David": 1, "Chris": 2, "Brian": 2, "Charlotte":3, "Victoria":3, "Liz":1, "Mike":2, "Tyler":3}
    #matches = PerformSecretSanta(name_families)
    matches = SecretSantaWrapper(name_families)
    print matches

    name_families = {"John": 1, "Brian" : 2, "Victoria" : 3, "David": 1}
    print SecretSantaWrapper(name_families)

    name_families = {"John": 1, "David": 1, "Chris": 2}
    print SecretSantaWrapper(name_families)


'''
Read names and families
'''



'''
Sets up the things we need for recursion
'''
def SecretSantaWrapper(name_families):
    matches = recursiveSecretSanta(name_families, name_families.keys(), {})
    if matches == None:
        print "Sorry, with that combination no matchings are possible"
    return matches

'''
Does recursion, Shuffles gifters so we get different results each time
'''
def recursiveSecretSanta(name_families, gifters, matches):
    #random.shuffle(gifters)
    #Base case
    if len(matches) == len(name_families):
        print "Good"
        return True
    #else...Recursive case
    for gifter in gifters:
        possible_giftees = getGiftees(gifter, name_families, matches)
        if len(possible_giftees) > 0:
            for person in possible_giftees:
                matches[gifter] = person
                gifters.remove(gifter)
                #Must go deeper
                if(recursiveSecretSanta(name_families, gifters, matches)):
                    return matches
                else:
                    print "Bad"
                    gifters.append(gifter)
                    del matches[gifter]
        else:
            print "else"
            return None #Same as False


'''
Removes people who will be gifted
'''
def getGiftees(gifter, name_families, matches):
    giftees = name_families.keys()
    #Remove people in the same family, will include gifter
    for name, family in name_families.items():
        if name_families[gifter] == family:
            giftees.remove(name)
    #Also remove people already matched
    if bool(matches):
        for reciever in matches.values():
            if reciever in giftees: giftees.remove(reciever)
    return giftees


#The "not so smart method" that only works if the matching is possible..
def PerformSecretSanta(name_families):
    matches = {}
    redo = False
    while True:
        for name in name_families.keys():
            possible_giftees = getGiftees(name, name_families, matches)
            print possible_giftees
            if len(possible_giftees) > 0:
                matches[name] = random.choice(possible_giftees)
            else:
                redo = True
        if redo:
            redo = False
            matches = {}
        else:
            break
    return matches





if __name__ == "__main__":
    main()