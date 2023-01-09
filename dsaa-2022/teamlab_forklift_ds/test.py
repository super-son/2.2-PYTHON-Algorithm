import teamlab_forklift_ds as ds
filename = "forklist_move.csv"
dataset = ds.load_dataset(filename)
sorted_result = ds.sort_dataset(dataset)
result = ds.build_linkedlistbag(sorted_result)
for node in result['TEAM10054239']:
    print(node)
# print(len(result['TEAM10054239']))
# test_bag = ds.LinkedListBag()
# test_bag.append(ds.ForkliftNode("test지게차", 2323.2323, 11515.1515, "2000-01-01 08:30:50.590"))
# test_bag.insert(ds.ForkliftNode("test지게차2", 2324.2343, 11525.1523, "2000-01-01 08:30:50.591"),2)
# test_bag.remove("2000-01-01 08:30:50.590")
# print(len(test_bag))
# print(iter(test_bag))
# print(result['TEAM10054239'])

# forklift_name = 'TEAM10054239'
# node_info = sorted_result[forklift_name][0]
# node = ds.ForkliftNode(forklift_name, node_info[0], node_info[1], node_info[2])
# print(node)
# print(result)
# for idx, i in enumerate(result):
#     print(i)
#     if idx > 6:
#         break
# print(result)
# print(result.len())
# print(result.iter())


