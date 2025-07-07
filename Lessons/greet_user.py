import sys

# 检查用户是否传入了足够多的参数
if len(sys.argv) > 1:
    # sys.argv[0] 是脚本名 'greet_user.py'
    # sys.argv[1] 是我们期望的第一个参数
    name = sys.argv[1]
    print(f"你好，{name}！欢迎来到命令行世界。")
else:
    print("错误：请输入你的名字作为参数！")
    print("用法: python greet_user.py [你的名字]")

# 让我们看看 sys.argv 到底是什么
print(f"\ Debug Info")
print(f"sys.argv 的内容是: {sys.argv}")
print(f"总共有 {len(sys.argv)} 个元素。")