from itertools import product


def minimize_cnf(cnf_str):
    # Parse the CNF string into a list of clauses
    clauses = cnf_str.split('&')
    clauses = [clause.strip('()').split('|') for clause in clauses]

    # Create a list of all possible variable assignments
    variables = set()
    for clause in clauses:
        for literal in clause:
            variables.add(literal.strip('!'))

    # Initialize the minimized CNF as the original CNF
    minimized_cnf = clauses.copy()

    # Iterate over all possible variable assignments
    for assignment in product([True, False], repeat=len(variables)):
        # Create a dictionary of variable assignments
        var_assignment = {var: assignment[i] for i, var in enumerate(sorted(variables))}

        # Evaluate the CNF with the current assignment
        is_satisfied = all(evaluate_clause(clause, var_assignment) for clause in clauses)

        # If the current assignment makes the CNF unsatisfiable, remove it from the minimized CNF
        if not is_satisfied:
            minimized_cnf = [clause for clause in minimized_cnf if not evaluate_clause(clause, var_assignment)]

    # Convert the minimized CNF back to a string format
    minimized_cnf_str = '&'.join(['(' + '|'.join(clause) + ')' for clause in minimized_cnf])
    return minimized_cnf_str


def evaluate_clause(clause, var_assignment):
    # Evaluate a clause given a variable assignment
    for literal in clause:
        var = literal.strip('!')
        is_negated = literal.startswith('!')
        if (var_assignment[var] and not is_negated) or (not var_assignment[var] and is_negated):
            return True
    return False


# Example usage:
cnf_str = "(x1|x2|x3)&(x1|x2|!x3)&(!x1|x2|x3)&(x1|!x2|x3)"
minimized_cnf_str = minimize_cnf(cnf_str)
print(minimized_cnf_str)