# import langid
from langid.langid import LanguageIdentifier, model

identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
identifier.set_languages(['zh','en'])


def langdeid(input_f, output_f):
    indexs = []
    index = 0  # 记录行下标
    with open(input_f, 'r') as f:
        for line in f.readlines():
            line = line.split(" ")
            new_line = ""
            for word in line:
                new_line += word
            try:
                lang = identifier.classify(new_line)[0]
                prec = identifier.classify(new_line)[1]
                if lang != 'zh':
                    print(str(index) + " ", lang, prec, " " + new_line)
                    indexs.append(index)
            except Exception as e:
                print(str(index) + " ", e, " " + new_line)
                indexs.append(index)

            index = index + 1
    return indexs


def main():
    indexs = langdeid("/Users/wangqinglong/Windows/800/LDC.ch", "/Users/wangqinglong/Windows/800/LDC.new.ch")
    print(len(indexs))
    print(indexs)


if __name__ == '__main__':
    main()
