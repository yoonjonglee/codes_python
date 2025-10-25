import sys

# input
str = "asgegsagefasg" # "gef"
#str = "aaaaaa"
#str = "asdeavfeva"
#str = "abcabcbb"

# code here
def find_longest_substring(str):
    l = 0; w = []; ml = 0; res = "" # initialize left pointer, window, max length and result
    
    # iterate through the string with right pointer
    for r in range(len(str)):
        # if character at right pointer is in window, move left pointer to right until it's not
        while str[r] in w: w.remove(str[l]); l += 1 
        w.append(str[r]) # add character at right pointer to window
        cl = r - l  + 1 # current length
        # update max length and result if current length is greater
        if cl > ml: 
            ml = cl # update max length
            res = str[l:r+1] # update result
        print(res)
    return res
    
sol = find_longest_substring(str)

#output
print(sol)