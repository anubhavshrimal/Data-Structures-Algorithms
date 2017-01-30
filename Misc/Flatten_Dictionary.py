

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

    flatten_dict(None, dictionary, flatDictionary)

    for k in flatDictionary:
        print(k, ":", flatDictionary[k])
