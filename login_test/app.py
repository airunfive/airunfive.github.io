from input import*

def do_reg():
    i = '1'
    users=[]
    
    while(i == '1'):
        username = input_username()
        password = input_password()
        phone = input_phone()
        user = {'username': username, 'password': password, 'phone': phone}
        users.append(user)
        print('还需要创建用户吗？')
        i = input('输入1继续,输入0退出')
    
    keys = users[0].keys()
    with open('./test.csv','a+') as f:
        for row in users:
            value = [row.get(key, '') for key in keys]
            f.write('\n'+','.join(value))

def do_login():
    username = input("请输入用户名：")
    user = select_user(username)
    if user == None:
        print('未找到用户')
        return 
    
    password = input("请输入密码：")
    if user['password'] == password:
        print("登入成功")


'''
修改密码，因为Python中没有直接在文本特定位置修改的功能，只能实现全部读入后统一操作再覆写
只适用于文件较小的写法
'''
def do_change():
    list = read_csv('./test.csv', 'r')
    username = input("请输入用户名：")
    lt = list[0].keys()
    key = next(iter(lt))
    for dict in list:
        if dict[key] == username:
            old_pass = input("请输入旧密码：")
            if dict['password'] == old_pass:
                print('匹配成功')
                new_pass = input("请输入新密码：")
                dict['password'] = new_pass
                break
        else:
            print('未找到用户')
            return 
    lt = list[0].keys()
    with open('./test.csv','w') as f:
        f.write('username,password,phone')
        for dict in list:
            value = [dict.get(key, '') for key in lt]
            f.write('\n'+','.join(value))
        
def menu():
    print("***********欢迎使用用户管理系统***********")
    print('''
    1、注册用户
    2、登入用户
    3、修改密码
    4、退出
    ''')
    choice = input("请输入1|2|3|4：")
    if choice == '1':
        do_reg()
        menu()
    elif choice == '2':
        do_login()
        menu()
    elif choice == '3':
        do_change()
        menu()
    elif choice == '4':
        exit(0)
    else:
        print('请输入1~4之间的数')
        menu()

def main():
    menu()


if __name__ == '__main__':
    main()