def ranking(struct):
    for ind, key in enumerate(struct):
        ind += 1
        key['num'] = ind


def sort_by_rating(struct):
    return sorted(struct, key=lambda k: k['rating'], reverse=True)


def procedure(struct):
    struct = sort_by_rating(struct)
    ranking(struct)
    return struct


array = [{'num': 2, 'rating': 9.4}, {'num': 6, 'rating': 7.8}, {'num': 3, 'rating': 8.6}]
print(array)
array = sort_by_rating(array)
print(array)
ranking(array)
print(array)

new_item = {'num': 100, 'rating': 9.8}
array.append(new_item)
print(array)

array = procedure(array)
print(array)
