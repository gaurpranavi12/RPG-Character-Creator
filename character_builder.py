#This code aims to display: 
#Bob               (name)
#STR ●●●●○○○○○○    (STR --> Strength)
#INT ●●○○○○○○○○    (INT --> Intelligence)
#CHA ●○○○○○○○○○    (CHA --> Charisma)

full_dot = '●' #Use a variable to store ● and ○ so that it is easier to code later on.
empty_dot = '○'

#define(create) a function with 4 parameters(variables) that can only be used in the function
def create_character(name, strength, intelligence, charisma):

    if not isinstance(name, str):       #The name should be a string(text/words)
        return 'The character name should be a string'

    elif name == '':                    #A name has to be given
        return 'The character should have a name'

    elif len(name) > 10:                #The name cannot be too long/more than 10 characters
        return 'The character name is too long'

    elif ' ' in name:                   #The character name cannot have any spaces (it has to be connected/ 1 name)
        return 'The character name should not contain spaces'
    
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'       #The characteristics(strength, intelligence, charisma) can only be integers(number)

    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'        #The numbers assigned to the characteristics should be 1 or more

    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'        #The numbers assigned to the characteristics should be 4 or less

    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'        #The total sum of numbers assigned to the characteristics should equal to 7

    return(
    f'{name}\n'               #first line should have the name
    f'STR {strength * full_dot + (10 - strength) * empty_dot}\n'                     #second line should show the strength
    f'INT {intelligence * full_dot + (10 - intelligence) * empty_dot}\n'                    #third line should show the intelligence
    f'CHA {charisma * full_dot + (10 - charisma) * empty_dot}'                    #fourth line should show the charisma
    )
    
print(create_character('Bob', 4, 2, 1))                      #this runs and prints the code
