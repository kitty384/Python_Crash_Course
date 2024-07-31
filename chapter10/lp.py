file_path = "D:\code\python\python-practice\chapter10\learning_python.txt"

with open(file_path, "r") as f:
    # first_method :整个读取
    print(f.read().strip()+"1")
    print("\n")
    # 按行读取
    for line in f:
        print(line.strip()+"2")
    # 列表读取
    lines = f.readlines()

for line in lines:
    print(line.strip()+"3")
