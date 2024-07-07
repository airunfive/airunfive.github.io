'''
csv自动读取器
'''
def read_csv(path, mode = 'r'):
    list = []
    with open(path, mode) as f:
        members = f.readlines()
    if not members:
        return False
    keys = members[0].strip().split(',')
    members = members[1:]
    
    for member in members:
        member = member.strip().split(',')
        dict={}
        for i in range(len(member)):
            dict[keys[i]] = member[i]
        list.append(dict)
    return list
# result = read_csv('./test.csv', 'r')
# print(result)