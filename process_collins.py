# coding:utf-8

# 删除句对中tag
def rm_tag(input_f, output_f):
    with open(input_f, 'r', encoding='utf-8') as f1, open(output_f, 'w', encoding='utf-8') as f2:
        for line in f1.readlines():
            line = line.strip()
            line_list = line.split()
            first_word = True
            for word in line_list:
                if "<vocab>" in word:
                    word = word.split("<vocab>")[1]  # 去掉关键词左边的部分
                    word = word.split("</vocab>")[0]  # 去掉关键词右边的部分

                word = word.lower()
                if first_word == True:
                    first_word = False
                else:
                    f2.write(" ")
                f2.write(word)
            f2.write('\n')


if __name__ == '__main__':
    rm_tag("/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/collins_fl/examples_collins_fl.oneword.en",
           "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/collins_fl/examples_collins_fl.oneword.notag.en")
