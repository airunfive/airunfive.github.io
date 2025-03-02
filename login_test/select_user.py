from read_csv import* 

def select_user(username):
    list = read_csv('./test.csv', 'r')
    if list == False:
        return False
    lt = list[0].keys()
    key = next(iter(lt))
    for dict in list:
        if dict[key] == username:
            return dict
        else:
            return None