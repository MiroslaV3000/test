def truth_table(expression):
    # Define the variables
    variables = sorted(set(i for i in expression if i.isalpha()))
    n = len(variables)

    # Initialize the truth table as a list of dictionaries
    table = []

    # Generate the truth table
    for i in range(2**n):
        # Convert i to binary and pad with zeros
        values = bin(i)[2:].zfill(n)

        # Replace the variables in the expression with the values
        local_expression = expression
        for var, val in zip(variables, values):
            local_expression = local_expression.replace(var, str(int(val)))

        # Replace the logical operators
        local_expression = local_expression.replace('&', ' and ').replace('|', ' or ').replace('!', ' not ').replace('->', '<=').replace('~', ' not ')

        # Evaluate the expression
        result = eval(local_expression)

        # Create a dictionary for the row and append it to the table
        row = {var: int(val) for var, val in zip(variables, values)}
        row['result'] = int(result)
        table.append(row)

    # Return the truth table
    for row in table:
        print(row)

    return table
