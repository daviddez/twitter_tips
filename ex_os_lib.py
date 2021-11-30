import os

# os.system(command)
"""
Execute the command (a string) in a subshell. This is implemented by calling the Standard 
C function system(), and has the same limitations. Changes to sys.stdin, etc. are not reflected 
in the environment of the executed command. If command generates any output, it will be sent 
to the interpreter standard output stream. The C standard does not specify the meaning of the 
return value of the C function, so the return value of the Python function is system-dependent. 
  --> On Unix, the return value is the exit status of the process encoded in the format specified 
      for wait().
  --> Perfered:  subprocess()
"""

# os.name
""" The name of the os dependent module imported. """
print(f'os.name:		{os.name}')

# os.ctermid()
""" Return the filename corresponding to the controlling terminal of this process """
print(f'os.ctermid():		{os.ctermid()}')

# os.environ
""" 
A mapping object where keys and values are stings that represent the process environment. 
This mapping is captured the first time the os module is imported, typically during Python 
startup as part of processing site.py. Changes to the environment made after this time are not 
reflected in os.environ, except for changes made by modifying os.environ directly.
"""
print(f'os.environ:		USERNAME: {os.environ["USERNAME"]}')

# os.environb
"""
Bytes version of environ: a mapping object where both keys and values are bytes objects 
representing the process environment. environ and environb are synchronized (modifying environb 
updates environ, and vice versa).
environb is only available if supports_bytes_environ is True.
"""
#print(f'os.environb:		b HOSTNAME: {os.environb("b'HOSTNAME'")}')

# os.chdir(path)
""" Change the directory """

# os.fchdir(fd)
""" 
Change the current working directory to the directory represented by the file descriptor fd. 
The descriptor must refer to an opened directory, not an open file. As of Python 3.3, this is 
equivalent to os.chdir(fd).
"""
fd = os.open("/home", os.O_RDONLY)
print(f'os.fchdir():		{os.fchdir(fd)}')

# os.getcwd()
""" Get the current working directory """
print(f'os.getcwd():		{os.getcwd()}')

# os.getcwdb()
""" Return a bytestring representing the current working directory. """
print(f'os.getcwdb():		{os.getcwdb()}')
