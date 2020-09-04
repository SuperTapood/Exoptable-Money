import cx_Freeze

OPTIONS = {"build_exe": {"packages": ["pygame"],
                         "include_files": ["main.py", "buy.py", "collision.py",
                                           "colors.py", "compile.py", "complex.py",
                                           "fallables.py", "game.py", "group.py",
                                           "letters.py", "objects.py", "scenes.py"]}}
EXECUTABLES = [cx_Freeze.Executable("main.py")]


cx_Freeze.setup(
    options=OPTIONS,
    executables=EXECUTABLES
)