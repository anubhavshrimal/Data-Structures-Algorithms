

def flatten_dict(initialVal, dictionary, flatDictionary):
    for key in dictionary:
        value = dictionary[key]
        if type(value) is not dict:
            if initialVal is None:
                flatDictionary[key] = value
            else:
                flatDictionary[initialVal + '.' + key] = value
        else:
            if initialVal is None:
                flatten_dict(key, value, flatDictionary)
            else:
                flatten_dict(initialVal + '.' + key, value, flatDictionary)


# iterative solution
def flatten_dict2(dictionary):
    flatDictionary = {}
    stack = [(dictionary, None)]
    while stack:
        d, path = stack.pop()

        for k, v in d.items():
            if path is None:
                newkey = k
            else:
                newkey = '.'.join([path, k])
            if isinstance(v, dict):
                stack.append((v, newkey))
            else:
                flatDictionary[newkey] = v
    return flatDictionary


if __name__ == '__main__':
    flatDictionary = {}
    dictionary = {
      'Key1': '1',
      'Key2': {
        'a': '2',
        'b': '3',
        'c': {
          'd': '3',
          'e': '1'
          }
        }
    }

    # recursive function call
    flatten_dict(None, dictionary, flatDictionary)

    # iterative function call
    f = flatten_dict2(dictionary)

    for k in f:
        print(k, ":", f[k])
