# TO READ FIELES
# f = open("demo.txt", "r")
# print(f.read())
# print(f.read(5))
# print(f.readline())

# for i in f:
#     print(i)
# f.close()


# TO WRITE INTO  EXISTING FILES
# To write to an existing file, you must add a parameter to the open() function:
#
# "a" - Append - will append to the end of the file
#
# "w" - Write - will overwrite any existing content

# f = open("demo.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# # after appending read the file
# f = open("demo.txt", "r")
# print(f.read())
# f.close()

# f = open("demo1.txt", "w")
# f.write("Here Is the new file!")
# f.close()
#
# # to See the file after writing
# f = open("demo1.txt", "r")
# print(f.read())


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
#
# "x" - Create - will create a file, returns an error if the file exist
#
# "a" - Append - will create a file if the specified file does not exist
#
# "w" - Write - will create a file if the specified file does not exist


# # To create a new file
# f = open("demo2.txt", "x")
# f.close()

# f = open("demo3.txt", "w")
# f.close()

# to read the new file
# f = open("demo2.txt", "r")
# print(f.read())

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
# import os
# os.remove ("demo3.txt")

# To avoid getting an error, you might want to check if the file exists before you try to delete it:
import os
if os.path.exists("demo3.txt"):
    os.remove("demo3.txt")
else:
    print("File doesn't exists!")

