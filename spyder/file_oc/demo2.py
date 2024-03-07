# fp = open("mymodule.txt", "w")
# fp.write("# hello\n*****\n" * 5)
fp1 = open("test.txt", "r")
# content = fp1.read()    # 似乎只能读文本文档     read是一字节一字节读，效率很低
# content1 = fp1.readline()   # 一行一行读,但只能读一行
content1 = fp1.readlines()      # 每行为列表中的一个成员
# ['# hello\n', '*****\n', '# hello\n', '*****\n', '# hello\n', '*****\n', '# hello\n', '*****\n', '# hello\n',
# '*****\n']
# print(content)
print("-----------------------")
print(content1)
fp1.close()
# fp.close()
