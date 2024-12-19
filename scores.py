myFile = open('scores.txt','r')    # open scores.txt in reading mode
subjects = myFile.readline().strip().split(',')
subjects = [str(subject) for subject in subjects]  # generate a list of subjects
subjects = subjects[1:len(subjects)]   # get rid of name
# now initialize some monitors over performance a dictionary with key, the name of subject and value a list with name and grade
keys = subjects  # parse subjects to keys -- suffies
values = [[ '' , 0 ] for i in range(len(subjects)) ] # value structure as tuples or list to store name and best grade of best student at one subject
# wrap up a dictionary
my_dict = dict(zip(keys,values))
# now go over the rest of the lines: and see whos got the biggest scores ----- update accordingly
for line in myFile:
    content = line.strip().split(',')
    name = content[0]  # always the name is content[0] the first provided
    for i in range(1,len(content)):
        if int(content[i]) > my_dict[subjects[i-1]][1]:
            my_dict[subjects[i-1]][0] = name
            my_dict[subjects[i-1]][1] = int(content[i])

print('Highest Scores:')
for key , content_list in my_dict.items():
    print( key + ": " + content_list[0] + " " + "(" + str(content_list[1]) + ")" )
'''
'''
def edit_distance(str1, str2):
    # start by initializing a matrix with dimension: ( len(str1) , len(str2) )
    # matrices are columns repeated how many lines:
    dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
    # matrix created --- initialize first costs to 0 -> first line + first column
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            # go over each cell:
            operation_cost = 0 if str1[i-1] == str2[j-1] else 1
            # compartes what it would cost to change current letter in string1 to each letters in string2
            dp[i][j] = min( dp[i-1][j] + 1 , # isnertion
                            dp[i][j-1] + 1 , # deletion
                            dp[i-1][j-1] + operation_cost # substituion
                            )
    # in the end return the value in the bottom corner of the matrix, this is on the border created at initialization
    return dp[len(str1)][len(str2)]
print ( edit_distance( 'cat' , 'bat' ) )