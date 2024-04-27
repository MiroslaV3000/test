import Create_Table
import Find_SKNF
import Find_CDNF
logical_function = "(!a & b) | с "
print(Find_SKNF.truth_table_to_cnf(Create_Table.truth_table(logical_function)))
print(Find_CDNF.truth_table_to_dnf(Create_Table.truth_table(logical_function)))
