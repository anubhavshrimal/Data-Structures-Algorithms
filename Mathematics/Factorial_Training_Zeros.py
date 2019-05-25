# Find the number of trailing zeros present in the factorial of a number n.

def fact_trailing_zeros(num):
    c = 5 
    count = 0 

    # count number of factors of 5 possible in num!
    # 5 paired with 2 will give 10 i.e. 1 trailing zero
    # powers of 5 will give multiple zeros
    while num // c != 0: 
        count += num // c 
        c *= 5
    
    return count

num = 1000
print(f"{num}! has {fact_trailing_zeros(num)} trailing zeros")
