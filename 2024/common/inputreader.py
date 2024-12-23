from IPython.core.display import HTML, Markdown
from aocd.models import Puzzle
from bs4 import BeautifulSoup

from .matrix import Matrix


class InputReader:
    """
    Class to read input from file
    """

    def __init__(self, input_source: str):
        self.input_data = input_source.splitlines()

    def lines_as_str(self) -> list:
        """
        Read input as list of strings

        :return:
        """
        return self.input_data

    def as_str(self) -> str:
        """
        Read input as list of strings

        :return:
        """
        return "".join(self.input_data)

    def as_chrs(self) -> list:
        """
        Read input as list of strings

        :return:
        """
        return list("".join(self.input_data))

    def lines_as_int(self) -> list:
        """
        Read input as list of integers

        :return:
        """
        return list(map(int, self.input_data))

    def lines_as_ints(self) -> list:
        """
        Read input as list of lists of integers

        :return:
        """
        return [list(map(int, x.split())) for x in self.input_data]

    def lines_as_strs(self) -> list:
        """
        Read input as list of lists of integers

        :return:
        """
        return [list(x.split()) for x in self.input_data]

    def matrix(self) -> Matrix:
        """
        Read input as matrix

        :return:
        """
        return Matrix([list(x) for x in self.input_data])


class PuzzleWrapper:

    def __init__(self, year: int, day: int):
        self.puzzle = Puzzle(year=year, day=day)

    def get_code_blocks(self, min_length) -> list:
        files = [
            self.puzzle.prose0_path,
            self.puzzle.prose1_path,
            self.puzzle.prose2_path
        ]

        output = []

        for file in files:
            # read files if they exist
            if file.is_file():
                text = file.read_text()
                soup = BeautifulSoup(text, features="html.parser")
                for code in soup.find_all("code"):
                    text = []
                    for content in code.contents:
                        text.append(content.get_text())
                    text = "".join(text)
                    if len(text) >= min_length:
                        output.append(text)

        return output

    def get_code_block(self, block_number: int, min_length=30) -> InputReader:
        blocks = self.get_code_blocks(min_length)
        return InputReader(blocks[block_number])

    def print_article(self, part: int):
        files = [
            self.puzzle.prose0_path,
            self.puzzle.prose1_path,
            self.puzzle.prose2_path
        ]

        articles = []

        for file in files:
            # read files if they exist
            if file.is_file():
                text = file.read_text()
                soup = BeautifulSoup(text, features="html.parser")
                for article in soup.find_all("article"):
                    articles.append(article)

        display(HTML(articles[part].prettify()))

    def print_easter_eggs(self):
        display(Markdown(f"## Easter Eggs"))
        for next_easter_egg in self.puzzle.easter_eggs:
            title = next_easter_egg['title']
            display(Markdown(f"{next_easter_egg} ({title})"))

    def example(self, example_number=0) -> InputReader:
        example = self.puzzle.examples[example_number]
        return InputReader(example.input_data)

    def input(self) -> InputReader:
        return InputReader(self.puzzle.input_data)

    def header(self):
        display(Markdown(f"# {self.puzzle.title}"))
        display(Markdown(f"[Open Website]({self.puzzle.url})"))
