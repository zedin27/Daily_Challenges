#==========================================================================================#
#                                           PYTHON                                         # 
#                                        THE BASICS 3                                      #
#                                       RANDOMIZATION                                      # 
#                                    Written By: Kirk Worley                               #
#==========================================================================================#
#                                           KEY TERMS                                      # 
#==========================================================================================#
#                                                                                          # 
#   import      -   A Python term that implements commands from another module.            # 
#   module      -   A set of code or chunk of code that can be utilized within your own.   # 
#   random      -   A Python module that helps determine unsequenced numbers.              # 
#   command     -   A command from a module is created by using the modules name, a        # 
#                   period, then the command name.                                         # 
#                   Example: random.randInt(l, h)                                          # 
#                                                                                          #
#==========================================================================================#
#                                           OBJECTIVE                                      # 
#==========================================================================================#
#                                                                                          #
#   To learn how to use, interpret, and understand the "Random" module of Python; to       # 
#   be able to implement random generation in your own Python code.                        # 
#                                                                                          #
#==========================================================================================#
#                                           THE RANDOM MODULE                              # 
#==========================================================================================#
#                                                                                          #
#   Throughout our other lessons, we have learned the basic foundations of Python,         # 
#   and even how to create and use functions. Now, say we want to add an element of        # 
#   uncertainty to our code. We can use Pythons built in random generator.                 # 
#   To do this with any program you are writing, before you write any code, you must       # 
#   "import" the built in random module. To do this, simply type above any code you have   # 
#   the following:                                                                         # 
#                                                                                          #
#-------------------------------------------IMPORT RANDOM MODULE---------------------------#

#######################
#   !DO NOT DELETE!   #

import random

#   !DO NOT DELETE!   #
#######################

#-------------------------------------------END WORKSPACE, DO NOT TYPE BELOW THIS----------#
#                                                                                          #
#   Now we have imported our random module, we are able to use any of the commands that    # 
#   come with this module. These commands usually generate random numbers for us, and      # 
#   can be used for a variety of different purposes, such as programming basic AI,         # 
#   creating an uncertainty element to a program, assisting in unbiased choice, etc.       # 
#                                                                                          #
#==========================================================================================#
#                                           THE RANDOM MODULE COMMANDS                     # 
#==========================================================================================#
#                                                                                          #
#   Here are some of the basic  commands we can use with "random":                         # 
#                                                                                          #
#   random.randint(a,b) [Range of a-b including both a and b.]                             # 
#   random.randrange(a, b) [Random integer in the range of a and b, not including b.]      # 
#   random.jumpahead(n) [n > 0, Jump to a state of random generation away from current.*]  # 
#   random.random() [Returns a random float from 0.0 to 1.0]                               # 
#                                                                                          #
#   * = This means while the numebers are generated randomly, the pattern in which they    # 
#       are generated is somewhat similar. Using the "jumpahead" command can help          # 
#       create a better random generator. This is especially useful in programs that       # 
#       have multiple instances of the "random" class.                                     # 
#                                                                                          #
#==========================================================================================#
#                                           RANDOM PRACTICE                                # 
#==========================================================================================#
#                                                                                          #
#   With the commands given, in conjunction with the "print" command, try playing around   # 
#   with different random commands until you become familiar with how they function.       # 
#   Once you feel comfortable on the syntax and usage of a random command, feel free to    # 
#   implement them into your own code for any reason. Remember since the "random" module   # 
#   was already imported, you do not have to import it again.                              # 
#                                                                                          #
#-------------------------------------------RANDOM PRACTICE WORKSPACE:---------------------#

























#-------------------------------------------END WORKSPACE, DO NOT TYPE BELOW THIS----------#
#==========================================================================================#
#                                           END OF LESSON                                  # 
#==========================================================================================#
