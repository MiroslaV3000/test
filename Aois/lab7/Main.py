


def write_conjunction_word(matrix, column_index1, column_index2, new_column_index):
    # Считываем первое слово
    word1 = read_word_by_index(matrix, column_index1)

    # Считываем второе слово
    word2 = read_word_by_index(matrix, column_index2)

    # Выполняем побитовую операцию "И" над словами
    conjunction_word = ""
    for i in range(len(word1)):
        conjunction_word += str(int(word1[i]) & int(word2[i]))

    # Записываем результат в новый столбец
    matrix = write_word_to_column(matrix, conjunction_word, new_column_index)

    return matrix




def write_word_to_column(matrix, word, column_index):
    for row_index in range(len(matrix)):
        if row_index + column_index < len(matrix):
            matrix[row_index + column_index][column_index] = int(word[row_index])
        else:
            matrix[row_index + column_index - len(matrix)][column_index] = int(word[row_index])
    return matrix


def write_sheffer_word(matrix, column_index1, column_index2, new_column_index):
    # Считываем первое слово
    word1 = read_word_by_index(matrix, column_index1)

    # Считываем второе слово
    word2 = read_word_by_index(matrix, column_index2)

    # Выполняем операцию Шеффера над словами
    sheffer_word = ""
    for i in range(len(word1)):
        sheffer_word += str(1 - (int(word1[i]) & int(word2[i])))

    # Записываем результат в новый столбец
    matrix = write_word_to_column(matrix, sheffer_word, new_column_index)

    return matrix


def copy_and_paste_word(matrix, source_column_index, target_column_index):
    # Считываем слово из исходного столбца
    word_to_copy = read_word_by_index(matrix, source_column_index)

    # Вставляем слово в целевой столбец
    matrix = write_word_to_column(matrix, word_to_copy, target_column_index)

    return matrix


def copy_negate_and_paste_word(matrix, source_column_index, target_column_index):
    # Считываем слово из исходного столбца
    word_to_copy = read_word_by_index(matrix, source_column_index)

    # Отрицаем слово
    negated_word = ""
    for char in word_to_copy:
        negated_word += str(1 - int(char))

    # Вставляем отрицаемое слово в целевой столбец
    matrix = write_word_to_column(matrix, negated_word, target_column_index)

    return matrix


def find_nearest_value(matrix, target_value):
    nearest_value = None
    nearest_column = None

    for column_index in range(len(matrix[0])):
        word = read_word_by_index(matrix, column_index)

        gj0 = 0
        lj0 = 0

        for i in range(len(word) - 1, -1, -1):
            ai = int(target_value[i])
            Sji = int(word[i])

            gji = (gj0 or (not ai and Sji and not lj0))
            lji = (lj0 or (ai and Sji and gj0))

            gj0 = gji
            lj0 = lji

        if gj0 == 0 and lj0 == 0:
            if nearest_value is None or int(word, 2) < nearest_value:
                nearest_value = int(word, 2)
                nearest_column = column_index
        elif gj0 == 1 and lj0 == 0:
            if nearest_value is None or int(word, 2) > nearest_value:
                nearest_value = int(word, 2)
                nearest_column = column_index

    return nearest_column


def find_nearest_value_below(matrix, target_value):
    nearest_value = None
    nearest_column = None

    for column_index in range(len(matrix[0])):
        word = read_word_by_index(matrix, column_index)

        gj0 = 0
        lj0 = 0

        for i in range(len(word) - 1, -1, -1):
            ai = int(target_value[i])
            Sji = int(word[i])

            gji = (gj0 or (not ai and Sji and not lj0))
            lji = (lj0 or (ai and Sji and gj0))

            gj0 = gji
            lj0 = lji

        if gj0 == 0 and lj0 == 0:
            if nearest_value is None or int(word, 2) > nearest_value:
                nearest_value = int(word, 2)
                nearest_column = column_index
        elif gj0 == 0 and lj0 == 1:
            if nearest_value is None or (int(word, 2) < nearest_value and int(word, 2) > int(target_value, 2)):
                nearest_value = int(word, 2)
                nearest_column = column_index

    return nearest_column





def print_matrix(matrix):
    # Определяем максимальную ширину элемента в матрице
    max_width = max(len(str(cell)) for row in matrix for cell in row)

    # Форматируем и выводим каждую строку матрицы с разделителями
    for i, row in enumerate(matrix):
        formatted_row = '|'.join(f' {cell:{max_width}} ' for cell in row)
        border = '-' * (len(formatted_row) + 2)  # Добавляем границу сверху и снизу
        print(border)
        print(f'|{formatted_row}|')
        if i == len(matrix) - 1:  # Добавляем границу снизу для последней строки
            print(border)



# Создаем пустую матрицу 16x16
matrix = [[0 for _ in range(16)] for _ in range(16)]


matrix = write_word_to_column(matrix, "1001001100110011", 1)
print_matrix(matrix)
# Ищем слово в матрице
result = find_word(matrix, "1001001100110011")
