from aocd import get_data
lines = get_data(day=18, year=2020).splitlines()

import pyparsing as pp
rule_a = pp.infixNotation(pp.Word(pp.nums), [(pp.oneOf("* / + -"), 2, pp.opAssoc.LEFT)])
expressions_a = [rule_a.parseString(line) for line in lines]

rule_b = pp.infixNotation(pp.Word(pp.nums), [(pp.oneOf("+ -"), 2, pp.opAssoc.LEFT), (pp.oneOf("* /"), 2, pp.opAssoc.LEFT)])
expressions_b = [rule_b.parseString(line) for line in lines]


def parse_expression(expr):
    """Recursive expression parsing. The expressions must be present in a structured format."""
    child_expressions = []
    for child_expr in expr:
        if isinstance(child_expr, pp.ParseResults):
            child_expressions.append(parse_expression(child_expr))
        else:
            child_expressions.append(child_expr)
    while len(child_expressions) > 2:
        res = eval("".join(map(str, child_expressions[0:3])))
        child_expressions = [res] + child_expressions[3:]
    return int(child_expressions[0])


print(sum(parse_expression(expr) for expr in expressions_a))
print(sum(parse_expression(expr) for expr in expressions_b))
