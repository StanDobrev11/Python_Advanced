lst = [5, 3, 2, 1, -7, 10, 'dadb', 'aabb', 'caab', 'dbaa', 'bbaa']


# lst.sort(reverse=True)
# print(lst)
#
# ll1 = ['dadb', 'aabb', 'caab', 'dbaa', 'bbaa']
#
# print(sorted(ll1, key=lambda x: x[1]))


def has_permission(page):
    def access(new_username):
        if new_username[0].upper() == "S":
            return f'This {new_username} has permission to {page}'
        else:
            return f'This {new_username} does not have permission to {page}'
    def permission(username):
        if username.lower() == 'admin':
            return f'This {username} has permission to {page}'
        else:
            return f'This {username} does not have permission to {page}'



    return  access or permission


print(has_permission('Admin page')(new_username='SADMIN'))

