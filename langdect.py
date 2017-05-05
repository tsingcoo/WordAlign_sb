from langdetect import detect


def langde(input_f, output_f):
    lines = []
    indexs = []
    i = 0  # 记录行下标
    with open(input_f, 'r') as f:
        for line in f.readlines():
            try:
                lang = detect(line)
                if lang == 'zh-cn':
                    lines.append(line)
                    indexs.append(i)
            except Exception as e:
                print(str(i) + " ", e)

            i = i + 1

    with open(output_f, 'w') as f:
        for line in lines:
            f.writelines(str(i) + " " + line)


def main():
    langde("/Users/wangqinglong/Windows/800/LDC.ch", "/Users/wangqinglong/Windows/800/LDC.new.ch")


if __name__ == '__main__':
    main()
