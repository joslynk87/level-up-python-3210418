
def index_all(search_list, item):
    indices = []
    for index, value in enumerate(search_list):
        # print(f"{index}: {value}")
        if value == item:
            indices.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item):
                print([index] + i)
                indices.append([index] + i)
    return indices

example = [[[1,2,3], 2, [1,3]], [1,2,3]]
print(index_all(example,2))