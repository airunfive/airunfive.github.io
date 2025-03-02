import re

'''
用户名规则：只能是大小写字母和数字，不能以数字开头，长度为5~12位
'''
def check_username(username):
    if len(username) < 5 and len(username) > 12:
        return False
    
    if username[0] >= '0' and username <= '9' :
        return False
    
    for char in username:
        if not (ord(char) in range(65, 91) or ord(char) in  range(97, 123) or ord(char) in range(48, 58)):
            return False
        else:
            return True

'''
密码规则：必须且只能由大小写字母和数字组成，长度为6~15位
'''
def check_password(password):
    if len(password) < 6 and len(password) > 15:
        return False
    
    large = 0
    small = 0
    num = 0
    other = 0
    for char in password:
        if not (ord(char) in range(65, 91) or ord(char) in range(97, 123) or ord(char) in range(48, 58)):
            return False
        if ord(char) in range(65, 91):
            large += 1
        elif ord(char) in range(97, 123):
            small += 1
        elif ord(char) in range(48, 58):
            num += 1
        else:
            other += 1

    if large < 1 and num < 1 and num < 1 and other > 0:
        return False
    else:
        return True

'''
电话号码规则：匹配中国电话号码，第一位为1，第二位需要在3到9之间，共11位
''' 
def check_phone(phone):
    number_regex=r'^1[3-9]\d{9}$'
    if re.match(number_regex, phone):
        return True
    else:
        return False


'''
测试代码范例
'''
# def check_function(func, expect, *args):
#     check = func(*args)
#     if check == expect:
#         print("功能%s：成功" % func.__name__)
#     else:
#         print("功能%s：失败" % func.__name__)

# check_function(check_username, True, 'sdkfjglj')
# check_function(check_username, False, '1UDUjj')
# check_function(check_password, True, 'abc1ABC')
# check_function(check_password, False, '*&*jfsdl')
# check_function(check_phone, True, '19859814518')
# check_function(check_phone, False, '29859814518')
# check_function(check_phone, False, '12859814518')