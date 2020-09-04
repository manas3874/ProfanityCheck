"""
I have made use of BetterComments, a VScode extention, for better readability.

Here we can test the code by the following methods:
1. Having the user type in an input to test it.
2. Making changes to the .txt file externally then reading it to find profanity degree.(';' separated data must be provided. The separation is between the user_id and the actual comment)

3. (NOT PROVIDED HERE) We can make queries to our database and use each user_ID and comment to check for profanity and take immediate action.

There are 3 degrees of profanity: low, medium and high.
A comment without any profanity will result in None
profanities in this code
low=['abc','pqr','xyz']
medium=['defg','hijk']
high=['qwerty','zxcvbn','asdfgh']

the highest degree of profanity will be the output
"""
import my_module
import module_for_individual_inputs


#! only required function to check the degree of profanity.
# Can be named init() for this module so that it is easy to work from an external API
def func_initial():
    
    print('\n\nHello user, Welcome to the profanity degree tester \nHow would you like to check the degree of profanity?\n\n')
    while True:

        inputdata=int(input('choose from\n1. Live input\n2. From your own tester.txt file (make sure file is externally written before running the code to avoid errors)\n'))
        if inputdata in range(1,3):
            print('\ninput is {} '.format(inputdata))
            break
        else:
            print('\n{} was not asked\n\ngive input again\n'.format(inputdata))

    return inputdata
a=func_initial()

if a==1:
    module_for_individual_inputs.tester()
elif a==2:
    print('Make sure the tester.txt file is ready')


    #! Reading the external file. 
    # will throw an error if the tester file is not ready
    file_of_comments=open('tester.txt','rt')

    #! simple dict to store few example comments.
    comment_dict={}

    #?The time complexity of running this for loop is O(n). In a practical situation we may need to optimise this code since the number of comments made on a daily basis are in the order of millions

    for line in file_of_comments:
        user_and_comment=line.split(';') #assuming no two users have the same name, ideally we will use user_ID in place of the name which is unique.
        comment_dict[user_and_comment[0]]=user_and_comment[1]

    my_module.degree_check(comment_dict)


