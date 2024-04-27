def truth_table_to_cnf(table):
    # Инициализируем список для хранения конъюнктов
    conjuncts = []

    # Проходим по каждой строке таблицы истинности
    for row in table:
        # Если результат ложно, добавляем конъюнкт
        if row['result'] == 0:
            # Создаем конъюнкт как дизъюнкцию отрицаний переменных, где переменная равна 1
            literals = [f'!{var}' if row[var] == 1 else var for var in row if var != 'result']
            # Добавляем скобки вокруг каждого конъюнкта
            conjunct = '(' + ' | '.join(literals) + ')'
            conjuncts.append(conjunct)

    # Объединяем все конъюнкты в одну строку, разделяя их дизъюнкциями
    cnf = ' & '.join(conjuncts)

    return cnf

