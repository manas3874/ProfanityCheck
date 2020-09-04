"""
I have made use of BetterComments, a VScode extention, for better readability.

profanities in this code
1. abc
2. pqr
3. xyz

There are 3 degrees of profanity: low, medium and high.

In this version of the code, we consider the number of profanities used within a comment to judge the degree of profanity.
"""
import my_module

#! Reading the external file.
file_of_comments=open('tester.txt','rt')

#! simple dict to store few example comments.
comment_dict={}

#?The time complexity of running this for loop is O(n). In a practical situation we may need to optimise this code since the number of comments made on a daily basis are in the order of millions

for line in file_of_comments:
    user_and_comment=line.split(';') #assuming no two users have the same name, ideally we will use user_ID in place of the name which is unique.
    comment_dict[user_and_comment[0]]=user_and_comment[1]

#! only required function to check the degree of profanity.
# Can be named init() for this module so that it is easy to work from an external API
my_module.degree_check(comment_dict)
