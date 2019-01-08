#==========================================================================================#
#                                           PYTHON                                         # 
#                                        THE BASICS 2                                      #
#                                    Written By: Kirk Worley                               #
#==========================================================================================#
#                                           KEY TERMS                                      # 
#==========================================================================================#
#                                                                                          #
#   function    -   A repeatable set of instructions or code.                              # 
#   def         -   "Define", this is used to create a function.                           # 
#   call        -   This is a term that means "activate my function" or "run my function"  # 
#   arguments   -   Arguments are placed inside () when defining a function. Arguments     # 
#                   are used to add paramaters to a function.                              # 
#   local       -   Local variable, this is a variable that is only modified inside a      # 
#   variable        function.                                                              # 
#   return      -   Command that updates existing variables from a function.               # 
#   pass        -   A command that can be used to "do nothing" even when a command like    # 
#                   "return" is required.                                                  # 
#   reference   -   Using something inside a function, usually a variable.                 # 
#                                                                                          #
#==========================================================================================#
#                                           FUNCTIONS                                      # 
#==========================================================================================#
#                                                                                          # 
#   In this brief Python lesson, we'll be covering functions. Functions are essential to   # 
#   any programmer. They are essentially a code that can be repeated as many times as      # 
#   necessary. A function is preceded by the word "def" which stands for define. When you  # 
#   tell Python to define something, you are creating a set of instructions to be          # 
#   repeated at any time. This is called a function. Remember that a function is always    # 
#   preceded by the word "def" and followed by  parentheses and a colon "():".             # 
#   The parentheses are important because variables, or "arguments", can be given inside   # 
#   these, but we will discuss this later.                                                 # 
#                                                                                          #
#   This is an example of a function.                                                      # 
#                                                                                          #
#   def my_function():                                                                     # 
#       print "This is my function."                                                       # 
#                                                                                          #
#   This could be a function. To use a function whenever you want inside your code it is   # 
#   called "calling" your function. The way you call a function is to use its name in      #     
#   your code. A function on its own will not do anything. Below, create your own          # 
#   function name, and then run the code using "F5" or Run -> Run Module. Remember to      # 
#   leave the "():" at the end. Also remember, any time you have a colon, make sure the    # 
#   code is indented.                                                                      # 
#                                                                                          #
#-------------------------------------------COMPLETE THE CODE 1:---------------------------# 

##def <your function name>():
##    print "This is my function."

#-------------------------------------------END WORKSPACE, DO NOT TYPE BELOW THIS----------#
#                                                                                          #
#   If you ran the code, nothing should have happened. That's because we haven't called    # 
#   the function in the code. Calling a function means we are asking it to run our pre-    # 
#   defined instructions. To call a function, simply type its name into your code where    # 
#   you want it, including its () and any "arguments" if it needs them.                    # 
#                                                                                          #
#   Example:                                                                               #
#                                                                                          #
#   def my_function():                                                                     #
#       print "This is my function."                                                       #
#                                                                                          #
#   my_function()                                                                          # 
#                                                                                          #
#   This defines "My Function" and it also "calls" it. This would display in the shell     # 
#                                                                                          #
#   >>>                                                                                    #
#   This is my function.                                                                   #
#   >>>                                                                                    #
#                                                                                          #
#   We can have anything in our function that we want. However, we need to understand      #  
#   that variables inside functions are called "Local Variables". What does this mean?     # 
#   A local variable means that it is only counted or remembered inside that function.     # 
#   This means a variable that is modified inside a function will only stay modified       # 
#   for the function. Let's look at this in use; go ahead and run this code:               # 
#                                                                                          #
#-------------------------------------------FUNCTIONS EXAMPLE 1----------------------------#

##x = 3
##
##def example_function():
##    print "This is the example function. X is equal to 1."
##    x = 1
##    print x
##
##example_function()
##
##print x

#-------------------------------------------END WORKSPACE, DO NOT TYPE BELOW THIS----------#
#                                                                                          #
#   Woah! What happened? We see that we set x to 3 in the beginning, but our function      # 
#   sets x to 1 AFTER it. So x should be 1 right? Well, not quite. Because x is in the     # 
#   function, it is counted as a "local variable." Local variables are only manipulated    # 
#   within functions, even if we call the function after assigning the variable.           # 
#   Remember this important note: If you use a variable inside a function (reference it)   # 
#   BEFORE you have assigned it an actual value, you will get an error.                    # 
#                                                                                          #
#   Example:                                                                               # 
#                                                                                          #
#   def my_function():                                                                     # 
#       print x                                                                            #
#                                                                                          #
#   my_function()                                                                          #
#                                                                                          #
#   x = 5                                                                                  #
#                                                                                          #
#   Why won't this work? Well, inside our definition, we tell our function to print 'x'.   # 
#   Then we call our function, but we haven't actually given x a value yet. To fix this,   # 
#   we have to give x a value BEFORE calling our function. Placing the "x = 5" line        # 
#   ABOVE "my_function()" would fix this error. Because we have now given x a value first  # 
#   and THEN we call our function, which prints the value of x.                            # 
#                                                                                          #
#   This is how it should look:                                                            #
#                                                                                          #
#   def my_function():                                                                     #
#       print x                                                                            #
#                                                                                          #
#   x = 5                                                                                  #
#                                                                                          #
#   my_function()                                                                          # 
#                                                                                          #
#   This will fix the error we would have recieved.                                        # 
#   Now, how can we get our variable to be updated? What if we want our function to        # 
#   manipulate other variables like x forever?                                             # 
#                                                                                          #
#   Well, we cant necessarily do that without some major tweaking.                         #     
#   First off, we can look at something called the "return" command. The "return" command  # 
#   is a command that lets you return a value at a certain time, it usually                # 
#   is used to interpret an input from the user, and give a value back. Return             # 
#   gives a value back to what was initially called.                                       # 
#                                                                                          #
#   Let's look at our previous example. But let's tweak it a little bit.                   # 
#   We will add the variable 'x' as our "arguments" so we can modify that variable.        # 
#                                                                                          #
#-------------------------------------------FUNCTIONS EXAMPLE 2----------------------------#

##x = 0
##
##def example_function(x):
##    print "X = %d currently." % x
##    print "This is our example function."
##    print "We will add 1 to x."
##    x = x + 1
##    print "X = %d currently." % x
##    print "We will now return x."
##    return x
##
##x = example_function(x)
##
##print x

#-------------------------------------------END WORKSPACE, DO NOT TYPE BELOW THIS----------#
#                                                                                          #
#   Through that code above, we are able to perform a function of adding one to x, and     # 
#   then we reassign it by saying "x = example_function(x)" This changes x to the output   # 
#   from our function.                                                                     # 
#                                                                                          #
#   If you're still unsure of how a function works, here is a brief summary before you     # 
#   will be given space to create your own function.                                       # 
#                                                                                          #
#   Functions are a repeatable set of instructions to make your life easier.               # 
#   They can send back values to be interpreted.                                           # 
#   They can be given arguments to alter specific variables.                               # 
#   They are always preceded by the phrase "def".                                          # 
#   They are always followed by "(arguments if any):".                                     # 
#   The body of a function is always indented.                                             #     
#                                                                                          #
#   Using everything encompassed in this brief lesson, write your own function below.      # 
#   It can do anything you want it to. Print a statement, add something, whatever          # 
#   you choose. Just remember to put "def" first and follow it with the correct            # 
#   arguments if there are any, and a colon.                                               # 
#                                                                                          #
#-------------------------------------------COMPLETE THE CODE 2:---------------------------#
############################################################################################
#                           USE THE SPACE BELOW TO CREATE YOUR FUNCTION                    # 
############################################################################################



















############################################################################################
#                           CALL YOUR FUNCTION HERE                                        # 
############################################################################################

#example: <myfunction>():

#-------------------------------------------END WORKSPACE, DO NOT TYPE BELOW THIS----------#
#==========================================================================================#
#                                           END OF LESSON                                  # 
#==========================================================================================#
