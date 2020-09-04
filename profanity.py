"""
I have made use of BetterComments, a VScode extention, for better readability.

profanities in this code
1. abc
2. pqr
3. xyz
There are 3 degrees of profanity: low, medium and high.

"""

#! An Abstract Data Type to store the user comment during degree_check
class Comment():
    def __init__ (self,user_id,comment):
        self.user=user_id
        self.comment=comment

    def comment_details(self):

        #! RETURN A TUPLE TO AVOID MUTATION TO THE DATA DURING RUNTIME
        return (self.user,self.comment)


def profanity_check(comment_details):
    count=0
    for prof in list_of_profanities:

        #! will check the presence of profanities in the comment
        count+=comment_details.count(prof)
    return count

def degree_check(comment_dict):
    for user in comment_dict:
        degree='low'
        com=Comment(user,comment_dict[user])
        user_comment_details=com.comment_details()
        count=profanity_check(user_comment_details[1].lower())
        if 1<count<5:
            degree='medium'
        elif count>5:
            degree='high'

        #! using print here to output all the details. Should Ideally return an output to take an action.
        print(f'{user} has {count} profanities in the comment and the degree of profanity is {degree}')


#! simple dict to store few example comments
comment_dict={
    'jack':'hey, what are you doing this evening?', #0
    'mark': 'It is time for some xyz', #1
    'carl':"why would you abc from xyz and pqr", #3
    'john': 'is it already time for pqr', #1
    'maria':'why so abc abc and pqr xyz even after pqr pqr', #6
    'jade': 'I am so abc pqr xyz xyz abc xyz abc abc' #8
}

#! List of acceptable profanities which is mutable to make changes anytime
list_of_profanities=['abc','pqr','xyz']

#! only required function to check the degree of profanity. Can be named init() for this module so that it is easy to work from an external API
degree_check(comment_dict)
