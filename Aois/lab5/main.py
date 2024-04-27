import CreateSDNF
import MinimizedSDNF
table = [{'a': 0, 'b': 0, 'с': 0, 'result': 0},
{'a': 0, 'b': 0, 'с': 1, 'result': 1},
{'a': 0, 'b': 1, 'с': 0, 'result': 1},
{'a': 0, 'b': 1, 'с': 1, 'result': 0},
{'a': 1, 'b': 0, 'с': 0, 'result': 1},
{'a': 1, 'b': 0, 'с': 1, 'result': 0},
{'a': 1, 'b': 1, 'с': 0, 'result': 0},
{'a': 1, 'b': 1, 'с': 1, 'result': 1}]
table1 = [{'a': 0, 'b': 0, 'с': 0, 'result': 0},
{'a': 0, 'b': 0, 'с': 1, 'result': 0},
{'a': 0, 'b': 1, 'с': 0, 'result': 0},
{'a': 0, 'b': 1, 'с': 1, 'result': 1},
{'a': 1, 'b': 0, 'с': 0, 'result': 0},
{'a': 1, 'b': 0, 'с': 1, 'result': 1},
{'a': 1, 'b': 1, 'с': 0, 'result': 1},
{'a': 1, 'b': 1, 'с': 1, 'result': 1}]


cnf = MinimizedSDNF.string_to_cnf(CreateSDNF.truth_table_to_dnf(table))
knf_result = MinimizedSDNF.Quine_McCluskey(cnf)
knf_string = MinimizedSDNF.implicants_to_string(knf_result)
print(knf_string)  # Выводим строку КНФ
cnf = MinimizedSDNF.string_to_cnf(CreateSDNF.truth_table_to_dnf(table1))
knf_result = MinimizedSDNF.Quine_McCluskey(cnf)
knf_string = MinimizedSDNF.implicants_to_string(knf_result)
print(knf_string)  # Выводим строку КНФ