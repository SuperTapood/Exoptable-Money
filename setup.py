import cx_Freeze

OPTIONS = {"build_exe": {"packages": ["pygame"],
                         "include_files": ["sprites", "setting.py", "sprite_manager.py",
                         "buy.py", "collision.py", "colors.py", "complex.py",
                         "fallables.py", "game.py", "group.py", "main.py", "letters.py", "objects.py", "scenes.py"]}}
EXECUTABLES = [cx_Freeze.Executable("main.py")]


cx_Freeze.setup(
    options=OPTIONS,
    executables=EXECUTABLES
)