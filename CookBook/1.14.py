# 排序不支持原生比较的对象
from operator import attrgetter


# 你想排序类型相同的对象，但是他们不支持原生的比较操作。
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


if __name__ == '__main__':
    print(sort_notcompare())
    users = [User(23), User(3), User(99)]
    print(sorted(users, key=attrgetter('user_id')))  # 运行更快

    print(min(users, key=attrgetter('user_id')))
    print(max(users, key=attrgetter('user_id')))



