#!/usr/bin/env python3
"""
Script to create a new Advent of Code solution notebook from a template.

Usage:
    python create_day.py <year> <day>
    
Example:
    python create_day.py 2024 15
"""

import json
import sys
from pathlib import Path


def create_day_notebook(year: int, day: int) -> None:
    """Create a new notebook from template for the given year and day."""
    
    # Validate inputs
    if not (2015 <= year <= 2025):
        print(f"Error: Year must be between 2015 and 2025 (got {year})")
        sys.exit(1)
    
    if not (1 <= day <= 25):
        print(f"Error: Day must be between 1 and 25 (got {day})")
        sys.exit(1)
    
    # Paths
    repo_root = Path(__file__).parent
    template_path = repo_root / "template.ipynb"
    year_dir = repo_root / str(year)
    output_path = year_dir / f"day_{day:02d}.ipynb"
    
    # Check if template exists
    if not template_path.exists():
        print(f"Error: Template file not found at {template_path}")
        sys.exit(1)
    
    # Create year directory if it doesn't exist
    year_dir.mkdir(exist_ok=True)
    
    # Check if file already exists
    if output_path.exists():
        response = input(f"File {output_path} already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(0)
    
    # Load template
    with open(template_path, 'r') as f:
        notebook = json.load(f)
    
    # Replace placeholders in all cells
    for cell in notebook['cells']:
        if 'source' in cell:
            # Replace in source code
            for i, line in enumerate(cell['source']):
                line = line.replace('YYYY', str(year))
                line = line.replace('DD', f'{day:02d}')
                cell['source'][i] = line
    
    # Write the new notebook
    with open(output_path, 'w') as f:
        json.dump(notebook, f, indent=1)
    
    print(f"✅ Created notebook: {output_path}")
    print(f"\nNext steps:")
    print(f"  1. Open the notebook: jupyter notebook {output_path}")
    print(f"  2. Run the setup cell to fetch the problem")
    print(f"  3. Implement your solution!")


def main():
    """Main entry point."""
    if len(sys.argv) != 3:
        print("Usage: python create_day.py <year> <day>")
        print("Example: python create_day.py 2024 15")
        sys.exit(1)
    
    try:
        year = int(sys.argv[1])
        day = int(sys.argv[2])
    except ValueError:
        print("Error: Year and day must be integers")
        sys.exit(1)
    
    create_day_notebook(year, day)


if __name__ == '__main__':
    main()
