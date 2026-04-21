# Rock-Paper-Scissors

A CLI Rock, Paper, Scissors game built using Python.

## Requirements

- Python 3.10+

## Run Locally

1. Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Run the game.

```powershell
python main.py
```

## Build Executable (PyInstaller One-File)

Always build with `--onefile` so the output is a single executable *i made this mistake so yeah plz do it.

```powershell
pyinstaller --clean --onefile --name rock-paper-scissors main.py
```

The executable will be created at:

- `dist/rock-paper-scissors.exe`

You can now run the project.
