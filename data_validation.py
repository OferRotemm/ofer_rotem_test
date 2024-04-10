def num_length(num):
    if len(str(num)) == 4 :
        return True
    else :
        return False

def is_square(num):
    for n in  range(num) :
        if n*n == num :
            return True
    else :
        return False

def valid_name(x):
    x = x.split()
    if len(x) == 2 :
        if x[0] == x[0].capitalize() and x[1] == x[1].capitalize():
            return True
        else:
            return False
    else :
        return False


def even_odd_digits(num):
    num = str(num)
    odd_count = 0
    even_count = 0
    for n in num:
        if int(n) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count >= odd_count :
        return True
    else :
        return False
    

        




if __name__ == '__main__':
    print('check less than 4 digits, Expected result is: False')
    print("Actual result is:")
    print(num_length(67))
    print('----')
    print('check more than 4 digits, Expected result is: False')
    print("Actual result is:")
    print(num_length(67569))
    print('----')
    print('check 4 digits, Expected result is: True')
    print("Actual result is:")
    print(num_length(6754))
    print('-------------------')
    print('check number 4, Expected result is: True')
    print("Actual result is:")
    print(is_square(4))
    print('----')
    print('check number 9, Expected result is: True')
    print("Actual result is:")
    print(is_square(9))
    print('----')
    print('check number 8, Expected result is: False')
    print("Actual result is:")
    print(is_square(8))
    print('-------------------')
    print('check \'Ofer Rotem\', Expected result is: True')
    print("Actual result is:")
    print(valid_name('Ofer Rotem'))
    print('----')
    print('check \'Ofer rotem\', Expected result is: False')
    print("Actual result is:")
    print(valid_name('Ofer rotem'))
    print('----')
    print('check \'ofer Rotem\', Expected result is: False')
    print("Actual result is:")
    print(valid_name('ofer Rotem'))
    print('----')
    print('check \'ofer rotem\', Expected result is: False')
    print("Actual result is:")
    print(valid_name('ofer rotem'))
    print('----')
    print('check \'Ofer Nir Rotem\', Expected result is: False')
    print("Actual result is:")
    print(valid_name('Ofer Nir Rotem'))
    print('----')
    print('check \'OferRotem\', Expected result is: False')
    print("Actual result is:")
    print(valid_name('OferRotem'))
    print('----')
    print('check \'Ofer\', Expected result is: False')
    print("Actual result is:")
    print(valid_name('Ofer'))
    print('-------------------')
    print('check 33, Expected result is: False')
    print("Actual result is:")
    print(even_odd_digits(33))
    print('----')
    print('check 491, Expected result is: False')
    print("Actual result is:")
    print(even_odd_digits(491))
    print('----')
    print('check 10, Expected result is: True')
    print("Actual result is:")
    print(even_odd_digits(10))
    print('----')
    print('check 122, Expected result is: True')
    print("Actual result is:")
    print(even_odd_digits(122))
    print('----')
    print('check 0, Expected result is: True')
    print("Actual result is:")
    print(even_odd_digits(0))
    print('----')
    print('check 184, Expected result is: True')
    print("Actual result is:")
    print(even_odd_digits(184))
    print('----')

