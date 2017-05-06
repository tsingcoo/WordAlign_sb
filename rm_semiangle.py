def replace_semiangle(input_f, output_f):
    with open(input_f, 'r') as fi, open(output_f, 'w') as fo:
        for line in fi.readlines():
            line = line.replace(",", "，")
            line = line.replace(".", "。")
            line = line.replace("?", "？")
            line = line.replace("!", "！")
            line = line.replace(":", "：")
            fo.write(line)


if __name__ == '__main__':
    replace_semiangle("/Users/wangqinglong/Windows/800/LDC.ch", "/Users/wangqinglong/Windows/800/LDC.nosemi.ch")
