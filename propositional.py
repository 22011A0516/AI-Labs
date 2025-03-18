import itertools

def tokenize(s):
    return [ch for ch in s if not ch.isspace()]

def parse_formula(s):
    tokens = tokenize(s)
    pos = 0

    def parse_expr():
        return parse_equiv()

    def parse_equiv():
        nonlocal pos
        left = parse_implies()
        if pos < len(tokens) and tokens[pos] == '⇔':
            pos += 1
            right = parse_equiv()
            return ("iff", left, right)
        return left

    def parse_implies():
        nonlocal pos
        left = parse_or()
        if pos < len(tokens) and tokens[pos] == '⇒':
            pos += 1
            right = parse_implies()
            return ("implies", left, right)
        return left

    def parse_or():
        nonlocal pos
        left = parse_and()
        while pos < len(tokens) and tokens[pos] == '∨':
            pos += 1
            left = ("or", left, parse_and())
        return left

    def parse_and():
        nonlocal pos
        left = parse_not()
        while pos < len(tokens) and tokens[pos] == '∧':
            pos += 1
            left = ("and", left, parse_not())
        return left

    def parse_not():
        nonlocal pos
        if pos < len(tokens) and tokens[pos] == '¬':
            pos += 1
            return ("not", parse_not())
        return parse_atom()

    def parse_atom():
        nonlocal pos
        if tokens[pos] == '(':
            pos += 1
            exp = parse_expr()
            pos += 1
            return exp
        lit = tokens[pos]
        pos += 1
        return ("literal", lit)

    return parse_expr()

def eval_ast(ast, model):
    op = ast[0]
    if op == "literal":
        return model[ast[1]]
    if op == "not":
        return not eval_ast(ast[1], model)
    a = eval_ast(ast[1], model)
    b = eval_ast(ast[2], model)
    if op == "and":
        return a and b
    if op == "or":
        return a or b
    if op == "implies":
        return (not a) or b
    if op == "iff":
        return a == b

def get_symbols(ast):
    op = ast[0]
    if op == "literal":
        return {ast[1]}
    if op == "not":
        return get_symbols(ast[1])
    return get_symbols(ast[1]) | get_symbols(ast[2])

def find_model(formulas):
    asts = [parse_formula(f) for f in formulas if f.strip()]
    syms = set()
    for ast in asts:
        syms |= get_symbols(ast)
    syms = sorted(syms)
    for values in itertools.product([True, False], repeat=len(syms)):
        model = dict(zip(syms, values))
        if all(eval_ast(ast, model) for ast in asts):
            return model
    return None

def main():
    kb1 = [
        "A∨B",
        "¬A⇔¬B∨C",
        "¬A∨¬B∨C"
    ]
    model = find_model(kb1)
    if model:
        print("Model:", model)
    else:
        print("No satisfying assignment found.")
        
    kb2 = [
        "C⇔B∨D",
        "A⇒¬B∧¬D",
        "¬(B∧¬C)⇒A",
        "¬D⇒C"
    ]
    model = find_model(kb2)
    if model:
        print("Model:", model)
    else:
        print("No satisfying assignment found.")

if __name__ == "__main__":
    main()
