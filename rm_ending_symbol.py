def rm_es(input_f, output_f):
    symbols = ['...','.', '?', '!', ',', '，', '。', '！', '？']
    with open(input_f, 'r', encoding='utf-8') as f1, open(output_f, 'w', encoding='utf-8') as f2:
        for line in f1.readlines():
            line_list = line.strip().split(" ")
            if line_list[-1] in symbols:
                line_list = line_list[:-1]
            if line_list[0] in symbols:
                line_list = line_list[1:]
            firstword = True
            for word in line_list:
                if firstword == True:
                    firstword = False
                else:
                    f2.write(" ")
                f2.write(word)
            f2.write('\n')


if __name__ == '__main__':
    rm_es(
        "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/collins_fl/examples_collins_fl.oneword.final.ch",
        "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/collins_fl/examples_collins_fl.oneword.nosym.final.ch")
    rm_es(
        "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/collins_fl/examples_collins_fl.oneword.notag.token.final.en",
        "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/collins_fl/examples_collins_fl.oneword.notag.token.nosym.final.en")
