
# Shortsighted blob (Medium)

What if the blob only seeks the pointer when it's 
close enough?

*Hint:*

The `intent_vector` describes the direction and distnace 
from the blob to the pointer.  It has a `length` attribute - 
that is, you can find out how far the blob and pointer are 
apart with 

    intent_vector.length 

The game window is about 4 units wide altogether.

So how could you keep the blob from moving if the pointer 
is too far away?  You'll probably use Python's `if` 
statement, which looks like 

    if intent_vector.length < 2:
        print('It is not very far away')
        print('I can almost smell it')

The indentation is important!

Can you adapt that to make sure the blob only swivels 
and moves when the `intent_vector` is short?


Then save the file, stop the game, and run the program again.
