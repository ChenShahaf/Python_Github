#LESSON 12 INPUT/OUTPUT FILES

def PART1():
    '''
    Part 1 = See It to Believe It
    Until now,
    the Python code you've been writing comes from one source and only goes to one place: you type it in at the keyboard
    and its results are displayed in the console.
    But what if you want to read information from a file on your computer,
    and/or write that information to another file?
    This process is called file I/O (the "I/O" stands for "input/output"),
    and Python has a number of built-in functions that handle this for you.
    '''
    #EXAMPLE
    my_list = [i ** 2 for i in range(1, 11)]
    # Generates a list of squares of the numbers 1 - 10
    f = open("output.txt", "w")

    for item in my_list:
        f.write(str(item) + "\n")

    f.close()
def PART2():
    #PART 2 - The open() Function
    '''
    Let's walk through the process of writing to a file one step at a time.

    The first code that you saw executed in the previous exercise was this:
    ======================================================================
    =           f = open("output.txt", "w")                              =
    ======================================================================
    This told Python to open output.txt in "w" mode ("w" stands for "write").
    We stored the result of this operation in a file object, f.
    Doing this opens the file in write-mode and prepares Python to send data into the file.

    MODES OF MANIPULATING TEXT:
    write-only mode ("w")
    read-only mode ("r")
    read and write mode ("r+")
    append mode ("a"), which adds any new data you write to the file to the end of the file.
    '''

    my_file = open("output.txt", "r+")
def PART3():
    '''
    We added the list comprehension from the first exercise to the code in the editor.
    Our goal in this exercise will be to write each element of that list to a file called output.txt.
    The output.txt file that you write to will be created in your current folder -
    for simplicity, the folder has been hidden. output.txt will list each number on its own line.
    We can write to a Python file like so:
    ==============================================
    =   my_file.write("Data to be written")      =
    ==============================================
    The .write() method takes a string argument, so we'll need to do a few things here:
    You must close the file.
    You do this simply by calling my_file.close()
    (we did this for you in the last exercise).
    If you don't close your file, Python won't write to it properly. From here on out, you gotta close your files!
    '''
    my_list = [i ** 2 for i in range(1, 11)]
    my_file = open("output.txt", "w")
    # Add your code below!
    for value in my_list:
        my_file.write(str(value) + "\n")

    my_file.close()
def PART4():
    #Reading
    '''
    Finally, we want to know how to read from our output.txt file.
    As you might expect, we do this with the read() function, like so:
    =================================================================
    =           print(my_file.read())                               =
    =================================================================
    '''
    my_file = open("output.txt", "r")
    print(my_file.read())
    my_file.close()
def PART5():
    #Reading Between the Lines
    '''
    What if we want to read from a file line by line, rather than pulling the entire file in at once.
    Thankfully, Python includes a .readline() method that does exactly that.
    If you open a file and call .readline() on the file object, you'll get the first line of the file;
    subsequent calls to .readline() will return successive lines.
    '''
    my_file = open("text1.txt", "w")
    my_file.write("I am the first line.\n"
                  "I am the second line.\n"
                  "I am the third line.\n")
    my_file = open("text1.txt", "r")

    print(my_file.readline())
    print(my_file.readline())
    print(my_file.readline())
    my_file.close()
def PART6():
    #Part 6 - PSA: Buffering Data
    '''
    We keep telling you that you always need to close your files after you're done writing to them. Here's why!
    During the I/O process, data is buffered:
        this means that it is held in a temporary location before being written to the file.
    Python doesn't flush the buffer—that is, write data to the file—until it's sure you're done writing.
    One way to do this is to close the file. If you write to a file without closing,
    the data won't make it to the target file.
    '''
    # Use a file handler to open a file for writing
    write_file = open("text.txt", "w")

    # Open the file for reading
    read_file = open("text.txt", "r")

    # Write to the file
    write_file.write("Not closing files is VERY BAD.")
    write_file.close()
    # Try to read from the file
    print(read_file.read())
    write_file.close()
def PART7():
    #The 'with' and 'as' Keywords
    '''
    Programming is all about getting the computer to do the work.
    Is there a way to get Python to automatically close our files for us?
    Of course there is. This is Python.

    You may not know this, but file objects contain a special pair of built-in methods: __enter__() and __exit__().

    The details aren't important, but what is important is that when a file object's __exit__() method is invoked,
    it automatically closes the file. How do we invoke this method? With with and as.

    The syntax looks like this:
    ============================================
    =   with open("file", "mode") as variable: =
    =       # Read or write to the file        =
    ============================================
    '''
    with open("text.txt", "w") as textfile:
        textfile.write("Success!")
def PART8():
    #PART 8 -Try It Yourself
    with open("TestText.txt", "w") as my_file:
        my_file.write("This ia a test File.")
def PART9():
    #PART 9- Case Closed?
    '''
    Finally, we'll want a way to test whether a file we've opened is closed.
    Sometimes we'll have a lot of file objects open,
    and if we're not careful, they won't all be closed. How can we test this?
    ===================================
    =   f = open("bg.txt")            =
    =   f.closed                      =
    =   # False                       =
    =   f.close()                     =
    =   f.closed                      =
    =   # True                        =
    ===================================
    Python file objects have a closed attribute which is True when the file is closed and False otherwise.
    By checking file_object.closed, we'll know whether our file is closed and can call close() on it if it's still open.
    '''
    with open("textPart9.txt", "w") as my_file:
        my_file.write("My Data!")
    #Meaning if my_file.closed == FALSE(meaning that the file is open) then close it.
    if not my_file.closed:
        my_file.close()
    #print the boolean value of the closed file -meaning tell us if the file is closed or open
    print(my_file.closed)
PART9()