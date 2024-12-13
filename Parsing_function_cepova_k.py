# Another John Deere added to check the function properly for username recurrence
# Jay Z and Meghan Fox added to test the function's ability to process short names

data = {
    "students":["Adam Levine", "Monica Muller", "John Deere", "John Deere", "John Deere","Jay Z", "Jay Z", "Meghan Fox"],
    "active":[True, False, True, True, True, True, True, True]
}

def create_usernames(data):
    names = data["students"] #creating list of only students
    states = data["active"] #creating list of states

    states_new = []  # list of states containing only active
    names_new = []  # list of students containing only active

    #filtering active students
    for i in range(len(states)):
        if states[i] == True:
            states_new.append(states[i])
            names_new.append(names[i])

    #creating unique usernames
    user_names = [] #list of user names after first modification

    for i in range(len(names_new)):

        user_names.append(names_new[i].split()[1][0:5].lower()+names_new[i].split()[0][0:3].lower())
        #takes firts 5 characters of last name and adds first 3 characters of first name

    user_names_final=[] #creates a list for final UNIQUE usernames

    for i in range(len(user_names)): #eliminates reccuring usernames
        j=0 #changing the last character of the name to the number "j" until original username is created
        user_name=user_names[i]
        while user_names_final.count(user_name) > 0: #checks if the name recurs
            j = j + 1
            user_name= user_name[0:len(user_name) - 1] + str(j) #taking out the last character and replacing it with "j"
        user_names_final.append(user_name) # adding unique username to the final list

    data["usernames"]=user_names_final #adds a new key "usernames" and its corresponding values
    data["students"] = names_new
    data["active"] = states_new

    transformed_data=data

    return transformed_data

print(create_usernames(data))
