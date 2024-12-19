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