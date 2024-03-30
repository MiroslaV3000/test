def quine_mccluskey(minterms):
    prime_implicants = minterms.copy()
    while True:
        new_prime_implicants = []
        for i in range(len(prime_implicants)):
            for j in range(i+1, len(prime_implicants)):
                if can_merge(prime_implicants[i], prime_implicants[j]):
                    merged = merge(prime_implicants[i], prime_implicants[j])
                    if merged not in new_prime_implicants:
                        new_prime_implicants.append(merged)
        if not new_prime_implicants:
            break
        prime_implicants = new_prime_implicants
    return prime_implicants

def can_merge(a, b):
    diff_count = sum(1 for i, j in zip(a, b) if i != j)
    return diff_count == 1

def merge(a, b):
    merged = ''
    for i, (ai, bi) in enumerate(zip(a, b)):
        merged += '-' if ai != bi else ai
    return merged

def print_table(minterms, is_cnf=True):
    prime_implicants = quine_mccluskey(minterms)
    prime_implicants.sort()
    print("Prime Implicants:")
    for prime in prime_implicants:
        print(prime)
    print("\nFunction Output:")
    formatted_outputs = []
    for prime in prime_implicants:
        if is_cnf:
            # For CNF, we use '&' and '|' for AND and OR operations
            output = '(' + '|'.join([f"x{i+1}" if c == '1' else f"!x{i+1}" for i, c in enumerate(prime) if c != '-']) + ')'
        else:
            # For DNF, we use '|' and '&' for OR and AND operations
            output = '(' + '|'.join([f"x{i+1}" if c == '1' else f"!x{i+1}" for i, c in enumerate(prime) if c != '-']) + ')'
        formatted_outputs.append(output)
    final_output = '&'.join(formatted_outputs) if is_cnf else '|'.join(formatted_outputs)
    print(final_output)

def cnf_to_minterms(cnf_expression):
    products = cnf_expression.split('&')
    minterms = []
    for product in products:
        product = product.strip('()')
        variables = product.split('|')
        minterm_mask = ['0'] * len(variables)
        for variable in variables:
            index = int(variable.strip('x!')) - 1
            minterm_mask[index] = '1' if '!' not in variable else '0'
        minterms.append(''.join(minterm_mask))
    return minterms

def dnf_to_minterms(dnf_expression):
    sums = dnf_expression.split('|')
    minterms = []
    for sum_term in sums:
        sum_term = sum_term.strip('()')
        variables = sum_term.split('&')
        minterm_mask = ['0'] * len(variables)
        for variable in variables:
            index = int(variable.strip('x!')) - 1
            minterm_mask[index] = '1' if '!' not in variable else '0'
        minterms.append(''.join(minterm_mask))
    return minterms

def main():
    # Example CNF expression
    cnf_expression = "(x1|x2|x3)&(x1|x2|!x3)&(!x1|x2|x3)&(x1|!x2|x3)"
    minterms_cnf = cnf_to_minterms(cnf_expression)
    print("CNF to Minterms:")
    print_table(minterms_cnf, is_cnf=True)

    # Example DNF expression
    dnf_expression = "(!x1&x2&!x3)|(x1&!x2&!x3)|(x1&!x2&x3)|(x1&x2&!x3)|(!x1&x2&x3)"
    minterms_dnf = dnf_to_minterms(dnf_expression)
    print("\nDNF to Minterms:")
    print_table(minterms_dnf, is_cnf=False)

if __name__ == "__main__":
    main()