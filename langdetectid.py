import langid

def langdeid(input_f, output_f):
    indexs = []
    index = 0  # 记录行下标
    with open(input_f, 'r') as f:
        for line in f.readlines():
            try:
                lang = langid.classify(line)[0]
                if lang != 'zh':
                    print(str(index) + " ", lang)
                    indexs.append(index)
            except Exception as e:
                print(str(index) + " ", e)
                indexs.append(index)

            index = index + 1
    return indexs


def main():
    indexs = langdeid("/Users/wangqinglong/Windows/800/LDC.ch", "/Users/wangqinglong/Windows/800/LDC.new.ch")
    print(len(indexs))
    print(indexs)


if __name__ == '__main__':
    main()
