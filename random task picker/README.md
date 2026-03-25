# Random Task Picker

A simple tool to randomly select a task from a bullet list in a markdown file.

## Features
- Reads a markdown file (default: `missions.md`).
- Parses bullet points (`*`) that are **not** section headers (headers contain `***` or end with `:`).
- Prints one randomly chosen task.

## Requirements
- Python 3.6 or later.

## Usage

1. Clone this repository.
2. Place your tasks in a markdown file named `missions.md` (or edit the script to use your own filename).
   - Each task should be on its own line, starting with `* `.
   - Example:

```
### My Tasks

* Task 1: do something
* Task 2: another task
```

3. Run the script:
- On Windows: double-click `run_rt.bat` or run `python random_task.py` in a terminal.
- On macOS/Linux: run `python3 random_task.py`.

## Customization
- To change the input file, modify the `missions_file` variable in `random_task.py`.
- The batch file `run_rt.bat` assumes Python is installed at the path specified inside. If you have Python in your system `PATH`, you can change it to just `python random_task.py`.

## License
Feel free to use and modify as needed.
