import my_module
def tester():
    print('\nPlease provide a string of comment to check for profanity degree\n\n')

    while True:
        test_string=input('\nEnter your comment here\n')
        degree=my_module.profanity_check(test_string.lower())
        print(f'\nThe degree of profanity is {degree}\n\nHave another string to test?\n')
        
        while True:

            test_again=input('1. Yes\n2. No\n')
            if test_again=='1':
                break
            elif test_again=='2':
                print('Thanks for testing')
                return None
            else:
                print('invalid input')

