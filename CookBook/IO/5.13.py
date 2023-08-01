# 获取文件夹中的文件列表
import glob
import os
from fnmatch import fnmatch

# 你想获取文件系统中某个目录下的所有文件列表。
names = os.listdir('D:/python_work/Leetcode/CookBook/IO')
print(names)

# 你需要通过某种方式过滤数据
# Get all regular files
names = [name for name in os.listdir('D:/python_work/Leetcode/CookBook/IO')
         if os.path.isfile(os.path.join('D:/python_work/Leetcode/CookBook/IO', name))]
# Get all dirs
dirnames = [name for name in os.listdir('D:/python_work/Leetcode/CookBook/IO')
            if os.path.isdir(os.path.join('D:/python_work/Leetcode/CookBook/IO', name))]

# 文件名的匹配
pyfiles = glob.glob('D:/python_work/Leetcode/CookBook/IO/*.py')
pyfiles = [name for name in os.listdir('D:/python_work/Leetcode/CookBook/IO')
           if fnmatch(name, '*.py')]


# 文件大小，修改时间等
pyfiles = glob.glob('*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]
for name, size, mtime in name_sz_date:
    print(name, size, mtime)
# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
