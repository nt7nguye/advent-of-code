import sys
from importlib import import_module

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <day> <part>")
        sys.exit(1)

    day = sys.argv[1]
    part = sys.argv[2]

    try:
        puzzle_module = import_module(f"day{day}.part{part}")
    except ImportError:
        print(f"Day {day} or Part {part} not found.")
        sys.exit(1)

    input_data = open(f"day{day}/input{part}.txt", "r").read().splitlines()

    solve_function = getattr(puzzle_module, "solve", None)
    if solve_function is None or not callable(solve_function):
        print(f"Solver function not found for Day {day} Part {part}.")
        sys.exit(1)

    result = solve_function(input_data)
    print(result)

if __name__ == "__main__":
    main()