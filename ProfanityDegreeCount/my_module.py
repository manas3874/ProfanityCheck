
#! List of acceptable profanities which is mutable to make changes anytime
list_of_profanities=['abc','pqr','xyz']

#! An Abstract Data Type to store the user comment during degree_check
class Comment():
    """
        Comment is an ADT to store the current comment details and keep them secure until the end of execution of profanity check.

        arguments:
        1. user_id: here we have considered the name of a user, which will be the user_ID in a practical situation.
        2. comment: The actual comment (string) which will be checked for degree of profanity.

        functions:
        1. comment_details: This function will return a tuple (immutable) of required information. (further used by function-degree_check)
    """
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
        com=Comment(user,comment_dict[user]) #! com is the instance of our Comment class which is an ADT to store our comment details
        user_comment_details=com.comment_details()
        count=profanity_check(user_comment_details[1].lower())
        if 1<count<5:
            degree='medium'
        elif count>5:
            degree='high'

        #! using print here to output all the details. Should Ideally return an output to take an action.
        print(f'{user} has {count} profanities in the comment and the degree of profanity is {degree}')
