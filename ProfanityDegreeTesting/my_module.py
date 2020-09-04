
#! List of acceptable profanities which is mutable to make changes anytime
dict_of_profanities={
    'low':('abc','pqr','xyz'),
    'medium':('defg','hijk'),
    'high':('qwerty','zxcvbn','asdfgh')
}

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
    degrees=('high','medium','low') #to iterate through the dict
    #reversed order of degrees because if we find HIGH then we need not check lower order profanities
    for degree in degrees:
        for prof in dict_of_profanities[degree]:
            if prof in comment_details:
                return degree


def degree_check(comment_dict):
    for user in comment_dict:
        com=Comment(user,comment_dict[user]) #! com is the instance of our Comment class which is an ADT to store our comment details
        user_comment_details=com.comment_details()
        degree=profanity_check(user_comment_details[1].lower())

        #! using print here to output all the details. Should Ideally return an output to take an action.
        print(f'The degree of profanity is {degree} for {user}')
