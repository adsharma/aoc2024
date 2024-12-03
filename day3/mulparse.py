#!/usr/bin/env python3

import sys

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

# Define a simple grammar for arithmetic expressions
grammar = Grammar(
    r"""
    expr = (mul_expr / do_expr / dont_expr / space / badmul / any)+
    mul_expr = "mul" "(" number "," number ")"
    do_expr = "do()"
    dont_expr = "don't()"
    number = ~r"\d\d?\d?"
    space = ~r"\s+"
    badmul = ~r"mul(?!mul)*"
    any = ~r"."
    """
)


class Calculator(NodeVisitor):
    def __init__(self):
        super().__init__
        self._do = True

    def visit_expr(self, node, visited_children):
        sum = 0
        for v in visited_children:
            if type(v[0]) is int:
                if self._do:
                    sum += v[0]
            elif v[0].text == "do()":
                self._do = True
            elif v[0].text == "don't()":
                self._do = False

        return sum

    def visit_mul_expr(self, node, visited_children):
        return visited_children[2] * visited_children[4]

    def generic_visit(self, node, visited_children):
        """The generic visit method."""
        return visited_children or node

    def visit_number(self, node, visited_children):
        return int(node.text)

    def visit_any(self, node, visited_children):
        return 0


tree = grammar.parse(open("data1.txt").read())
# print(tree)
calc = Calculator()
print(calc.visit(tree))
