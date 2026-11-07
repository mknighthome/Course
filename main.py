import ast
import math
from tkinter import Button, Entry, StringVar, Tk

from utils.calculator import add_nums, divide_nums, multiply_nums, subtract_nums


def evaluate_expression(expression):
    """Safely evaluate a basic arithmetic expression."""
    try:
        parsed = ast.parse(expression, mode="eval")
    except SyntaxError:
        raise ValueError("Invalid expression")

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = _eval(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod)):
            left = _eval(node.left)
            right = _eval(node.right)
            if isinstance(node.op, ast.Add):
                return add_nums(left, right)
            if isinstance(node.op, ast.Sub):
                return subtract_nums(left, right)
            if isinstance(node.op, ast.Mult):
                return multiply_nums(left, right)
            if isinstance(node.op, ast.Div):
                return divide_nums(left, right)
            if isinstance(node.op, ast.Pow):
                return left ** right
            if isinstance(node.op, ast.Mod):
                return left % right
        raise ValueError("Unsupported expression")

    return _eval(parsed)


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.display = StringVar()
        self.display.set("0")

        entry = Entry(
            root,
            textvariable=self.display,
            font=("Arial", 22),
            justify="right",
            bd=8,
            relief="sunken",
        )
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        buttons = [
            ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3),
        ]

        for button_data in buttons:
            if len(button_data) == 3:
                text, row, col = button_data
                columnspan = 1
            else:
                text, row, col, columnspan = button_data

            btn = Button(
                root,
                text=text,
                width=6,
                height=2,
                font=("Arial", 16),
                command=lambda value=text: self.handle_click(value),
            )
            btn.grid(row=row, column=col, columnspan=columnspan, sticky="nsew", padx=4, pady=4)

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)

    def handle_click(self, value):
        current = self.display.get()

        if value == "C":
            self.display.set("0")
            return

        if value == "⌫":
            if current and current != "0":
                self.display.set(current[:-1] or "0")
            else:
                self.display.set("0")
            return

        if value == "=":
            expression = current.strip()
            if not expression or expression == "0":
                return
            try:
                result = evaluate_expression(expression)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.display.set(str(result))
            except (ValueError, ZeroDivisionError):
                self.display.set("Error")
            return

        if current == "0" and value not in {"+", "-", "*", "/", "%"}:
            self.display.set(value)
        elif current == "Error":
            self.display.set(value if value not in {"+", "-", "*", "/", "%"} else "0")
        else:
            self.display.set(current + value)


def build_app():
    root = Tk()
    CalculatorApp(root)
    return root


if __name__ == "__main__":
    root = build_app()
    root.mainloop()
