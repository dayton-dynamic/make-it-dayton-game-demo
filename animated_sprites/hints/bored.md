
# Short attention span blob (Hard)

What if the blob gets bored after moving toward the 
pointer for a few seconds, and quits?

*Hint:*

You'll need to keep track of how long it has been since 
the pointer moved.  Python's `time.time()` function can do 
it - it outputs the number of seconds in the "UNIX epoch", 
so if you call `time.time()` once, store that value in a 
variable, then call it again later, subtracting the new 
value from the old one shows how many seconds went by.

You'll need to add an `import` statement at the top of the 
file:

    import time 

Then, when the pointer is moved (do you see the 
`on_mouse_motion` method?), use `time.time()` to store that 
time in an "instance variable" - give it a name within `self`, 
like `self.mouse_moved_at`.

Now, before the blob actually moves, use `time.time()` again 
to see if it's been too long since the mouse moved - to see 
if it's gotten bored.  You'll need to use Python's `if` 
statement, which looks like 

    if (time.time() - self.mouse_moved_at < 3):
        print("I'm not bored yet")

The indentation is important!

Then save the file, stop the game, and run the program again.
