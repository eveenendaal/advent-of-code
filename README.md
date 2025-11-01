# Advent of Code Solutions

My personal solutions to the [Advent of Code](https://adventofcode.com/) puzzles, implemented in Python using Jupyter notebooks.

## Progress

| Year | Completed | Progress |
|------|-----------|----------|
| 2024 | 25/25 ⭐ | ████████████████████████████████ 100% |
| 2023 | 1/25      | █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 4% |
| 2022 | 2/25      | ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 8% |
| 2021 | 1/25      | █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 4% |
| 2020 | 1/25      | █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 4% |
| 2019 | 1/25      | █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 4% |
| 2018 | 1/25      | █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 4% |
| 2017 | 1/25      | █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 4% |
| 2016 | 1/25      | █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 4% |
| 2015 | 5/25      | █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 20% |

**Total: 39/275 puzzles completed**

## Repository Structure

```
├── 2015-2025/          # Solutions organized by year
│   └── day_XX.ipynb    # Jupyter notebooks for each day (25 per year)
├── common/             # Shared utilities and helper functions
│   ├── __init__.py     # Package initialization
│   ├── inputreader.py  # Input parsing utilities
│   └── matrix.py       # Matrix/grid helper functions
└── pyproject.toml      # Project dependencies and configuration
```

## Technology Stack

- **Python 3.13+** - Primary language
- **Jupyter Notebooks** - Interactive development and presentation
- **UV** - Fast Python package manager

### Key Dependencies

- [advent-of-code-data](https://pypi.org/project/advent-of-code-data/) - Automatic puzzle input fetching
- [NetworkX](https://networkx.org/) - Graph algorithms and data structures
- [NumPy/Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [Matplotlib](https://matplotlib.org/) - Data visualization
- [SymPy](https://www.sympy.org/) - Symbolic mathematics

## Setup & Usage

### Prerequisites

- Python 3.13 or higher
- [UV](https://docs.astral.sh/uv/) (recommended) or pip

### Using GitHub Codespaces or Dev Containers

The easiest way to get started is using GitHub Codespaces or VS Code Dev Containers. The repository includes a pre-configured devcontainer that automatically:
- Sets up a universal development environment with Python support
- Installs UV package manager
- Installs all dependencies via `uv sync`
- Configures Jupyter and Python extensions

Simply open the repository in Codespaces or in VS Code with the Dev Containers extension.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/eveenendaal/advent-of-code.git
   cd advent-of-code
   ```

2. Install dependencies:
   ```bash
   # Using UV (recommended)
   uv sync
   
   # Using pip
   pip install -e .
   ```

3. Set up your session token for automatic input fetching:
   ```bash
   # Get your session token from adventofcode.com browser cookies
   export AOC_SESSION="your_session_token_here"
   ```

### Running Solutions

Open any Jupyter notebook and run all cells:
```bash
jupyter notebook 2024/day_01.ipynb
```

## Solution Structure

Each solution follows a consistent structure:

1. **Input Processing** - Parse problem input using `InputReader`
2. **Part 1** - Solve the first part with test cases
3. **Part 2** - Solve the second part with test cases
4. **Easter Eggs** - Display any hidden messages from the problem

## Useful Links

- [Advent of Code](https://adventofcode.com/) - Official AoC website
- [NetworkX Documentation](https://networkx.org/documentation/stable/index.html)
- [Advent of Code Data](https://pypi.org/project/advent-of-code-data/) - Python library for AoC
- [Peter Norvig's AoC Python Utils](https://github.com/norvig/pytudes/blob/10ee4b490097f11d947def8a5b4e5203a5876e27/ipynb/AdventUtils.ipynb)
- [AoC Subreddit](https://www.reddit.com/r/adventofcode/) - Community discussions
