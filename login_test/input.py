from check import *
from select_user import *

def input_username():
    username = input("请输入用户名（大小写字母和数字，不以数字开头）：")
   
    if  select_user(username):
        print('用户名已存在')
        username = input_username()
        return username
    
    result = check_username(username)
    if result == True:
        print("格式正确")
        return username
    else:
        print("格式错误，请重新输入：")
        username = input_username()
        return username

def input_password():
    password = input("请输入密码（大小写字母和数字组合）：")
    result = check_password(password)
    if result == True:
        print("格式正确")
        return password
    else:
        print("格式错误，请重新输入：")
        password = input_password()
        return password
    
def input_phone():
    phone = input("请输入电话（中国号码 +86）：")
    result = check_phone(phone)
    if result == True:
        print("格式正确")
        return phone
    else:
        print("格式错误，请重新输入：")
        phone = input_phone()
        return phone
