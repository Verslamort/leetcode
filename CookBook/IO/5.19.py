# 创建临时文件和文件夹
import tempfile
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory

# 你需要在程序执行时创建一个临时文件或目录，并希望使用完之后可以自动销毁掉。
with TemporaryFile('w+t') as f:
    # 读取/写入文件
    f.write('Hello World\n')
    f.write('Testing\n')
    # 从头开始查找并读取数据
    f.seek(0)
    data = f.read()
    # 临时文件已销毁


with NamedTemporaryFile('w+t') as f:  # delete=False
    print('filename is:', f.name)


# 创建一个临时目录
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)

# 更低级别，可以使用 mkstemp()和mkdtemp()
print(tempfile.mkstemp())
print(tempfile.mkdtemp())
print(tempfile.gettempdir())

# 自定义目录及命名规则
f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='D:/python_work/Leetcode/CookBook/IO')
print(f.name)







