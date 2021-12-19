import re
import random

divisor = 13

def generate_random_num(mod_num):
    if mod_num >= 6:
        max_num = 5
    else:
        max_num = mod_num
    randam_num = random.randint(0, max_num)
    return randam_num

def encrypt_data(target):
    '''
    暗号化。
    Args:
        target(string):暗号化する文字列
    Returns:
        result(string):暗号化した文字列
    '''
    
    # 文字を数値に変換する
    char_list = list(target)
    char_ord_list = []
    for char_ord in char_list:
        char_ord_list.append(ord(char_ord))

    # 暗号化
    div_list = []
    mod_list = []
    mod_dic = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F"}
    str_list = []
    for num in char_ord_list:
        div_list.append(num//divisor)
        mod_list.append(num%divisor)
    for count,mod_num in enumerate(mod_list):
        str_list.append(str(div_list[count]))
        randam_num = generate_random_num(mod_num)
        mod_num = mod_num - randam_num
        str_list.append(mod_dic[randam_num])
        while(mod_num >= 1):
            randam_num = generate_random_num(mod_num)
            mod_num = mod_num - randam_num
            str_list.append(mod_dic[randam_num])

    # リスト内結合
    result = ''.join(str_list)
    return result

def decryption_data(target):
    '''
    復号化。
    Args:
        target(string):復号化する文字列
    Returns:
        result(string):復号化した文字列
    '''
    
    # 文字列を分割
    strs_list = []
    while len(target) != 0:
        tmp = []
        num_match = re.match("[0-9]*",target).group()
        tmp.append(num_match)
        target = target.lstrip(num_match)
        str_match = re.match("[a-zA-Z]*",target).group()
        tmp.append(str_match)
        target = target.lstrip(str_match)
        strs_list.append(tmp)
    # 空を削除
    strs_list = list(filter(None, strs_list))
    # 文字列を数値にする
    mod_dic = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
    nums_list = []
    for strings in strs_list:
        nums = []
        for string in strings:
            mod_total = 0
            if string.isdecimal():
                nums.append(int(string) * divisor)
            else:
                char_list = list(string)
                for char in char_list:
                    mod_total += int(mod_dic[char])
            if string == strings[-1]:
                nums.append(mod_total)
                nums_list.append(nums)
    # 復号
    result = ""
    for nums in nums_list:
        result += chr(sum(nums))
    return result
