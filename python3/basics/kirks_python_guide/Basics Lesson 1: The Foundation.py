#==========================================================================================#
#                                           PYTHON                                         #
#                                        GENERAL NOTES                                     #
#                                    Written By: Kirk Worley                               #
#==========================================================================================#
#                                                                                          #
#                           Welcome to a general overview Python.                          #
#   This section of notes will teach you the basics of Python and anything you may want    #
#   to know. This is simply a general overview of a few key terms, concepts and commands.  #
#   It may not cover everything you want to know, but my objective is to provide everyone  #
#   with a basic understanding of how Python works, and the basics on which you can use it #
#   to your advantage!                                                                     #
#                                                                                          #
#==========================================================================================#
#                                       THE BASICS                                         #
#==========================================================================================#
#                                                                                          #
#   Here we will start with some basics. In this section, we're going to cover some        #
#   of the simple things in Python, that can help you understand the foundation of         #
#   Python programming.                                                                    #
#                                                                                          #
#   Contents of "THE BASICS":                                                              #
#   - Key Words                                                                            #
#   - White Space                                                                          #
#   - Comments                                                                             #
#   - Variables                                                                            #
#   - Booleans                                                                             #
#   - Operators                                                                            #
#   - Loops                                                                                #
#                                                                                          #
#==========================================================================================#
#                                       KEY TERMS/WORDS                                    #
#==========================================================================================#
#                                                                                          #
#   If we want to begin to learn Python, we're going to need to know some of the key       #
#   words or terms used when talking about Python. This as known as the "language" or      #
#   "semantics", which essentially means: "What do these terms mean?"                      #
#   Well, good question. Let's start off with some key terms and words you'll need to      #
#   know, in order to navigate Python. Keep in mind, we are mostly if not excluding        #
#   VPython completely, and mainly sticking to Python in and of itself.                    #
#                                                                                          #
#   Key Word/Term   --  Symbol  --  Meaning                                                #
#   White Space     --          --  The amount of space from the edge to your code.        #
#   Comment         --    #     --  Ignore what comes after this symbol.                   #
#   Variable        --   N/A    --  A "Variable" that can be used to store information.    #
#   Boolean         --   N/A    --  A "Boolean" can be True or False.                      #
#   Str (String)    --   ""     --  A "String" is anything in quotes. (' or ")             #
#   Int (Integer)   --   1,2..  --  An "Integer" is a whole number.                        #
#   Float           --   1.4..  --  A "Float" is any number with a decimal.                #
#   Condition       --  various --  A "Condition" is a condition for x to be checked.      #
#   Module          --   N/A    --  A "Module" is a package of code with a specific use.   #
#   Package         --   N/A    --  A "Package" usually means a completed (Python) code.   #
#   Import          --  import  --  "Import" brings other modules into your code.          #
#   Operators       --  various --  Operators do many things to Booleans and Variables.    #
#   def             --   def    --  "def" starts a function. It means "define".            #
#   Function        --  various --  A "Function" is a repeatable code.                     #
#   Arguments       --    ()    --  Arguments are in () and are "variables" for functions. #
#   if              --    if    --  An "if" statement checks if something is true/false.   #
#   and             --   and    --  Check if more than one element is true.                #
#   Loop            --  various --  A "Loop" is repeated until something is satisfied.     #
#   Print           --   print  --  "Print" displays something in the console.             #
#                                                                                          #
#   While there are many, many more terms I could show you, these are a few very           #
#   important ones you will hear a lot, and use a lot. I recommend getting used to these   #
#   terms and key words.                                                                   #
#                                                                                          #
#   Now, let's get a bit more in depth to these key terms. These sections will be          #
#   marked with a a large header, and are in no particular order. While excersises are     #
#   indicated with a dashed line break.                                                    #
#                                                                                          #
#==========================================================================================#
#                                       WHITE SPACE                                        #
#==========================================================================================#
#                                                                                          #
#   "White Space" refers to the distance from the edge of the program. White Space is one  #
#   of the most common source of errors. Every time you create a new body of code, a tab   #
#   (4 spaces) is requied to keep your code in the body. Every time you use a colon,       #
#   you are creating a new body of code, and thus should another indent to subsequent      #
#   lines that you wish to be included inside the body of said code.                       #
#                                                                                          #
#==========================================================================================#
#                                       COMMENTING                                         #
#==========================================================================================#
#                                                                                          #
#   "Why is this text in red?" You may ask. Well, the simple answer to that is:            #
#   It's a comment!                                                                        #
#                                                                                          #
#   But what's a comment?                                                                  #
#                                                                                          #
#   Well, a comment is a line of code that is preceded by an octothorpe, or "#" symbol.    #
#   It is a line, or part of a line of code that Python doesn't read as part of the        #
#   program.                                                                               #
#   This can be at the beginning, or the end of your line of code. However, putting a      #
#   comment in the middle, will result in anything after the "#" symbol will not be read   #
#   as code.                                                                               #
#                                                                                          #
#   There are also quick commands for "commenting out" multiple lines of code. "Commenting #
#   out" a line or multiple lines means to simply ignore them by placing "#" or "##" at    #
#   the beginning of those lines. This command on Windows is Alt+3 while highlighting      #
#   an area you want to be ignored. Check Format -> Comment Out Region for your            #
#   particular operating system's command.                                                 #
#   Let's try it real quick. See if you can fix the problem below.                         #
#                                                                                          #
#---------------------------------------COMMENTS PRACTICE----------------------------------#

Woah! This line of text should not be here.

#---------------------------------------END COMMENTS PRACTICE------------------------------#
#                                                                                          #
#   Woah! If we were to run our code, we would get an error! That line of text shouldn't   #
#   be there! You know what to do!                                                         #
#                                                                                          #
#   If you put a "#" in front of the word "this", you should see the following:            #
#                                                                                          #
#------------------------------------------------------------------------------------------#
#this line of text should not be here.                                                     #
#------------------------------------------------------------------------------------------#
#                                                                                          #
#   If not, fix it now. Remember comments can be used as notes to yourself, or anyone      #
#   else viewing your code. Or just simple reminders or placeholders. Lastly, remember     #
#   you can do this to multiple lines using your system's "Comment Out" function. See:     #
#   Format -> Comment Out for the shortcut.                                                #
#                                                                                          #
#   Congrats! You've taken the first step into the world of Python. Ready for the next?    #
#   Throughout these notes, there may be tests or examples you can interact with by        #
#   running the code, these usually need to be "Un Commented" to work. They will be        #
#   marked with "##" in front of the lines of code. Along with a dashed line break,        #
#   naming the exercise. Be sure to remove the two "#" symbols, and follow instructions.   #
#   When moving on to a different exercise, don't forget to put the "#" symbols back,      #
#   to make sure no unwanted code is read. Unless of course, you want it to be.            #
#                                                                                          #
#==========================================================================================#
#                                       VARIABLES                                          #
#==========================================================================================#
#                                                                                          #
#   For this next part, we will learn about variables.                                     #
#   Variables are just like what they are in math, except a little more versatile.         #
#   An important note about variables, is they must be defined or assigned first before    #
#   being used anywhere in your code. If a variable is 'referenced' that is, used in       #
#   some way before you have assigned it or created it, you will recieve an error.         #
#   Variable names are in black text. Like this. After you remove the comments, navigate   #
#   to "Run" at the top, and select "Run Module" or press [F5]. Once it has displayed      #
#   our test variable, go ahead and close the "Python Shell" if you want to.               #
#                                                                                          #
#---------------------------------------VARIABLE EXAMPLE-----------------------------------#

## Remove these comments.
#test = 1
#print test
#test2 = 573863852L
#print test2
## Remove these comments.

#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   Our variable name is "test" and we have told Python it is equal to 1. Test2 is set to  #
#   a large number, so we add L at the end of it, denoting a "long" number.                #
#   We'll get into the different things we can do to a variable later, but for now, let's  #
#   see what we can do with variables.                                                     #
#   Variables in and of themselves are very useful to coding! They can hold a value, as    #
#   well as strings, floats, etc. You can even make them into lists! More on that later.   #
#   Here, create your own variable with a name like "my_variable" or "var1", and let's     #
#   assign it to 4, which is an "Integer" or a whole number. Remember that variable names  #
#   can't include spaces, so use an underscore instead if you have to.                     #
#                                                                                          #
#---------------------------------------TYPE YOUR VARIABLE HERE----------------------------#



#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   Great! Now, remember your variable, as we are going to use it in just a moment.        #
#   Did you know Python is good at math? It can add (+), subtract (-), multiply (*) and    #
#   divide (/). Let's check some basic code first.                                         #
#                                                                                          #
#   First let's look at some "Comparators."                                                #
#                                                                                          #
#   Comparators do as the name implies, they compare. This can be variables, statements,   #
#   floats, booleans, strings, etc. While some only work with numbers, a few can be        #
#   almost universal, and work with anything.                                              #
#   The types of comparators you should be familiar with are:                              #
#                                                                                          #
#   Symbol      --      Meaning                                                            #
#   ==          --      Equal To                                                           #
#   >           --      Greater Than                                                       #
#   <           --      Less Than                                                          #
#   >=          --      Greater Than or Equal To                                           #
#   <=          --      Less Than or Equal To                                              #
#   !=          --      Not Equal To                                                       #
#                                                                                          #
#   These symbols will help you when checking variables.                                   #
#   Now, let's fill in this code, and understand what it is doing. Remember to remove      #
#   the comment marks from it. Do not do anything after filling in <your variable here>.   #
#                                                                                          #
#---------------------------------------COMPLETE THE CODE 1:-------------------------------#

var1 = 2 #This is my variable. Var1. Do not change this.
yolo = 42

if yolo != 4:
   print "Uh Oh! Your variable doesn't equal 4!"

var2 = yolo + var1

print var2

#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   Woah! What's all that saying? Well, let's take a look at it piece by piece shall we?   #
#                                                                                          #
#   First off: We are creating another variable, var1, and "assigning" it a value, 2.      #
#   Assigning means we are telling Python what var1 is. We are assigning it a value of 2.  #
#                                                                                          #
#   Next, we have an 'if' statement.                                                       #
#   An if statement checks for true or false. In this case we have:                        #
#   if <your variable> != 4:                                                               #
#   This says in English "If" <your variable> "doesnt equal" 4:                            #
#   A colon marks the beginning of a "Body" of code.                                       #
#   A body of code tells Python to do something, when something else is run. In this case, #
#   if your variable wasn't equal to 4, we told it to say "Your variable doesn't equal 4." #
#                                                                                          #
#   The "print" command will show us the text "Uh Oh! Your variable doesn't equal 4." if   #
#   the "if" statement is true.                                                            #
#                                                                                          #
#   Next we have another variable, this time, var2. And we are assigning it the value of   #
#   <your variable> + var1.                                                                #
#   Since your variable should be 4, and var1 is 2, the answer should be 6. Well, let's    #
#   figure out!                                                                            #
#                                                                                          #
#   Navigate to the "Run" command and select "Run Module" or press "F5" on Windows.        #
#   Make sure the [Complete the Code 1] is not commented out.                              #
#                                                                                          #
#   If everything went as planned, the Python Shell should have read:                      #
#   >>>                                                                                    #
#   6                                                                                      #
#   >>>                                                                                    #
#                                                                                          #
#   If not, or you got an error, recheck the [Complete The Code 1] section.                #
#                                                                                          #
#   Variables can be added to each other, subtracted, divided, etc.                        #
#   However, variables do not have to be just numbers. Variables can be "strings" too.     #
#   A string is text. The only difference between strings and variables, is that           #
#   strings are encased by quotes, either single '' or double "", and the text appears     #
#   green in the IDLE or VIDLE (This program). There are a few exceptions for strings,     #
#   using other characters like \ or an apostrophe in words like (don't) may mess up       #
#   the intended string. A way around this is to use triple double quotes.                 #
#   If you need to use quotes and single quotes in a string, encase the entire string      #
#   in triple double quotes like below. Try running the code below to see it printed       #
#   in the Python Shell.                                                                   #
#                                                                                          #
#---------------------------------------STRING EXAMPLE 1-----------------------------------#

##print """This is a 'string' that uses single and "double" quotes."""

#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   Encasing strings in triple quotes elminates Python reading other symbols that may      #
#   have interfered with your string. Now let's make a variable with a string, and see     #
#   what we can do with it.                                                                #
#   A note to remember:                                                                    #
#   - If you encase your string in 'single quotes':                                        #
#   You can use "double quotes" inside the string.                                         #
#   - If you encase your string in "double quotes":                                        #
#   You can use 'single quotes' inside the string.                                         #
#   - If you encase your string in """triple quotes""":                                    #
#   You can use any symbol inside your string.                                             #
#                                                                                          #
#   The variable 'my_string' can be assigned using = to a value, in this case, assign it   #
#   to a string of your choice. Take into account what your string will include to         #
#   determine what kind of quotes you need to use.                                         #
#                                                                                          #
#---------------------------------------COMPLETE THE CODE 2:-------------------------------#

##my_string = <enter a string>
##
##print (isinstance(my_string, basestring))
##
##print my_string

#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   Alright, let's pick apart what we have up there once more.                             #
#                                                                                          #
#   First, we have the variable: my_string                                                 #
#   We assign my_string to <your string>.                                                  #
#                                                                                          #
#   Next we have print (isinstance(my_string, basestring))                                 #
#   Woah! What's all this mean? Well, let's take a look:                                   #
#   - print                                                                                #
#   > We know what print does, it outputs something to the Shell or terminal.              #
#   But why is (isintance(my_string, basestring)) in parentheses, when "print my_string"   #
#   isn't?                                                                                 #
#   Good question. The answer to that is organization. By encasing exactly what we want    #
#   to print, we are organizing our code for ourselves and anyone else. They will know     #
#   we want to print everything inside the parentheses, in this case, the isinstance       #
#   function.                                                                              #
#                                                                                          #
#   So once more, we have:                                                                 #
#   - print                                                                                #
#   > Print something to the Shell or terminal.                                            #
#   - isinstance(object, class or type)                                                    #
#   > isinstance is a function that we can use to check if an object is something.         #
#   While that may sound vague, we are checking "my string" as the object, and we are      #
#   asking Python if "my_string" is a "basestring" which includes all types of strings,    #
#   both regular text and unicode (special symbols).                                       #
#   - isinstance(my_string, basestring)                                                    #
#   > "my_string" is the object, and "basestring" is the class we are checking.            #
#   We could substitute this for a number of things. We could ask if "var1" is an          #
#   integer like this.                                                                     #
#                                                                                          #
#   isinstance(var1, int)                                                                  #
#                                                                                          #
#   And finally, we print my_string.                                                       #
#                                                                                          #
#   That is a lot to understand, so make sure you're satisfied with the logic of the       #
#   code above, and review it if you feel you need to.                                     #
#                                                                                          #
#   Lastly, we're going to go over lists.                                                  #
#   To perform a function on something, you use a . followed by the command you want       #
#   to perform. Example: mylist[.sort]                                                     #
#                                                                                          #
#   Lists are variables that can be added to and removed from, sorted, counted, etc.       #
#   Some of the commands with lists are:                                                   #
#   .append(x)  : Add something to the end of the list.                                    #
#   .remove(x)  : Remove the first item in the list whose value is x, if there is no       #
#                 such item it is an error.                                                #
#   .sort()     : Sort the list in alphabetical order.                                     #
#   .insert(i,x): Insert something at the given point. i is the index, x is the item.      #
#                 i = 0 would be the front of the list.                                    #
#   .index(x)   : Find the index of the item x, it is an error if there is no item x.      #
#   .pop(i)     : Removes the item at index i from the list and 'returns' it to a          #
#                 function. If no i is given, .pop() takes the last item on the list.      #
#   .count(x)   : Return the number of times x appears in the list.                        #
#   .reverse()  : Reverse the elements of the list, in place.                              #
#                                                                                          #
#   Let's create a list and try some things with it.                                       #
#   Lists are denoted by square brackets after assignment. You can add elements to the     #
#   list when it is first created, separating elements by commas, or you can leave it      #
#   empty and add to it whenever you please.                                               #
#   Example: example_list = []                                                             #
#   Example2: example_list_2 = [4, 4, 5, 6, "string", variable, 2.14]                      #
#                                                                                          #
#   Let's create a list, and add the following things to it using the .append() function.  #
#   Create a list of your choice, keep it empty.                                           #
#   Add "Green Eggs" to your list.                                                         #
#   Next, add "Ham" to your list.                                                          #
#   Next, print how many times "Ham" appears in your list.                                 #
#   Lastly, print your list to the Shell.                                                  #
#   Then run your program.                                                                 #
#                                                                                          #
#---------------------------------------COMPLETE THE CODE 3:-------------------------------#

##create your list and add elements here.





#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   Did your code perform as expected? If not, try again! If it printed this:              #
#   >>>                                                                                    #
#   1                                                                                      #
#   ['Green Eggs', 'Ham']                                                                  #
#   >>>                                                                                    #
#   Then you've added the elements correctly. If something else was printed, but similar   #
#   to the above, that is okay too.                                                        #
#                                                                                          #
#   Now, a quick note, you probably made your code like this:                              #
#   my_list = []                                                                           #
#   my_list.append("Green Eggs")                                                           #
#   my_list.append("Ham")                                                                  #
#   etc.                                                                                   #
#                                                                                          #
#   While this is correct, did you know you could also assign variables to strings and     #
#   add those to the list as well? That way they can be used in multiple lists or          #
#   anywhere in our program.                                                               #
#                                                                                          #
#   For example:                                                                           #
#   ge = "Green Eggs"                                                                      #
#   ham = "Ham"                                                                            #
#   my_list.append(ge)                                                                     #
#   my_list.append(ham)                                                                    #
#   print my_list                                                                          #
#                                                                                          #
#   This would yield the same output.                                                      #
#   Did you also know? You can add variables to each other even if they are strings?       #
#                                                                                          #
#   They are added as they are, without spaces or commas, so you may want to edit          #
#   strings you want to add together if you want them to be gramatically correct.          #
#   This could be useful if you want to make combinations of different variables or        #
#   strings.                                                                               #
#                                                                                          #
#   Example:                                                                               #
#   ge = "Green Eggs, "                                                                    #
#   ham = "Ham, "                                                                          #
#   milk = "Milk, "                                                                        #
#   bisc = "A Biscuit, "                                                                   #
#   n = "And "                                                                             #
#   ending = "and that's it."                                                              #
#                                                                                          #
#   print "My breakfast:"                                                                  #
#   print (ge + ham + milk + ending)                                                       #
#                                                                                          #
#   [or]                                                                                   #
#                                                                                          #
#   print (ham + bisc +  milk + ending)                                                    #
#   etc.                                                                                   #
#                                                                                          #
#   The latter will print:                                                                 #
#   >>>                                                                                    #
#   Ham, A Biscuit, Milk, and that's it.                                                   #
#   >>>                                                                                    #
#                                                                                          #
#   Finally, here is a space for you to utilize variables, lists and strings to            #
#   experiment if you wish. If you need more space, simply press enter to make a new       #
#   line. When finished experimenting, don't forget to comment out the lines, so they      #
#   do not interfere with other exercises, unless you wish to keep displaying them in      #
#   the shell.                                                                             #
#                                                                                          #
#---------------------------------------FREE WORKSPACE-------------------------------------#







#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   This is the end of the variable section. Next we are going to talk briefly about       #
#   "Booleans."                                                                            #
#                                                                                          #
#==========================================================================================#
#                                       BOOLEANS                                           #
#==========================================================================================#
#                                                                                          #
#   This small section will cover Booleans and the if/else statements.                     #
#   To get started, booleans are like a lighswitch. They can either be "On/Off" or in this #
#   case, "True/False".                                                                    #
#   Booleans can be created and assigned like any other variable, but remember to make     #
#   it a boolean it must have the value of "True" or "False"                               #
#                                                                                          #
#   Example: my_boolean = False                                                            #
#                                                                                          #
#   This means "my_boolean" is false. This can be helpful for a number of reasons. We can  #
#   use booleans like switches, to track progress of something or to give a readout on     #
#   anything you may want to assign a True or False value to.                              #
#                                                                                          #
#   That's that! Booleans are that simple!                                                 #
#   Let's try to incorporate a boolean into some other code, and see what they can do.     #
#   Examine the code below, and determine what 'test_boolean' will be after the program    #
#   has been ran. (True/False)                                                             #
#   Input your answer as True / False in the variable "my_answer".                         #
#                                                                                          #
#---------------------------------------COMPLETE THE CODE 4:-------------------------------#

my_answer = "<After reading below, change this to True or False, without the quotes.>"

##test_boolean = False
##
##this_string = "A string."
##another_string = "A string."
##
##test_boolean = (this_string == another_string)
##print test_boolean
##

############################################################################################
#                                       !!DO NOT READ BELOW HERE, SPOILER!!                #
############################################################################################






















if my_answer == True:
    print "Correct!"
elif my_answer == False:
    print "Incorrect, re-examine the code."

############################################################################################
#                                       !!END SPOILER SECTION!!                            #
############################################################################################

#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   Did you get the answer right? If so, congrats! You're on your way to mastering the     #
#   art of utilizing booleans.                                                             #
#                                                                                          #
#   Lastly, we're going to go over the if/elif/else statement.                             #
#                                                                                          #
#   An "if/else" statement is a boolean. It is used to check 'is "____" true?'             #
#                                                                                          #
#   The structure of an "if" statement is as follows.                                      #
#                                                                                          #
#   Begin with the if statement, followed by the object or object you would like to check, #
#   and then a colon. After the colon, pressing enter should automatically indent by 1 Tab #
#   but if for some reason Python does not automatically indent, any time you have a       #
#   colon, you should follow subsequent lines that you want to be in the body of the code  #
#   with 1 tab (4 spaces), or enough tabs based on where the body of the code is located.  #
#                                                                                          #
#   Example: If you have two "if" statements, the second if statement's body code should   #
#   be indented by 2 tabs. (1st "if" statement = 1 tab, the second "if" statement = 2      #
#   tabs.)                                                                                 #
#                                                                                          #
#   if some_object [is] something:                                                         #
#   TAB:print "Some object is something is true."                                          #
#                                                                                          #
#   This is a very poor example of an if statement, but a better example is the if         #
#   statement that checks whether your answer to the Boolean Exercise was true. Look over  #
#   that "if" statement for a better example. Remember that "if" statements can use all    #
#   sorts of comparators, as well as other operations to check.                            #
#                                                                                          #
#   Lastly, "if" statements do not have to check if an object is true or false             #
#   strictly. They can check is object1 is (equal to, less than, etc.) object2.            #
#                                                                                          #
#   "Elif" statements can be used in conjunction with "if" statements. They mean           #
#   "else/if", the way they should be used is essentially another branch of an "if"        #
#   statement. It can be used to check an alternate condition to your "if" statement,      #
#   and execute a separate body of code. You can use as many "elif"s as you like.          #
#                                                                                          #
#   Example, we have var1 and var2. We want Python to say "True" if var1 is the same       #
#   as var2, and if var1 is greater than var2 we want it to say "Greater than" and if      #
#   if var1 is less than var2 we want it to say "Less than", and finally, if none of       #
#   those are true, print "None are true."                                                 #
#                                                                                          #
#   That's a big chunk of code! How can we accomplish that? Well, let's try to, using      #
#   if and elif statements. Create two variables, and assign one to 6, and the other       #
#   to 2.                                                                                  #
#                                                                                          #
#---------------------------------------COMPLETE THE CODE 5:-------------------------------#

##<create a variable1 here>
##<create a variable2 here>
##
##if <variable1> <use the correct comparator for "equals"> <variable2>:
##  print "True!"
##elif <variable1> <use the correct comparator for "greater than> <variable2>:
##  print "Greater than."
##elif <variable1> <use the correct comparator for "less than> <variable2>:
##  print "Less than."
##else:
##  print "None are true."

#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   After following the instructions above, the result should have been "True!"            #
#   Experiment with variable1 and variable2 values to change the results.                  #
#                                                                                          #
#   The last thing we will cover for booleans is the "else" statement. In an "if/elif"     #
#   clause, "else" can be put at the very end. It is a catch-all statement. Usually it is  #
#   optional, and if none of the if/elif statements are ran, the else statement is         #
#   executed.                                                                              #
#                                                                                          #
#   This concludes the short section regarding booleans and the if/elif clauses.           #
#                                                                                          #
#==========================================================================================#
#                                       OPERATORS                                          #
#==========================================================================================#
#                                                                                          #
#   This small section will go over a few of the most used comparators and operators       #
#   that are used in Python. The comparators may be repeated, but here are some simple     #
#   operators, comparators and flow control statements.                                    #
#                                                                                          #
#   ==      ~   Equals (Equality Comparison, similar to "is")                              #
#   >=      ~   Greater Than or Equal To                                                   #
#   <=      ~   Less Than or Equal To                                                      #
#   >       ~   Greater Than                                                               #
#   <       ~   Less Than                                                                  #
#   !=      ~   Not Equal To                                                               #
#                                                                                          #
#   or      ~   Check if one or more conditions are true, only one needs to be true.       #
#   and     ~   Check if one or more conditions are true, all must be true.                #
#   is not  ~   Check an identiy comparison. (Similar to ==)                               #
#   not     ~   Negative; change element to the "negative".                                #
#                                                                                          #
#   +       ~   Addition. (Integers, Floats, Long, Strings, Variables, Lists, etc.)        #
#   -       ~   Subctraction. (See above.)                                                 #
#   *       ~   Multiplication. (Integers, Floats, Long)                                   #
#   /       ~   Division. (See above.)                                                     #
#   %       ~   Modulus. (Divide by n, then take the remainder.)                           #
#   **      ~   Exponent.                                                                  #
#                                                                                          #
#   +=      ~   Add AND. Add right operand to the left operand. Result given to left       #
#               operand. [Example: c += a is equal to c = c + a.]                          #
#   -=      ~   Subtract AND. (See above, subtract instead.)                               #
#   *=      ~   Multiply AND. (See above, multiply instead.)                               #
#   /=      ~   Divide AND. (See above, divide instead.)                                   #
#   %=      ~   Modulus AND. (See above, modulus instead.)                                 #
#   **=     ~   Exponent AND. (See above, exponent instead.)                               #
#                                                                                          #
#   This concludes the small section listing basic operators in Python.                    #
#                                                                                          #
#==========================================================================================#
#                                       LOOPS                                              #
#==========================================================================================#
#                                                                                          #
#   Here, we will examine two simple loops. "While" loops, and "for" loops.                #
#                                                                                          #
#   A while loop statement in Python programming language repeatedly executes a target     #
#   statement as long as a given condition is true.                                        #
#   Example:                                                                               #
#   while expression:                                                                      #
#       statement(s)                                                                       #
#                                                                                          #
#   Here, statement(s) may be a single statement or a block of statements. The condition   #
#   may be any expression, and true is any non-zero value. The loop iterates while the     #
#   condition is true.                                                                     #
#   When the condition becomes false, program control passes to the line immediately       #
#   following the loop.                                                                    #
#   In Python, all the statements indented by the same number of character spaces after    #
#   a programming construct are considered to be part of a single block of code. Python    #
#   uses indentation as its method of grouping statements.                                 #
#                                                                                          #
#   A loop becomes infinite loop if a condition never becomes FALSE. You must use caution  #
#   when using while loops because of the possibility that this condition never resolves   #
#   to a FALSE value. This results in a loop that never ends. Such a loop is called an     #
#   infinite loop.                                                                         #
#   An infinite loop might be useful in client/server programming where the server         #
#   needs to run continuously so that client programs can communicate with it as and       #
#   when required.                                                                         #
#                                                                                          #
#   Python supports to have an else statement associated with a loop statement.            #
#   If the else statement is used with a while loop, the else statement is executed        #
#   when the condition becomes false.                                                      #
#                                                                                          #
#---------------------------------------WHILE LOOP EXAMPLE---------------------------------#

##count = 0
##while count < 5:
##   print count, " is  less than 5"
##   count = count + 1
##else:
##   print count, " is not less than 5"

#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   For loops are traditionally used when you have a piece of code which you want to       #
#   repeat n number of times.                                                              #
#                                                                                          #
#   While loops can be an alternative to these loops, but while loops are used when a      #
#   condition is to be met, or when something needs to be run forever.                     #
#                                                                                          #
#   Below is in example of a For loop that will run 3 times. (0 - 3 meaning: 0,1,2)        #
#                                                                                          #
#---------------------------------------FOR LOOP EXAMPLE-----------------------------------#

##for x in range(0, 3):
##    print "We're on time %d" % (x)

#---------------------------------------END WORKSPACE. DO NOT TYPE BELOW THIS--------------#
#                                                                                          #
#   A For loop could theoretically be run forever, if you give the range as a very         #
#   large number. However, knowing both of these loops now, you can choose which one will  #
#   be most effective for your program.                                                    #
#   The "%d" inside the string allows you to print a variable inside the string. The "%"   #
#   on the outside of the quotes indicates which variable you are going to print. In this  #
#   case, the variable is 'x'.                                                             #
#   The "in" "range" part of this 'for' loop indicates while the variable 'x' is 'in'      #
#   the range of 0 to 3, meaning from 0, 1, and 2. Range does not include the endpoint.    #
#                                                                                          #
#==========================================================================================#
#                                       END OF THE BASICS                                  #
#==========================================================================================#
#                                                                                          #
#   Thank you for participating in this basic Python programming exercise!                 #
#   Even though it isn't extremely long, I put a considerable amount of hours into this    #
#   to try and make everything clear and easy to understand.                               #
#                                                                                          #
#   If something was unclear, or you did not understand, please send me an email at        #
#   kworley@csumb.edu                                                                      #
#   I will try to/plan on releasing more of these to everyone. And if someone has a        #
#   request, a question on some particular code, please feel free to send me an email      #
#   and ask me about it. Feel free to also ask Jessica Gonzales, as she is extremely       #
#   smart and knowledgeable in Python. Don't be afraid to ask for help.                    #
#   Jessica's email is jesgonzales@csumb.edu                                               #
#                                                                                          #
#   Once again, I hope you found this to be helpful in understanding some of the basics!   #
#   Please leave me some feedback via email or in person, let me know if this was          #
#   helpful.                                                                               #
#                                                                                          #
#   Thank you again for taking the time to participate. Feel free to write any code        #
#   you want below the "End of Code" section, using these notes as reference.              #
#                                                                                          #
#   -Kirk Worley                                                                           #
#==========================================================================================#
#                                       END OF CODE                                        #
#==========================================================================================#
