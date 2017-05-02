# coding:utf-8

def split_en_ch(filename):
    # i = 0
    en = []
    with open(filename, 'r') as f:
        line = f.readline()  # 跳过第一行
        for line in f.readlines():
            # i += 1
            # if i < 100:
            # print(line.split('\t')[0])
            en.append(line.split('\t')[0])
    return en


def get_key_words(en):
    many_word_line = 0
    for line in en:
        # print(line)
        words = line.split(" ")
        i = 0
        for word in words:
            if "<vocab>" in word:
                i += 1
        if i > 1:
            print(line)
            print(i)
            many_word_line += 1
    print(many_word_line)


def main():
    en = split_en_ch("/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/examples.txt")
    get_key_words(en)


if __name__ == '__main__':
    main()
