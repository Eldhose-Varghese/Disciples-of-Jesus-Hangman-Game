import random as rd
import art
import hangman_stages

def hints(display,to_find,chances_left):
  print(display)
  print(f'\nYou have to find {to_find} letters and you have {chances_left} chances left')
names_list = [
                 "Peter",
                 "Andrew",
                 "John",
                 "Philip",
                 "Bartholomew",
                 "Matthew",
                 "Thomas",
                 "James",
                 "Jude",
                 "Simon"
             ]
chosen_name = rd.choice(names_list).lower()
chosen_name_list=list(chosen_name)
display = list(len(chosen_name)*("_"))
count=7
wrong_choice=0
flag=0
end_of_game=False
print(art.hangman_art)
while end_of_game==False:
  if count==0 or (display)==(chosen_name_list):
    end_of_game=True
  else:
    hints(display,display.count("_"),count)
    count=count-1
    guess=input("\nEnter a character : ")
    for i in range(len(chosen_name_list)):
      if chosen_name_list[i].lower()==guess.lower():
        display[i]=guess
        flag=0
        break
      else:
        flag=1
    if flag==1:
      wrong_choice=wrong_choice+1
      print(hangman_stages.hangman_stage[wrong_choice])
      
if display==chosen_name_list:
  print("You Won !!!")
  print(f'The actual word is {chosen_name_list}')
else:
  print("You Lost !!!")
  print(hangman_stages.hangman_stage[6])
  print(f'The actual word is {chosen_name_list}')
    
  
    
  
  

