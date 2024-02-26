import sys

# (!) Try changing this multiline string to any image you like:

# There are 68 periods along the top and bottom of this string:

bitmap = """ 
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("Bitmap Message")
print("Enter the message to display with the bitmap.")
message = input("> ")                                     
                                                                 
                                                                    
                                                                    
                                                 

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == " ":
            # Print an empty space since there's a space in the bitmap:
            print(" ", end="")
        else:
            # Print a character from the message:
            print(message[i % len(message)], end="")
    print() # Print a newline
