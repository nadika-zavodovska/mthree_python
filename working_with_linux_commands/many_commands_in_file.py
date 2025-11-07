# gives Python access to your operating system commands (Create folders, list files, get paths, environment variables).
import os
# lets you run Linux shell commands (Execute Linux commands like ls, cat, grep, or even another Python script) in a more controlled and safe way than os.system. Is the modern, powerful, and secure way to run external commands from within Python.
import subprocess

# Write to a file using a Linux command. The shell creates a new file named demo.txt (if it doesn’t exist) or overwrites it (if it does).
os.system("echo Hello from shell > demo.txt")

# Read it again using Linux 'cat'. shell=True - run this command through the system shell, not directly.
subprocess.run("type demo.txt", shell=True)

# open("demo.txt") - opens the file named demo.txt for reading (that’s the default mode "r").
# as f: - gives the opened file a name (f) that we can use to work with it.
with open("demo.txt") as f:
# f.read() reads the entire content of the file as a single string and stored in the variable data.
    data = f.read() 
print("Read in Python:", data)

# Append more text using Python. "a" mode - opens file for adding new text to the end (keeps existing content)
with open("demo.txt", "a") as f:
    f.write("Added from Python\n")

# Show final result using shell
subprocess.run("type demo.txt", shell=True)
