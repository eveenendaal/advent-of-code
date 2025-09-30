# Contributing Guide

This guide explains how to create consistent and well-structured Advent of Code solutions in this repository.

> **Quick Reference**: See [STRUCTURE.md](STRUCTURE.md) for a visual diagram of the notebook cell structure.

## Creating a New Solution

### Option 1: Using the Template Script (Recommended)

The easiest way to create a new solution is to use the provided script:

```bash
python create_day.py <year> <day>
```

For example:
```bash
python create_day.py 2024 15
```

This will:
- Create a new notebook from the template
- Place it in the correct year directory
- Pre-fill the year and day values

### Option 2: Manual Creation

If you prefer to create notebooks manually:

1. Copy `template.ipynb` to the appropriate year directory
2. Rename it to `day_XX.ipynb` (e.g., `day_01.ipynb`)
3. Replace `YYYY` with the year and `DD` with the day number

## Notebook Structure

Each solution notebook should follow this consistent structure:

### 1. Header (Markdown Cell)
- Problem title (will be updated after fetching from AoC)
- Brief description placeholder

### 2. Setup (Code Cell)
```python
from common.inputreader import InputReader, PuzzleWrapper

puzzle = PuzzleWrapper(year=int("2024"), day=int("01"))
puzzle.header()
```

### 3. Input Processing (Markdown + Code Cells)
- **Markdown**: Explain what the input parsing does
- **Code**: Define `parse_input(input_reader: InputReader)` function
- Test parsing with example data

**Best Practices:**
- Keep parsing logic separate from solution logic
- Make the function reusable for both parts
- Add type hints
- Include a docstring

### 4. Part 1 (Markdown + Code Cells)
- **Markdown**: Describe Part 1 requirements
- **Code**: Define `part_1(input_reader: InputReader, debug: bool = False)` function
- **Markdown**: "Test Case" header
- **Code**: Test with example data
- **Markdown**: "Real Input" header  
- **Code**: Run with actual puzzle input

**Best Practices:**
- Include a `debug` parameter for verbose output
- Add type hints and docstrings
- Use assertions to verify expected results
- Print intermediate steps when `debug=True`

### 5. Part 2 (Markdown + Code Cells)
Same structure as Part 1, but for Part 2 of the puzzle.

### 6. Easter Eggs (Markdown + Code Cell)
- **Markdown**: Explain that some puzzles have hidden messages
- **Code**: Call `puzzle.print_easter_eggs()`

## Code Style Guidelines

### General Python Conventions
- Use **snake_case** for function and variable names
- Use **type hints** for function parameters and return values
- Add **docstrings** to all functions
- Keep functions focused and single-purpose

### Naming Conventions
- Input parsing: `parse_input()` or `domain_from_input()` (legacy)
- Solution functions: `part_1()` and `part_2()`
- Helper functions: descriptive names like `find_shortest_path()`, `calculate_score()`

### Debug Output
Always include a `debug` parameter in solution functions:

```python
def part_1(input_reader: InputReader, debug: bool = False) -> int:
    """Solve Part 1 of the puzzle."""
    data = parse_input(input_reader)
    
    if debug:
        print(f"Parsed {len(data)} items")
    
    # Solution logic here
    result = 0
    
    if debug:
        print(f"Final result: {result}")
    
    return result
```

### Assertions
Use assertions to validate results:

```python
# For test cases
result = part_1(puzzle.example(0), debug=True)
assert result == 42, f"Expected 42, got {result}"

# For real inputs (once you know the answer)
result = part_1(puzzle.input())
assert result == 12345
```

## Input Processing Best Practices

### Common Patterns

**Reading lines as strings:**
```python
def parse_input(input_reader: InputReader) -> list[str]:
    return input_reader.lines_as_strs()
```

**Reading lines as integers:**
```python
def parse_input(input_reader: InputReader) -> list[list[int]]:
    return input_reader.lines_as_ints()
```

**Reading as a single string:**
```python
def parse_input(input_reader: InputReader) -> str:
    return input_reader.as_str()
```

**Grid/Matrix processing:**
```python
def parse_input(input_reader: InputReader) -> list[list[str]]:
    lines = input_reader.lines_as_strs()
    return [list(line) for line in lines]
```

**Custom parsing with regex:**
```python
import re

def parse_input(input_reader: InputReader) -> list[tuple[int, int]]:
    lines = input_reader.lines_as_strs()
    pattern = re.compile(r"(\d+),(\d+)")
    
    result = []
    for line in lines:
        match = pattern.match(line)
        if match:
            x, y = int(match.group(1)), int(match.group(2))
            result.append((x, y))
    
    return result
```

## Common Utilities

### Available in `common.inputreader`
- `InputReader` - Main class for reading puzzle inputs
- `PuzzleWrapper` - Helper for fetching puzzles and displaying headers
  - `puzzle.header()` - Display problem title and link
  - `puzzle.input()` - Get actual puzzle input
  - `puzzle.example(n)` - Get nth example from problem description
  - `puzzle.print_easter_eggs()` - Display hidden messages

### Available in `common.matrix`
- Grid/matrix manipulation utilities
- Neighbor finding functions
- Direction helpers

### External Libraries
Common libraries already included:
- `networkx` - Graph algorithms
- `sympy` - Symbolic mathematics  
- `numpy`, `pandas` - Data manipulation
- `matplotlib` - Visualization
- `re` - Regular expressions

## Tips for Clean Solutions

1. **Start simple**: Get a working solution first, optimize later
2. **Use markdown**: Explain your approach in markdown cells
3. **Test incrementally**: Run cells as you write them
4. **Keep outputs clean**: Clear output cells before committing (optional)
5. **Reuse code**: If you solve similar problems, extract common code to `common/`
6. **Document edge cases**: Note any special cases in comments or markdown
7. **Be consistent**: Follow the template structure for easier navigation

## Testing Your Notebook

Before committing:

1. **Restart kernel and run all cells**: Ensure your notebook runs top to bottom
2. **Verify assertions**: All test assertions should pass
3. **Check outputs**: Remove any excessively verbose debug output
4. **Validate structure**: Ensure you followed the standard cell structure

## Example Solution Flow

Here's a typical solving workflow:

1. **Read the problem** on adventofcode.com
2. **Create notebook** with `python create_day.py YEAR DAY`
3. **Run setup cell** to fetch problem description
4. **Implement parsing** - Test with example input
5. **Solve Part 1** - Get test case working first
6. **Verify Part 1** - Run with real input, add assertion
7. **Solve Part 2** - Same process as Part 1
8. **Check for easter eggs** - Run the easter eggs cell
9. **Clean up** - Remove excessive debug output, add markdown explanations
10. **Commit** - Push your working solution

## Questions or Suggestions?

If you have ideas for improving the notebook structure or this guide, please open an issue or submit a pull request!
