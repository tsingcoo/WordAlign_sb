def read_defs(input_f):
    word_def = {}
    with open(input_f, encoding='utf-8') as f:
        line = f.readline()  # 跳过第一行
        for line in f.readlines():
            line = line.strip()
            line_list = line.split("\t")
            word_def[line_list[0]] = line_list[1]
    print(word_def)
    print(len(word_def))


if __name__ == '__main__':
    read_defs("/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/defs.txt")
