import random
import re
from pathlib import Path

def extract_tasks(file_path: Path):
    """
    Parse a markdown file and return a list of task strings.
    Tasks are bullet lines that are not section headers.
    Section headers are identified by containing '***' or ending with ':'.
    """
    tasks = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                # Check if line is a bullet point
                if re.match(r'^\s*\* ', line):
                    # Skip section headers
                    if '***' in line or re.search(r':\s*$', line):
                        continue
                    # Remove leading whitespace and the '* ' marker
                    task = re.sub(r'^\s*\*\s*', '', line)
                    tasks.append(task)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    return tasks

def main():
    # Path to the missions file – change this to your actual file
    missions_file = Path("missions.md")
    tasks = extract_tasks(missions_file)

    if not tasks:
        print("No tasks found. Check the file format.")
        return

    selected = random.choice(tasks)
    print("Selected task:")
    print(selected)

if __name__ == "__main__":
    main()
