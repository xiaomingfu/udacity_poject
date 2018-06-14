#check whether the user's input is valid or not
welcome = '''welcome to the madlibs game.
Please select a game difficulty by typing it in Possible choices include easy, medium, and hard.'''
valid = ["easy", "medium", "hard"]
#user answer of choice of difficulty
warn = '''That's not an option! 
Please select a game difficulty by typing it in! Possible choices include easy, medium, and hard. '''

blank = ["__1__" , "__2__", "__3__", "__4__", "__5__","__6__", "__7__","__8__","__9__","__10__"]
#desplay fill_in_the_blank quiz
easy_quiz = '''The current paragraph reads as such:
A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.
It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.'''

medium_quiz = '''A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.'''

hard_quiz = '''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).'''

easy_quiz_answer = ["world",  "python", "print", "html"]
medium_quiz_answer = ["function", "argument", "None", "list"]
hard_quiz_answer = ["class","method", "__init__", "instance", "__repr__", "__add__", "__sub__", "__lt__", "__gt__", "__eq__"]
#prompt user to chose level, repeat till user chose one

def start_game():
    user_input = raw_input(welcome +"\n")            

    while user_input not in 'easy medium hard'.split():
        user_input = raw_input(warn +"\n")

    print "You've chosen " + user_input + "!"

    if user_input == "easy":
        play_game(easy_quiz, easy_quiz_answer, 5)
    elif user_input == "medium":
        play_game(medium_quiz, medium_quiz_answer, 4)
    elif user_input == "hard":
        play_game(hard_quiz, hard_quiz_answer, 3)

def play_game(quiz, quiz_answers, max_tries):
    print "The current paragraph reads as such:\n" + quiz
    print "You will get " + str(max_tries) + " guesses per problem"
    index = 0
    while index < len(quiz_answers):
        err_cnt = 0
        while True:
            ans = raw_input("What should be substituted in for " + blank[index] +"?\n") 
            if ans == quiz_answers[index]:
                print " Correct!"
                index += 1
                break    
            else:
                err_cnt += 1                
                if max_tries == err_cnt:
                    print "You failed. Game over!"
                    return
                print "That isn't the correct answer!  Let's try again; you have " + str(max_tries - err_cnt) + " trys left!"
    print "You won!"

start_game()