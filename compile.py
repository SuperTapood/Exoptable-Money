import os

# try to remove the previous build before making a new one
try:
	os.remove("build")
except Exception as e:
	print(e)
	print("it's fine don't worry about it")
	print("'twas expected")
	print("unless its not [WinError 2]")
	print("then you should probably worry")


# activate my venv (PYGAME)
os.system(f"conda activate PYGAME")
# direct the cmd to this dir
os.system(f"cd {os.path.dirname(__file__)}")
# run the compiling script
os.system(f"python build.py build")