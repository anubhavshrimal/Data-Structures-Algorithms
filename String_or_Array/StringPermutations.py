# To print all permutations of a given string

count = 0

def permutations(mat, l, r):
    if l == r:
        print(''.join(mat))
        global count
        count += 1
    else:
        for i in range(l, r+1):
            mat[l], mat[i] = mat[i], mat[l]
            permutations(mat, l+1, r)
            mat[l], mat[i] = mat[i], mat[l]


string  = "ABC"
permutations(list(string), 0, len(string)-1)
print('total permutations:', count)