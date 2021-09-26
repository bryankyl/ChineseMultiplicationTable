chineseDigits = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
chineseOrders = ["", "十", "百", "千", "萬"]


def to_chinese(num):
    # initialization
    num_to_str = str(num)
    number_of_digits = len(str(num))
    return_string = ""

    if num < 10:
        return_string = chineseDigits[num]
    elif num == 10:
        return_string = "十"
    elif number_of_digits == 2 and num_to_str[0] == "1":
        return_string = "十" + chineseDigits[int(num_to_str[1])]
    elif number_of_digits == 2 and num_to_str[1] == "0":
        return_string = chineseDigits[int(num_to_str[0])] + "十"
    else:
        for i in range(0, number_of_digits):
            if int(num_to_str[i]) != 0:
                if int(num_to_str[i-1]) == 0 and (num % 10) != 0:
                    return_string += "零"
                return_string += chineseDigits[int(num_to_str[i])]
                return_string += chineseOrders[number_of_digits-i-1]

    return return_string


for x in range(1, 10):
    print("   %s  " % to_chinese(x), end="\t\t\t")
print("")

for x in range(1, 10):
    for y in range(1, 10):
        if (x*y) < 10:
            print(" %s%s如%s " % (to_chinese(x), to_chinese(y), to_chinese(x * y)), end="\t\t")
        elif (x*y) == 10:
            print("%s%s得一%s" % (to_chinese(x), to_chinese(y), to_chinese(x * y)), end="\t\t")
        elif (x*y) < 20:
            print("%s%s一%s" % (to_chinese(x), to_chinese(y), to_chinese(x * y)), end="\t\t")
        elif ((x*y) % 10) == 0:
            print("%s%s中%s" % (to_chinese(x), to_chinese(y), to_chinese(x * y)), end="\t\t")
        else:
            print("%s%s%s" % (to_chinese(x), to_chinese(y), to_chinese(x*y)), end="\t\t")
    print("")
