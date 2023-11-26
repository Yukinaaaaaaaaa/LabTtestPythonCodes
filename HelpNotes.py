Please help me im under the water

Important codes to remember :
cd "C:\Local_Git_Repository" = change directory
mdkir = make directory
git init = to install the necessary git requirements to allow it to push
git branch = see the required branch
git branch checkout "___" = set the specific branch
git diff = to see the difference
git merge = to combine it together
git add 
git commit -m "Enter message" 
git remote add origin <GitHub repository URL> = to initiate the start of pushing origin
git remote -v = check the github its pushing to
git push --set-upstream origin master = pushing it to master branch
git push -u origin = pushing it to github
git tag -a v1.0 -m "Initial release v1.0" = to initialise the tag n prep to push
git push origin v1.0 = push tag
git submodule add <Git submodule repository URL>= adding of submodules
cd c:\clone_repo = cloning of git
git clone <URL of repository to clone> = cloning the specific url
git log = view and verify history

assert = assert is like saying, "I expect this statement to be true."
If the statement after assert is true, everything is fine.
If it's false, Python raises an error to let you know something unexpected happened.

Code example :
def test_Not_pure_integer_array():
    print("")
    input_arr = [3, 2, 1, 6, 7.7, 4, 5]  # Contains non-integer element
    answer = 2

    result = Lab3ex2.bubble_sort(input_arr, SORT_DESCENDING)
    assert (result == answer)


Dictionary Key = It's like a label or name for a specific piece of information.

Example:

In price_list, the keys are the names of fruits like 'apple', 'orange', etc.
Dictionary Value: It's the actual information associated with the key.

Example:

In price_list, the values are the prices of the corresponding fruits.
So, think of a dictionary like a collection of labeled information, where each label (key) is unique, and you can use these labels to quickly find and retrieve specific pieces of information (values). In your code, the dictionaries are used to store prices and quantities for different fruits.

code example:
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }


import (______)
is to import something from the same python file but different page
Example code : 





