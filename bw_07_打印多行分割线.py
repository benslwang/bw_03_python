"""
# 打印5行分割线
print_times = 0
while print_times < 5:
    def print_line(char, times):  # char表示一个字节
        print(char * times)


    print_line("-", 60)
    print_times += 1
"""

# 打印5行分割线
def print_line(char, times):
    """打印单行分割线

    :param char: 分割字符
    :param times: 重复次数
    """
    print(char * times)

def print_lines(char, times):
    """打印多行分割线

    :param char: 分割线使用的字符
    :param times: 分割线重复的次数
    """
    print_time = 0
    while print_time < 5:
        print_line(char, times)
        print_time += 1


name = 'ben wang'


# print_lines("-", 50)
