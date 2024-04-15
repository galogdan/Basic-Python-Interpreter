from dataclasses import dataclass

MAX_LENGTH = 9  # Max length of variables name and memory


# data classes to simplify the code

@dataclass
class Number:
    value: any

    def __repr__(self):
        return f"{self.value}"


@dataclass
class Boolean:
    value: bool

    def __repr__(self):
        return str(self.value)
