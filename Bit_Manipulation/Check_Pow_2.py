# Check whether a given number n is a power of 2 or 0


def check_pow_2(num):
    if num == 0:
        return 0

    if num & (num - 1) == 0:
        return 1

    return -1


switch = {
    0: "Number is 0",
    1: "Number is a power of 2",
    -1: "Number is neither a power of 2 nor 0"
}
case = check_pow_2(16)

print(switch[case])
