import os
import sys, time 

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def questiontime(questions):
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct! Next Round!")
            input()
            os.system('cls||clear')
        else:
            print("Unfortunately that is incorrect. Game Over")
            input()
            exit()
questiontime(questions[1:5])

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print("""
888              888    d8b              888b     d888          888                    888888b.                     888      
888              888    88P              8888b   d8888          888                    888  "88b                    888      
888              888    8P               88888b.d88888          888                    888  .88P                    888      
888      .d88b.  888888 "  .d8888b       888Y88888P888  8888b.  888  888  .d88b.       8888888K.   8888b.  88888b.  888  888 
888     d8P  Y8b 888       88K           888 Y888P 888     "88b 888 .88P d8P  Y8b      888  "Y88b     "88b 888 "88b 888 .88P 
888     88888888 888       "Y8888b.      888  Y8P  888 .d888888 888888K  88888888      888    888 .d888888 888  888 888888K  
888     Y8b.     Y88b.          X88      888   "   888 888  888 888 "88b Y8b.          888   d88P 888  888 888  888 888 "88b 
88888888 "Y8888   "Y888     88888P'      888       888 "Y888888 888  888  "Y8888       8888888P"  "Y888888 888  888 888  888 
                                                                                                                             
                                                                                                                             
                                                                                                                             
""")

print_slow("Press Enter to Start...")
input()

os.system('cls||clear')

print("""
                                             .~:..                              
                                              YB5JGPY.                          
                                :~J5GB###&&&&#B#B5YG&@^                         
                            .7B@@@@&BBGGB##&@@@@&##@@&:                         
                           :@@&&@@@@@@&&#&&@@@@@@@&#?                           ============================================
                           ?@@BP#&J~77?5B&&&&P^:!?PJ                         /                                                 
                           .@@&B#@!    GGGGG#J  :JG&.                       /       Hello! Welcome to Let's Make Bank! 
                            G@@@@#      .~^.   ~ :.~G:                     /                                                        
            .^:.            P!:~BY      :#~    !?#^..7J:                 <<     The aim of the game is to answer questions          
           .Y. !~          :G  !.     .   .:7^.  ...:7:7Y    .:^:.         \    correctly for the chance to win a lot of money! 
           .Y  J.           ?7:7:   ^B?.    ^~..    .?. ^G ^GG#GBGG~        \       I'm you're host, Frank, and you are? 
         ..?!  !^            :@B.   .5:::::. .:^~^~^:    &^&BGG5G5GB~        \\
     :~^!:^P    :J            #B     7&P7^:......:7     ^G^&BBG5BPBB7           =============================================
  .Y7~:!: .?~.  .&J           ~B      J@&&&#B??Y^:.     G~ ?#&G#&#G#5!!?.       
  G~.:.~ ..     P5G7           P.      ^GPYYPJ757. :   75    :?#?!Y5.^7?7!      
  Y5:::::^:JB&~?J!!#^         .Y#        .^~~~~^: .5  !5      !~ .  P7 .~GJ     
   .:...  ^#B#57!7!?#.     .7PGJP#:               ^J 7J        Y^.~~G5J?. ^5    
           ?G7!!777!JB::!YGGY7!!!GG7^            :!^BB         G&?  .Y&?:?PB    
            ^BY!!!!!!?BGYJ7!!!!!!!G5?J?7!!~:  ..??!BB5P.      PP75:.YJ?##Y75G~  
              5G7!!77!!7!!7!!!77!!?G5GPG^::~P5~JP^.~G~?G!    P5!!7JP@B? .5BP#Y  
               ^G57!!!!!!!!7JGB?7YJJ5JJB~:~7P&?PP!^?P?!!YP!!GY!!!!!7JGP   .^.   
                 ~5PYJJJYY5J^PB!PB5BBP7?55BBBP!GGG55?B!7!7PP7!777!!YP~          
                   .:~!!~:   5P!7?JY5PP7!77!?YB&J77!PP!7!!!!!7!!75G7            
                             GY!!!!!!!!77!!7!!?GY!!!#P?!!!!!!!?PG?              
                             GJ!777777777777!GBGJ~~?P:J5YJJY5PY~                
                             B7!777777777777!JY#7!~#^   .^^:.                   
                            .&7!777777777777PGYG!!JB                            
                            .&?7!!!!!77777!7GPB?!!#~                            
                             :!YG5J?7!!!!!!!!JP775B                             
                                #5PGGGPPPPPPP##Y?!.                             
                                B7!!77?YJ?JJ?G5                                 
                                B7!!!7#&J!!!JG                                  
                                B7!!!7&#7!!?B.                                  
                                B7!!!Y#G!!!B^                                   
                               .#J?77GGP!7GJ                                    
                            :JB@@@@@@BB@@@@@BJ^                                 
                         :G&@@@&#B&#G:~G##B&@@@@B7                              
""")

print_slow("Enter name: ")
your_name = input("")

os.system('cls||clear')

print(f"""
                                             .~:..                              
                                              YB5JGPY.                          
                                :~J5GB###&&&&#B#B5YG&@^                         
                            .7B@@@@&BBGGB##&@@@@&##@@&:                         
                           :@@&&@@@@@@&&#&&@@@@@@@&#?                           ============================================
                           ?@@BP#&J~77?5B&&&&P^:!?PJ                         /                                                 
                           .@@&B#@!    GGGGG#J  :JG&.                       /              G-Day, {your_name}! 
                            G@@@@#      .~^.   ~ :.~G:                     /      For each round, we'll pick a different                                                  
            .^:.            P!:~BY      :#~    !?#^..7J:                 <<      category. Answer correctly and you're still        
           .Y. !~          :G  !.     .   .:7^.  ...:7:7Y    .:^:.         \     in the game. If you're wrong though, 
           .Y  J.           ?7:7:   ^B?.    ^~..    .?. ^G ^GG#GBGG~        \         it's Game Over... here we go!
         ..?!  !^            :@B.   .5:::::. .:^~^~^:    &^&BGG5G5GB~        \\
     :~^!:^P    :J            #B     7&P7^:......:7     ^G^&BBG5BPBB7           =============================================
  .Y7~:!: .?~.  .&J           ~B      J@&&&#B??Y^:.     G~ ?#&G#&#G#5!!?.       
  G~.:.~ ..     P5G7           P.      ^GPYYPJ757. :   75    :?#?!Y5.^7?7!      
  Y5:::::^:JB&~?J!!#^         .Y#        .^~~~~^: .5  !5      !~ .  P7 .~GJ     
   .:...  ^#B#57!7!?#.     .7PGJP#:               ^J 7J        Y^.~~G5J?. ^5    
           ?G7!!777!JB::!YGGY7!!!GG7^            :!^BB         G&?  .Y&?:?PB    
            ^BY!!!!!!?BGYJ7!!!!!!!G5?J?7!!~:  ..??!BB5P.      PP75:.YJ?##Y75G~  
              5G7!!77!!7!!7!!!77!!?G5GPG^::~P5~JP^.~G~?G!    P5!!7JP@B? .5BP#Y  
               ^G57!!!!!!!!7JGB?7YJJ5JJB~:~7P&?PP!^?P?!!YP!!GY!!!!!7JGP   .^.   
                 ~5PYJJJYY5J^PB!PB5BBP7?55BBBP!GGG55?B!7!7PP7!777!!YP~          
                   .:~!!~:   5P!7?JY5PP7!77!?YB&J77!PP!7!!!!!7!!75G7            
                             GY!!!!!!!!77!!7!!?GY!!!#P?!!!!!!!?PG?              
                             GJ!777777777777!GBGJ~~?P:J5YJJY5PY~                
                             B7!777777777777!JY#7!~#^   .^^:.                   
                            .&7!777777777777PGYG!!JB                            
                            .&?7!!!!!77777!7GPB?!!#~                            
                             :!YG5J?7!!!!!!!!JP775B                             
                                #5PGGGPPPPPPP##Y?!.                             
                                B7!!77?YJ?JJ?G5                                 
                                B7!!!7#&J!!!JG                                  
                                B7!!!7&#7!!?B.                                  
                                B7!!!Y#G!!!B^                                   
                               .#J?77GGP!7GJ                                    
                            :JB@@@@@@BB@@@@@BJ^                                 
                         :G&@@@&#B&#G:~G##B&@@@@B7                              
""")
input()
os.system('cls||clear')

print("""
                                             .~:..                              
                                              YB5JGPY.                          
                                :~J5GB###&&&&#B#B5YG&@^                         
                            .7B@@@@&BBGGB##&@@@@&##@@&:                         
                           :@@&&@@@@@@&&#&&@@@@@@@&#?                           ============================================
                           ?@@BP#&J~77?5B&&&&P^:!?PJ                         /                                                 
                           .@@&B#@!    GGGGG#J  :JG&.                       /          Round 1: Pick your Category: 
                            G@@@@#      .~^.   ~ :.~G:                     /      Movies / TV / Music / Games / Sports / Books                                                  
            .^:.            P!:~BY      :#~    !?#^..7J:                 <<          Answer all correct in each category     
           .Y. !~          :G  !.     .   .:7^.  ...:7:7Y    .:^:.         \              for a total of $200k!
           .Y  J.           ?7:7:   ^B?.    ^~..    .?. ^G ^GG#GBGG~        \            type none to Exit Game
         ..?!  !^            :@B.   .5:::::. .:^~^~^:    &^&BGG5G5GB~        \\
     :~^!:^P    :J            #B     7&P7^:......:7     ^G^&BBG5BPBB7           =============================================
  .Y7~:!: .?~.  .&J           ~B      J@&&&#B??Y^:.     G~ ?#&G#&#G#5!!?.       
  G~.:.~ ..     P5G7           P.      ^GPYYPJ757. :   75    :?#?!Y5.^7?7!      
  Y5:::::^:JB&~?J!!#^         .Y#        .^~~~~^: .5  !5      !~ .  P7 .~GJ     
   .:...  ^#B#57!7!?#.     .7PGJP#:               ^J 7J        Y^.~~G5J?. ^5    
           ?G7!!777!JB::!YGGY7!!!GG7^            :!^BB         G&?  .Y&?:?PB    
            ^BY!!!!!!?BGYJ7!!!!!!!G5?J?7!!~:  ..??!BB5P.      PP75:.YJ?##Y75G~  
              5G7!!77!!7!!7!!!77!!?G5GPG^::~P5~JP^.~G~?G!    P5!!7JP@B? .5BP#Y  
               ^G57!!!!!!!!7JGB?7YJJ5JJB~:~7P&?PP!^?P?!!YP!!GY!!!!!7JGP   .^.   
                 ~5PYJJJYY5J^PB!PB5BBP7?55BBBP!GGG55?B!7!7PP7!777!!YP~          
                   .:~!!~:   5P!7?JY5PP7!77!?YB&J77!PP!7!!!!!7!!75G7            
                             GY!!!!!!!!77!!7!!?GY!!!#P?!!!!!!!?PG?              
                             GJ!777777777777!GBGJ~~?P:J5YJJY5PY~                
                             B7!777777777777!JY#7!~#^   .^^:.                   
                            .&7!777777777777PGYG!!JB                            
                            .&?7!!!!!77777!7GPB?!!#~                            
                             :!YG5J?7!!!!!!!!JP775B                             
                                #5PGGGPPPPPPP##Y?!.                             
                                B7!!77?YJ?JJ?G5                                 
                                B7!!!7#&J!!!JG                                  
                                B7!!!7&#7!!?B.                                  
                                B7!!!Y#G!!!B^                                   
                               .#J?77GGP!7GJ                                    
                            :JB@@@@@@BB@@@@@BJ^                                 
                         :G&@@@&#B&#G:~G##B&@@@@B7                              
""")

user_decision = input("What category are we starting with today?: ")

# import game_questions
# import movie_questions
from movie_questions import movietime, questions
from game_questions import gametime, questions
from tv_questions import tvtime, questions

while user_decision != "none":
    if (user_decision.lower() == "games"):
        questiontime(questions[0:5])
    if (user_decision.lower() == "movies"):
        movietime(questions[0:5])
    if (user_decision.lower() == "tv"):
        tvtime(questions[0:5])
    else:
        exit()
    # if (user_decision.lower() == "None"):
    #     continue
    
 
        

print(f"Thanks for playing, {your_name}!")


