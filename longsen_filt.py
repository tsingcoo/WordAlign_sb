# coding:utf-8

default_encoding = 'utf-8'


# 输出长度大于100的句子的index
def filt(input_f, output_f):
    indexs = []
    index = 0  # 记录行下标
    with open(input_f, 'r', encoding='utf-8') as fi, open(output_f, 'w', encoding='utf-8') as fo:
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
    indexs = filt(
        "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/collins_fl/examples_collins_fl.oneword.notag.token.en",
        "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/collins_fl/examples_collins_fl.oneword.notag.token.en.long.index")
    print(len(indexs))
    print(indexs)
