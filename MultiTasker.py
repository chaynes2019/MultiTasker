goals = dict()

with open("Goals.csv", 'r') as f:
    lines = f.readlines()
    
    for k in range(len(lines)):
        lines[k] = lines[k].replace('\n', '')

    data = lines[0].split(',')
    print(data)
    goalData = lines[1:]
    print(goalData)

    for goal in goalData:
        goalElements = goal.split(',')
        goalName = goalElements[0]
        #print(goalName)
        
        #Create dictionary mapping each of the elements of the goal to their appropriate
        #name, given by one of the CSV headers
        goalDict = dict()

        for k, datum in enumerate(data):
            #Populate dictionary, mapping each data type - given by the CSV headers - to
            #the appropriate goal element
            goalDict[datum] = goalElements[k]
            #print(goalDict)
        
        #Add goal - in dictionary form - to the dictionary of goals, using name as the key
        goals[goalName] = goalDict
    
    print(goals)
