import spacy

nlp = spacy.load('en')


def token_sym(input_f, output_f):
    with open(input_f, 'r', encoding='utf-8') as f1, open(output_f, 'w', encoding='utf-8')as f2:
        for line in f1.readlines():
            line = line[:-1]  # 怕是去掉换行符
            doc = nlp(line)
            firstword = True
            for word in doc:
                if firstword:
                    firstword = False
                else:
                    f2.write(" ")
                f2.write(str(word).lower())  # 大写转小写
            f2.write('\n')


if __name__ == '__main__':
    token_sym(
        "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/examples/examples.oneword.final.en",
        "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/examples/examples.oneword.final.token.en")
