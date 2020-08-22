import cx_Freeze
OPTIONS = {"build_exe": {"packages": ["pygame", "math", "time", "random"], 
						 "include_files": ['collision.py', 'colors.py', 'complex.py', 'fallables.py', 'game.py', 'group.py', 'main.py', 'objects.py', 'scenes.py']
}}

EXE = [cx_Freeze.Executable("main.py")]
cx_Freeze.setup(options=OPTIONS, executables=EXE)