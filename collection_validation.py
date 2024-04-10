


def dict_validator(li,dic):
    key_to_del = []
    for key in dic:
        if dic[key] not in li :
           key_to_del.append(key)
    for x in key_to_del :
        dic.pop(x)
    return dic


if __name__ == '__main__':
    a = [1,2,3]
    b = {'a':1, 'd':8, 'u':3, 'k':3, 't':5}
    print('check a,b, Expected result is: a:1, u:3, k:3')
    print("Actual result is:")
    print(dict_validator(a,b))