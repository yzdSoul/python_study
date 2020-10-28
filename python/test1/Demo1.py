# import sys; x = 'runoob'; sys.stdout.write(x + '\n')
#
# x = "a"
# y = "b"
# # 换行输出
# print(x)
# print(y)
#
# print('---------')
# # 不换行输出
# print(x, end=" ")
# print(y, end=" ")
# print()
#
# import sys

# print ('参数个数为:', len(sys.argv), '个参数。')
# print ('参数列表:', str(sys.argv))
###########################################
# import sys, getopt
#
# def main(argv):
#    inputfile = ''
#    outputfile = ''
#    try:
#       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#    except getopt.GetoptError:
#       print ('Demo1.py -i <inputfile> -o <outputfile>')
#       sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print ('Demo1.py -i <inputfile> -o <outputfile>')
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg
#    print ('输入的文件为：', inputfile)
#    print ('输出的文件为：', outputfile)
#
# if __name__ == "__main__":
#    main(sys.argv[1:])

#####################################
# a,b,c,d = 20,5.5,True,3+4j
# print(type(a),type(b),type(c),type(d))

# def reverseWords(input):
#    inputWords= input.split(" ")
#
#    inputWords = inputWords[-1::-1]
#
#    output = ''.join(inputWords)
#
#    return output
#
# if __name__ == "__main__":
#    input = 'hello world'
#
#    rw = reverseWords(input)
#    print(rw)

#
# from sys import argv, path  # 导入特定的成员
#
# print('================python from import===================================')
# print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

#
# def a():
#    '''这是文档字符串'''
#    pass
#
#
# print(a.__doc__)
#斐波那契数列
# a, b = 1, 2
# while b < 1000:
#     print(b)
#     a, b = b, a+b


