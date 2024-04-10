import collection_validation as v

def test_collection_validation():
    print('test for collection_validation')
    print('-------------------') 
    a = [1,2,3]
    b = {'a':1, 'd':8, 'u':3, 'k':3, 't':5}
    print('check a,b, Expected result is: a:1, u:3, k:3')
    print("Actual result is:")
    print(v.dict_validator(a,b))
    print('-------------------')
    print('-------------------')