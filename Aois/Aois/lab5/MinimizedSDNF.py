def combine_implicants(implicant1, implicant2):
    diff_count = 0
    diff_index = -1
    for i in range(len(implicant1)):
        if implicant1[i] != implicant2[i]:
            diff_count += 1
            diff_index = i

    if diff_count == 1:
        return implicant1[:diff_index] + ['-'] + implicant1[diff_index + 1:]

    return None


def Quine_McCluskey(cnf):
    # Получаем список всех возможных переменных и их отрицаний
    variables = set()
    for clause in cnf:
        for literal in clause:
            variable = literal.replace('!', '')
            variables.add(variable)

    # Создаем таблицу импликантов
    prime_implicants = []
    for clause in cnf:
        prime_implicants.append(clause)

    # Выполняем минимизацию
    while True:
        new_prime_implicants = []
        for i in range(len(prime_implicants)):
            for j in range(i + 1, len(prime_implicants)):
                combined = combine_implicants(prime_implicants[i], prime_implicants[j])
                if combined:
                    new_prime_implicants.append(combined)

        if not new_prime_implicants:
            break

        prime_implicants = new_prime_implicants

    # Преобразуем результат в КНФ
    knf_result = []
    for implicant in prime_implicants:
        knf_clause = []
        for literal in implicant:
            knf_clause.append(literal)
        knf_result.append(knf_clause)

    return knf_result


def implicants_to_string(implicants):
    # Преобразуем список импликантов в строку КНФ
    knf_string = ' & '.join(['(' + ' | '.join(clause) + ')' for clause in implicants])
    return knf_string


def string_to_cnf(cnf_string):
    # Удаляем пробелы и разбиваем строку на конъюнкцию
    cnf_string = cnf_string.replace(' ', '')
    clauses = cnf_string.split('|')

    # Преобразуем каждую конъюнкцию в список литералов
    cnf = []
    for clause in clauses:
        literals = clause.strip('()').split('&')
        cnf.append(literals)

    return cnf


