def replace_semiangle(input_f, output_f):
    with open(input_f, 'r', encoding='utf-8') as fi, open(output_f, 'w', encoding='utf-8') as fo:
        for line in fi.readlines():
            line = line.replace(",", "，")
            line = line.replace(".", "。")
            line = line.replace("?", "？")
            line = line.replace("!", "！")
            line = line.replace(":", "：")
            fo.write(line)


if __name__ == '__main__':
    replace_semiangle("/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/chinaDaily_zh_seg.txt",
                      "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/chinaDaily_zh_seg_nosemi.txt")
