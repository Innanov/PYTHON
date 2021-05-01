#Hangman Game
#By INNAN Nouhaila 

#steps: 
#pick a word
#have a variable called wrong_count
#create list of letters from the world
#create list of underscores __

#LOOP START
#guess a letter using input 
 #guessed correctly
  #assign the underscore to user's letter
 #guess incorrectly
  #increment wrong_count

#check if we won
 #no more underscores in the underscores
#chek if we lost
 #if wrong__count == 6: we lose
#LOOP END

#guess: i 

# 0 1 2 3 4 5
# c o d i n g
# _ _ _ _ _ _

word = "coding"
wrong_count = 0 
underscores = ['_']*len(word)
while True: 
  print(underscores)
  letter = input("What is your letter ?")
  if letter not in word:
    #you guess WRONG
    wrong_count = wrong_count + 1 
  else:
    #you guess CORRECT!
    for i in range(len(word)):
      if word[i] == letter:
        underscores[i] = letter

  if '_' not in underscores:
    print("YOU WON!")
    break
  if wrong_count == 6:
    print("YOU LOST!")
    break
