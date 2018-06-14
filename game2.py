EASY_TEMPLATE = '''The current paragraph reads as such:
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

MEDIUM_TEMPLATE = '''A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to retrun.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.'''

HARD_TEMPLATE = '''When you create a __1__, certain __2__s are automatically
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

EASY_ANS = ["world",  "python", "print", "html"]
MEDIUM_ANS = ["function", "argument", "None", "list"]
HARD_ANS = ["class","method", "__init__", "instance", "__repr__", "__add__", "__sub__", "__lt__", "__gt__", "__eq__"]

BLANKS = ["__1__" , "__2__", "__3__", "__4__", "__5__","__6__", "__7__","__8__","__9__","__10__"]

WELCOME_MSG = '''Welcome to the madlibs game.'''
PROMPT = '''Please select a game difficulty by typing it in. Possible choices include easy, medium, and hard.'''
WARN_MSG = '''That's not an option!'''


def play_game():
    games = {
        'easy': {
            'template': EASY_TEMPLATE,
            'answer': EASY_ANS,
            'max_tries': 5
        },
        'medium': {
            'template': MEDIUM_TEMPLATE,
            'answer': MEDIUM_ANS,
            'max_tries': 4
        },
        'hard': {
            'template': HARD_TEMPLATE,
            'answer': HARD_ANS,
            'max_tries': 3
        },
    }

    print WELCOME_MSG
    while True:
        choice = raw_input(PROMPT + '\n')
        if choice in games.keys():
            template = games[choice]['template']
            max_tries = games[choice]['max_tries']
            answer = games[choice]['answer']
            
            try_count = 0
            cur = 0
            while try_count < max_tries:
                print 'You have ' + str(max_tries - try_count) + ' lives left'

                ans = raw_input(template + '\n\n')
                if ans == answer[cur]:
                    template = template.replace(BLANKS[cur], ans)
                    cur += 1
                    if cur == len(answer):
                        print 'Won'
                        return
                else:
                    print 'wrong answer\n\n'
                    try_count += 1
            print 'Fail'
            return
        print WARN_MSG


if __name__ == '__main__':
    play_game()
