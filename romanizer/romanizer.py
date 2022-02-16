def descomponer (num: int, array: list, callback = lambda digit, index: digit):
    if not num//10:
        array.insert(0,callback(num, len(array)))
    else:
        array.insert(0,callback(num%10, len(array)))
        descomponer(num//10,array, callback)

def romanize (num:int)->str:

    romans = [
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "M", "MM", "MMM"]

    ]
    
    descomponer(num, array:=[], lambda d, i:romans[i][d])
    return "".join(array)

