# Kyler Naef 696969
store = 'Gamestop' #Harcoded title of the store. This is given a value at compile time, therefore 'hard coded'
print('Welcome to ' + store + '\n') # String concatenation
videoGame = input('What video game would you like to purchase?\n') # Returns a string value and assigns it to video game
costOfVideoGame = input('What is the cost of the video game? ') #Returns a string value and assigns it to the variable
print('Video Game: ' + videoGame + '\n') #output the prev input

costOfVideoGameToFloat = float(costOfVideoGame) # We need to cast the string to a float (float means a decimal number)
actionFigure = input('What action figure would you like to purchase?\n')
costOfActionFigure = input('What is the cost of the action figure? ')
costOfActionFigureToFloat = float(costOfActionFigure) #Casts a string value to a float


print('Action Figure: ' + actionFigure + '\n') #output the prev input

subTotal = costOfVideoGameToFloat + costOfActionFigureToFloat
taxAmount = subTotal * .10

print('The subtotal is: ')
print("%.2F" % subTotal) # The weird thing (%.2F) sets the precision. What would be 9.000020321001 would become 9.00
print('\nThe tax due is: ')
print("%.2F" % taxAmount)