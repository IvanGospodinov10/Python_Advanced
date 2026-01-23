def kwargs_length(**kwargs):
    length_dict = len(kwargs)

    return length_dict


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))
