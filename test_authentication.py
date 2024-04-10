import authentication as au
  
def test_authentication():
    print('test for authentication')  
    print('-------------------')  
    print('check valid_passwords(),\nExpected result is: list that begins with 1024,1089... and ends with ...9604,9801')
    check_li = au.valid_passwords()
    print("Actual result is:")
    print(check_li)
    print('----')
    print('check valid_passwords() length == 55, Expected result is: printing approval')
    print("Actual result is:")
    if len(check_li) == 55:
        print('There are 55 numbers on the list')
    print('-------------------')
    x = {'Joh Smi':10642, 'jim ro':10648, 'Jam Bond':13824, 'Jan Jone':85184}
    print('check signup, Expected result is: Jam Bond:13824, Jan Jone:85184')
    print("Actual result is:")
    print(au.signup(x))
    print('-------------------')
    print('check login, Expected result is: Welcome printing and True ')
    u = 'John Smith'       
    p =  [1023, 1042, 1024]  
    d=  {'Jane Doe':1296, 'John Smith':1024}   
    print(au.login(u,p,d))
    print('----') 
    p =  [1023, 1042, 1420]  
    print('check login, Expected result is: error printing and False ')
    print(au.login(u,p,d))
    print('-------------------')
    print('-------------------') 
    print('end of test')   
    print('-------------------')
    print('-------------------')