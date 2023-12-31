# 通过某个关键字排序一个字典列表
from operator import itemgetter

# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# 根据任意的字典字段排序
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# 支持多个key
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

rows_by_fname = sorted(rows, key=lambda r: r['fname'])  # itemgetter运行更快
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))


print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))


