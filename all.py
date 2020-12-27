import os
from collections import defaultdict
from subprocess import check_output
from timeit import default_timer as timer

from rich import print
from rich.live import Live
from rich.spinner import Spinner
from rich.style import Style
from rich.styled import Styled
from rich.table import Table
from rich.text import Text

# Executables for the runtimes, rename if necessary
PYTHON = "python3" if os.name == "posix" else "python"
PYPY = "pypy3"

# Exclude PyPy on days where it doesn't run properly
exclude_runtime = defaultdict(list)
#for i in [19]:
#    exclude_runtime[i].append(PYPY)

# Print runtime versions
python_version = check_output(f"{PYTHON} --version", shell=True)
if python_version:
    python_version = python_version.decode("UTF-8").splitlines()[0]
    print(f"CPython: {python_version}")

pypy_version = check_output(f"{PYPY} --version", shell=True)
if pypy_version:
    tmp = pypy_version.decode("UTF-8").splitlines()[1].split()
    pypy_version = " ".join(tmp[:2])[1:]
    print(f"PyPy: {pypy_version}")

# Define styles which are used more than once
blue = Style(color="blue")
spinner = Spinner("dots", text="In progress...")

# Define table with all its columns
python_time_text = Styled("", style=blue)
pypy_time_text = Styled("", style=blue)
cwd = os.getcwd().split(os.sep)[-1]
# Show year in title - assumes folder is named aoc-YYYY
title = f":snowflake: Advent of Code {cwd.split('-')[1]} :snowflake:" if cwd.startswith("aoc-") else "Advent of Code"
table = Table(title=title, title_style=Style(color="cyan"))
table.add_column("Day")
table.add_column("Part 1")
table.add_column("Part 2", footer="[uu]Total:\n[orange3]Combined Total:[/orange3][/uu]", footer_style=blue)
table.add_column("CPython Time", min_width=16, justify="right", footer=python_time_text)
table.add_column("PyPy Time", min_width=16, justify="right", footer=pypy_time_text)

# Live update table
total = defaultdict(list)
total_combined = [0] * 26
with Live(table, refresh_per_second=10) as live:
    # Execute all 25 days
    for i in range(1, 26):
        # File should be called dayXX.py, skip if doesn't exist
        file = f"day{i:02d}.py"
        if not os.path.exists(file):
            continue

        # Create row for day
        p1_text = Text("")
        p2_text = Text("")
        time_text = dict()
        for runtime in [PYTHON, PYPY]:
            time_text[runtime] = Styled("", style=blue)
        table.add_row(f"Day {i}", p1_text, p2_text, time_text[PYTHON], time_text[PYPY])

        results_added = False
        for runtime in [PYTHON, PYPY]:
            # Skip if runtime is excluded for this day
            if runtime in exclude_runtime[i]:
                time_text[runtime].renderable = Text("N/A")
                time_text[runtime].style = Style()
                continue

            # Show spinner
            time_text[runtime].renderable = spinner

            # Execute day with current runtime
            start = timer()
            output = check_output(f"{runtime} {file}", shell=True)
            end = timer()

            # Compute execution time and show it
            time = (end - start) * 1000
            time_str = f"{round(time):,} ms"
            time_text[runtime].renderable = Text(time_str)
            if time < 1000:
                time_text[runtime].style = Style(color="green")
            elif 1000 <= time < 5000:
                time_text[runtime].style = Style(color="orange1")
            else:
                time_text[runtime].style = Style(color="red")

            total_combined[i] = time if total_combined[i] == 0 else min(total_combined[i], time)

            # Add part 1 + 2 results if we didn't yet
            # Assumes the output contains part 1 result on first line and part 2 result on second line
            if not results_added:
                results = output.decode("UTF-8").splitlines()
                p1_text.append(results[0] if len(results) >= 1 else "N/A")
                p2_text.append(results[1] if len(results) >= 2 else "N/A")

                results_added = True

            total[runtime].append(time)

    # Add footer after all days are finished
    python_time_text.renderable = Text.from_markup(f"[uu]{round(sum(total[PYTHON])):,} ms[/uu]")
    pypy_time_text.renderable = Text.from_markup(f"[uu]{round(sum(total[PYPY])):,} ms\n" +
                                                 f"[orange3]{round(sum(total_combined)):,} ms[/orange3][/uu]")
    table.show_footer = True