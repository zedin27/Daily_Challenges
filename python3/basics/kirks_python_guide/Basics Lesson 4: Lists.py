#==========================================================================================#
#                                           PYTHON                                         # 
#                                        THE BASICS 4                                      #
#                                            LISTS                                         # 
#                                    Written By: Kirk Worley                               #
#==========================================================================================#
#                                           OBJECTIVES                                     # 
#==========================================================================================#
#                                                                                          # 
#   In this module, we will learn about lists and how they function. We will see how       # 
#   helpful they can be, as they are like sequences of variables that we can manipulate.   # 
#                                                                                          # 
#==========================================================================================#
#                                           KEY TERMS                                      # 
#==========================================================================================#
#                                                                                          #                           
#   Key terms to know about lists are as follows:                                          # 
#                                                                                          #
#   []          : These square brackets indicate a list.                                   # 
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
#==========================================================================================#
#                                           THIS MODULE                                    # 
#==========================================================================================#  
#                                                                                          #
#   For this module, all you have to do is run it first. Then, after you run it, feel      # 
#   free to examine the code to see how lists can function.                                # 
#                                                                                          #
############################################################################################
#                                           BEGIN CODE                                     # 
############################################################################################

print "============================================"
print "Welcome to Module 4: Lists."
print "In this module we will show you code and show you how it functions"
print "when dealing with lists."
print ""
print "The first thing we will do in our code is create a list."

mylist = []

print "============================================"
print "mylist = []"
print "--------------------------------------------"
print "List created."
print ""
print "Let's also create a variable that we can add to our list."

var_name = raw_input("What should the variable name be?\n>")

print "--------------------------------------------"
print "Alright, our variable name is now '%s'." %var_name
print ""
print "Now that our list 'my list' has been created, we can manipulate it."
print "Let's check out the first command: 'append(x)'"
print ""
print ".append(x) lets us add something to our list."
print "This is how it would look in our code."

mylist.append(var_name)

print "--------------------------------------------"
print "mylist.append(%s)" %var_name
print "--------------------------------------------"
print "%s has been appended to the list." %var_name
print "" 
print "Now how can we check if it is in our lsit?"
print "Well, we can do this:"
print ""
print "--------------------------------------------"
print "print(mylist)"
print "--------------------------------------------"
print ""

print(mylist)

print ""
print "And that is how we can check what is in our list."
print ""
raw_input("Press enter to continue...\n")
print "Now let's examine the next command: 'remove(x)'"
print ""
print ".remove(x) lets us remove something from our list."
print "If there is no value of x in the list, we will get an error."
print "This is how it would look in our code."

mylist.remove(var_name)

print "--------------------------------------------"
print "mylist.remove(%s)" %var_name
print "--------------------------------------------"
print "'%s' has been removed from mylist." %var_name
print ""
print "Now we can check again using 'print(mylist)'"
print ""

print "--------------------------------------------"
print "print(mylist)"
print "--------------------------------------------"
print ""

print(mylist)

print ""
print "There. We have added (append) and subtracted (remove)"
print "variables from our list. We don't have to use a variable, though."
print "We can use integers, strings or floats, too."
print "Example: mylist.append(1220)"
print "Would add 1220 to our list."
print ""
raw_input("Press enter to continue...\n")
print "Next we will look at the command: 'insert(i,x)'"
print "Insert is a command that we can use to insert a value into a specific point"
print "of our list."
print ""
print "Examine the following code."

print "--------------------------------------------"
print """mylist.append("Carl")"""
print """mylist.append("Jacob")"""
print """mylist.append("Ali")"""
print """mylist.append("Sarah")"""
print """print(mylist)"""

print """mylist.insert(1, "Sally")"""
print """print(mylist)"""
print "--------------------------------------------"

print ""
print "This code will add the students Carl, Jacob, Ali, and Sarah to our list."
print "This could be used as a seating chart."
print "But what if Carl and Jacob are talkative? Let's solve that by putting Sally"
print "between them in the seating list."
print "To do that, we have to use the inset command, like above."
print "The insert command is written like this:"
print ".insert(i,x)"
print "i = the index (place) where you want to insert something. 0 is the front of the list."
print "x = the item you want to insert."
print "If you don't provide an i value, it will add it to the end, just like .append(x)"
print ""
print "--------------------------------------------"
print "running the code above..."
print "--------------------------------------------"

mylist.append("Carl")
mylist.append("Jacob")
mylist.append("Ali")
mylist.append("Sarah")
print "List before insert:"
print (mylist)
print "List after insert:"
mylist.insert(1, "Sally")
print(mylist)
print "--------------------------------------------"
print "complete."
print "--------------------------------------------"

print ""
raw_input("Press enter to continue...\n")
print "Next, we will look at the command: 'pop(i)'"
print "The .pop(i) command works like this:"
print ".pop(i)"
print "i = The index of which item you would like to pop. If no i is given, it will take the last value."
print ".pop(i) takes the value at i, removes it from the list, and returns the value it gets."
print ""
print "What does this mean?"
print "Let's do a bit of a complicated example."
print "Let's use our list of students:\n"
print(mylist)
print ""
print "If we have a function that needs to be given a value from anywhere on the list, we can"
print "use the pop command."
print "Examine the following code."

print ""
print "--------------------------------------------"
print "def finder(x):"
print "    x = mylist.pop(0)"
print "    return x"
print ""
print "print (finder(x))"
print "--------------------------------------------"
print ""
print "This code above will do the do the following:"
print "The function 'finder(x)' will remove the first value from the list 'mylist'."
print "This is seen by the .pop(0) command."
print "After the first value is removed, it will be returned to the variable x."
print "This can be seen in the arguments of finder, 'finder(x)' and in the function itself."
print "Then we print the function, which will remove the first element in the list and then display it"
print "via the print command."
print "Let's see it in action.. (Press enter to continue.)"
raw_input("")
print "Here is the code one more time, using our list from before.\n"
print "--------------------------------------------"
print " x = ''"
print "def finder(x):"
print "    x = mylist.pop(0)"
print "    return x "
print ""
print "print (finder(x))"
print "--------------------------------------------"

x = '' 
def finder(x):
    x = mylist.pop(0)
    return x

print "--------------------------------------------"
print (finder(x))
print "--------------------------------------------"
print ""
print "This prints 'Carl' because he is the first student on our list."
print "Now, because we used 'pop', 'Carl' will no longer be in the list of students."
print ".pop(i) removes the element and returns the values it removed.\n And that is how you use the .pop(i) command.\n"
raw_input("Press enter to continue...\n")
print "Lastly, we will take a quick look at the last few commands."
print ".index(x); .sort(); .count(x); and .reverse()"
print "These commands are fairly simple."
print "--------------------------------------------"
print ".index(x) : This command tells you what index the element x is at in the list. If there is no x"
print "then you will recieve an error."
print "--------------------------------------------"
raw_input("Press enter to view '.sort()'\n")
print "--------------------------------------------"
print ".sort() : This command simply sorts the list in (usually) alphabetical order."
print "--------------------------------------------"
raw_input("Press enter to view '.count(x)'\n")
print "--------------------------------------------"
print ".count(x) : This command counts the amount of times the element 'x' appears in the list. If element 'x'"
print "is not present in the list, it will return 0."
print "--------------------------------------------"
raw_input("Press enter to view '.reverse()'\n")
print "--------------------------------------------"
print ".reverse() : This command simply reverses the elements of the list, in place."
print "Example: List1 = [1, 2, 3, 4, 5]
print "List1.reverse()"
print "print List1"
print ">>> [5, 4, 3, 2, 1]
print "--------------------------------------------"
raw_input("Press enter to continue...\n")
print "And that is the end of the lesson of lists! Feel free to exmaine the code to look at"
print "the internal workings of lists. I hope this helped."
print ""
print "============================================"
print "End of code.
print "============================================"

############################################################################################
#                                           END OF CODE                                    # 
############################################################################################
