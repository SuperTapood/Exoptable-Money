import os

try:
	os.remove("build")
except Exception as e:
	print(e)
	print("it's fine don't worry about it")
	print("'twas expected")
	print("unless its not [WinError 2]")
	print("then you should probably worry")


os.system(f"conda activate PYGAME")
os.system(f"cd {os.path.dirname(__file__)}")
os.system(f"python build.py build")