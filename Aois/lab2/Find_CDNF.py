def truth_table_to_dnf(table):
    # Инициализируем список для хранения дизъюнктов
    disjuncts = []

    # Проходим по каждой строке таблицы истинности
    for row in table:
        # Если результат истинен, добавляем дизъюнкт
        if row['result'] == 1:
            # Создаем дизъюнкт как конъюнкцию переменных, где переменная равна 0
            literals = [f'!{var}' if row[var] == 0 else var for var in row if var != 'result']
            # Добавляем скобки вокруг каждого дизъюнкта
            disjunct = '(' + ' & '.join(literals) + ')'
            disjuncts.append(disjunct)

    # Объединяем все дизъюнкты в одну строку, разделяя их конъюнкциями
    dnf = ' | '.join(disjuncts)

    return dnf
