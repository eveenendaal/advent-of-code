# Notebook Cell Structure

This document provides a visual reference for the standard notebook cell structure.

## Cell Flow

```
┌─────────────────────────────────────────────────────────┐
│ 1. Header (Markdown)                                    │
│    • Problem title                                       │
│    • Brief description                                   │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ 2. Setup (Code)                                         │
│    • Import PuzzleWrapper                               │
│    • Initialize puzzle                                   │
│    • Display header                                      │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ 3. Input Processing                                     │
│    ┌───────────────────────────────────────────────┐   │
│    │ Markdown: Explain parsing strategy            │   │
│    └───────────────────────────────────────────────┘   │
│    ┌───────────────────────────────────────────────┐   │
│    │ Code: parse_input() function                  │   │
│    │       Test with example data                  │   │
│    └───────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ 4. Part 1                                               │
│    ┌───────────────────────────────────────────────┐   │
│    │ Markdown: Part 1 requirements                 │   │
│    └───────────────────────────────────────────────┘   │
│    ┌───────────────────────────────────────────────┐   │
│    │ Code: part_1() function                       │   │
│    └───────────────────────────────────────────────┘   │
│    ┌───────────────────────────────────────────────┐   │
│    │ Markdown: "Test Case"                         │   │
│    └───────────────────────────────────────────────┘   │
│    ┌───────────────────────────────────────────────┐   │
│    │ Code: Run with example(0)                     │   │
│    │       Assert expected result                  │   │
│    └───────────────────────────────────────────────┘   │
│    ┌───────────────────────────────────────────────┐   │
│    │ Markdown: "Real Input"                        │   │
│    └───────────────────────────────────────────────┘   │
│    ┌───────────────────────────────────────────────┐   │
│    │ Code: Run with input()                        │   │
│    │       Assert result (once known)              │   │
│    └───────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ 5. Part 2                                               │
│    (Same structure as Part 1)                           │
│    • Markdown: Requirements                             │
│    • Code: part_2() function                            │
│    • Markdown: "Test Case"                              │
│    • Code: Test with example                            │
│    • Markdown: "Real Input"                             │
│    • Code: Run with real input                          │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ 6. Easter Eggs                                          │
│    ┌───────────────────────────────────────────────┐   │
│    │ Markdown: Explain easter eggs                 │   │
│    └───────────────────────────────────────────────┘   │
│    ┌───────────────────────────────────────────────┐   │
│    │ Code: puzzle.print_easter_eggs()              │   │
│    └───────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Benefits of This Structure

1. **Consistency**: Every notebook follows the same pattern
2. **Readability**: Markdown cells explain what's happening
3. **Testability**: Separate test and real input cells
4. **Debugging**: Debug parameter in solution functions
5. **Navigation**: Clear section headers with markdown
6. **Reusability**: Parsing logic separated from solution logic

## Cell IDs

The template uses descriptive cell IDs for better organization:
- `header` - Header markdown
- `setup` - Setup code
- `input-processing-header` - Input processing markdown
- `input-processing` - Input parsing code
- `part1-header` - Part 1 markdown
- `part1-solution` - Part 1 function
- `part1-test-header` - Part 1 test markdown
- `part1-test` - Part 1 test code
- `part1-real-header` - Part 1 real input markdown
- `part1-real` - Part 1 real input code
- (Similar for Part 2)
- `easter-eggs-header` - Easter eggs markdown
- `easter-eggs` - Easter eggs code

These IDs make it easier to navigate large notebooks in Jupyter.
