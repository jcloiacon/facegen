import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("facegen.py", base=base, icon="clienticon.ico")]

cx_Freeze.setup(
    name = "FACEGEN",
    options = {"build_exe": {"packages":["Tkinter"], "include_files":["clienticon.ico", ]}},
    version = "0.01",
    description = "Generates random faces and names",
    executables = executables
    )
