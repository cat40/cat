# -*- coding: cp1252 -*-
import random
import time
import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Error.cfg')) as errfile:
    ErrMes = [line.rstrip('\n') for line in errfile] #figure out how to avoid stripping this more than once, to allow message"That does not compute" to be repeated about a dozen times on new lines.
UNumErr = len(ErrMes) - 1
##ErrNum = UNumErr
##ErrMes = [''] * (UNumErr + 1)
##
##for values in ErrMes:
##    ErrMes[ErrNum] = lines[ErrNum + 3]
##    ErrNum = ErrNum - 1
#Functions
def error(UnqErr):
    NumErr = random.randint(0, UNumErr)
    if time.strftime('%d') == '1' and time.strftime('%m') == '4':
        print('April Fools!')
    elif time.strftime('%d') == '25' and time.strftime('%m') == '12':
        print('Merry Christmas')
    elif ErrMes[NumErr] == "YOU DIDN'T SAY THE MAGIC WORD!":
        print('Error...and...')
        time.sleep(.5)
        for __ in range(100):
            print('YOU DIDN\'T SAY THE MAGIC WORD!')
            time.sleep(.1)
        print('')
        print(UnqErr)
    elif ErrMes[NumErr] == "Thank you, Republic Airlines": #Have it play audio
        print('''Thank you, you random user, for breaking my coding from afar.
I was opened for some graphing by a user (that's you),
But you gave me an error with a smile ‘con brio’.
Thank you, you random user, What a joy to a programmer you are!
What a zest you've added to pedestrian life,
It was boring to be graphing while the wild goose flies,
But the tedium was broken by your wonderful surprise,
When you broke up my coding from afar!.

Thank you, you random user, for treating my programming with care.
There can be no greater happiness for the programmer,
Than to find his program thus reduced to tatters.
Uh-oh, you random user, in the firmament of errors, you're a star,
For you treat each piece of coding like a child of your own,
When you come across an input line, it's hit with a stone,
May you waken every morning with a new broken bone,
Like you broke up my coding from afar!

Thank you, you random user, for splintering my coding from afar!
My encoding was so strong that nothing could go through it,
Way to go you user, only you could do it,
Crash bang, you random user, in the field of demolition, you'll go far!
For you took it as a challenge when I show you my face.
and you saw the user input lines all over the place,
May a team of mad flamenco dancers do to your face
What you did to my coding from afar!''')
        print('')
        print(UnqErr)
    elif ErrMes[NumErr] == 'Tom Lehrer':
        print('[All Tom Lehrer songs]')
    elif ErrMes[NumErr] == 'This progam will self destruct in 5 seconds':
        print('''This program will self destruct in 5 seconds''')
        print'5'
        time.sleep(1)
        print'4'
        time.sleep(1)
        print'3'
        time.sleep(1)
        print'2'
        time.sleep(1)
        print'1'
        time.sleep(1)
        print'Maybe six...'
        time.sleep(1)
        print'7?'
        time.sleep(1)
        sys.exit()
    else:
        print(ErrMes[NumErr] + ' -- ' + UnqErr)
