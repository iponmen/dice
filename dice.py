def gen_dice(sides, num):
    # (int, int)-->list(list)
    # by numbering all the possible dice combanations just converted it to base 6 for example to make all combonations 
    # of base 6 numbers like how 1-99 is all the combonations of 2 "10-sided" values 
    grid = range(sides**num)
    add_1_to_all = lambda i: list(map(lambda j:j+1,i))
    grid = list(map(lambda i: base_converter_dice(i,sides), grid))
    grid = list(map(lambda i: size_consintency(num,i), grid))
    grid = list(map(lambda i: add_1_to_all(i), grid))
    # return list(map(lambda i: list(map(lambda j:j+1, size_consintency( num,base_converter_dice(i,sides) ))), range(sides**num)))
    return grid

def size_consintency(size, arrayx):
    # takes in a list and makes it longer with zeros
    # take in (int size, list arrayx)
    # returns list len(list)==size
    subx = size - len(arrayx)
    for i in range(subx):
        arrayx.insert(0, 0)
    return arrayx

def base_converter_dice(num, base):
    # (int, int) --> list
    # converts num to a based num of base "base" ex.bcd(4,2) --> [1,0,0]
    x=[]
    for i in range(num):
        x.insert(0, num % base)
        num = num//base
        if(num == 0):
            break
    return x

def check_sucsess_rate(dice_table, dc):
    # (Dice, int) --> float
    # tells dc (succsess number) rate of this dice table made from the gen_dice funk

    size = len(dice_table)
    total_passes = 0
    for i in dice_table:
        for j in i:
            if(j >= dc):
                total_passes += 1
                break
    return(total_passes/size)

print(gen_dice(6, 2))

print(check_sucsess_rate(gen_dice(20, 2), 10))
