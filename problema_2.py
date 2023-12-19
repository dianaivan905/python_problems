# Make a join - inner join mai precis - intre cele 2 tabele, - manual join
#
table1 = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'}
]

table2 = [
    {'id': 1, 'occupation': 'Engineer'},
    {'id': 2, 'occupation': 'Doctor'}
]

# #Expected output
#
# [
#     {'id': 1, 'name': 'Alice', 'occupation': 'Engineer'},
#     {'id': 2, 'name': 'Bob', 'occupation': 'Doctor'}
# ]
# table2 = {
#     '1': {'occupation': 'Engineer'},
#     '2': {'occupation': 'Doctor'}
# }

from copy import deepcopy


def join_tables(table1, table2, key):

  table2_dict = {}
  result_table = []

  for item in table2:
      item_key = str(item[key])
      item.pop(key)
      table2_dict[item_key] = item

  print(table2_dict)

  for item in table1:
      item_key = str(item[key])
      if item_key in table2_dict.keys():
          item.update(table2_dict[item_key])
          result_table.append(item)

  return result_table


key = 'id'
joined_data = join_tables(table1, table2, key)
print(joined_data)