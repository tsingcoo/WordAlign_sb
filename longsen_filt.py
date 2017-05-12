# 输出长度大于100的句子的index
def filt(input_f, output_f):
    indexs = []
    index = 0  # 记录行下标
    with open(input_f, 'r')as fi, open(output_f, 'w')as fo:
        for line in fi.readlines():
            line_list = line.split(" ")
            if len(line_list) > 100:
                indexs.append(index)
                print(str(index) + " " + line)
                fo.write(str(index))
                fo.write('\n')

            index += 1
    return indexs


if __name__ == '__main__':
    indexs = filt("/Users/wangqinglong/Windows/800/LDC.ch", "/Users/wangqinglong/Windows/800/LDC.long.index.ch")
    print(len(indexs))
    print(indexs)
