# 创建文件，不能创建文件夹
fp = open("test.md", "w")  # 必须添加模式
fp.write("hello world")
fp.close()
