import data_validation as d
import collection_validation as v

def valid_passwords():
    valid_li = []
    for num in range(1024,9802):
        if d.num_length(num) and d.is_square(num) and d.even_odd_digits(num):
            valid_li.append(num)
    return valid_li


def signup(d):
    ok_li = valid_passwords()
    new_dic = v.dict_validator(ok_li, d)
    invalid = []
    for key in new_dic:
        if not d.valid_name(key) :
             invalid.append(key)
    for key in invalid:
        new_dic.pop(key)
    return new_dic
        

def login(username, password_attempts, users_data):
    if username in users_data:
        for p in password_attempts:
            if p == users_data[username] :
                print('Welcome')
                return True
        print('error')
        return False     
    else:
        print('You do not have a username\nPlease register')
        return None
        



if __name__ == '__main__':
    print('check valid_passwords(),\nExpected result is: list that begins with 1024,1089... and ends with ...9604,9801')
    check_li = valid_passwords()
    print("Actual result is:")
    print(check_li)
    print('----')
    print('check valid_passwords() length, Expected result is: printing approval')
    print("Actual result is:")
    if len(check_li) == 55:
        print('There are 55 numbers on the list')
    print('-------------------')
    x = {'Joh Smi':10642, 'jim ro':10648, 'Jam Bond':13824, 'Jan Jone':85184}
    print('check signup, Expected result is: Jam Bond:13824, Jan Jone:85184')
    print("Actual result is:")
    print(signup(x))
    print('-------------------')
    print('check login, Expected result is: Welcome printing and True ')
    u = 'John Smith'       
    p =  [1023, 1042, 1024]  
    d=  {'Jane Doe':1296, 'John Smith':1024}   
    print(login(u,p,d))
    print('----') 
    p =  [1023, 1042, 1420]  
    print('check login, Expected result is: error printing and False ')
    print(login(u,p,d))
    
    
    
    
    
    
    