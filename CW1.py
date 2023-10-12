def count_sheeps(sheep):
    amount = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            amount += 1
        else:
            amount += 0
    return amount


sheep_list = [True, True, True, False,
              True, True, True, True,
              True, False, True, False,
              True, False, False, True,
              True, True, True, True,
              False, False, True, True]

print(count_sheeps(sheep_list))



