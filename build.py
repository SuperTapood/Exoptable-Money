# some cmd code used to compile the game
# but it produces a bad application for some ungodly reason

import cx_Freeze

OPTIONS = {"build_exe": {"packages": ["pygame"],
                         "include_files": ['buy.py', 'collision.py', 'colors.py', 'complex.py', 'data.json',
                                           'fallables.py', 'game.py', 'group.py', 'main.py', 'objects.py', 'scenes.py']
                         }}

EXE = [cx_Freeze.Executable("main.py")]
cx_Freeze.setup(options=OPTIONS, executables=EXE)
