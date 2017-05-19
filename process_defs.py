import jieba
import re


def read_defs(input_f, output_f, output_word, output_def):
    word_def = {}
    rep = {",": "", "，": "", ".": "", "(": "", "（": "", "）": "", ")": "", "[": "", "]": "", "<": "", ">": "", "...": "",
           "；": "",
           "=": "", '\“': "", "…": "", "、": "", "的": ""}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    with open(input_f, encoding='utf-8') as f:
        line = f.readline()  # 跳过第一行
        for line in f.readlines():
            line = line.strip()
            line_list = line.split("\t")
            word_def[line_list[0]] = line_list[1]
    with open(output_f, 'w', encoding='utf-8')as f, open(output_word, 'w', encoding='utf-8')as f_word, open(output_def,
                                                                                                            'w',
                                                                                                            encoding='utf-8')as f_def:
        for k, v in word_def.items():
            v = pattern.sub(lambda m: rep[re.escape(m.group(0))], v)
            seg_list = list(jieba.cut(v))
            f.writelines(k)
            f.writelines("\t")
            f.writelines(" ".join(seg_list))
            f.writelines("\n")

            f_word.writelines(k)
            f_word.writelines("\n")
            f_def.writelines(" ".join(seg_list))
            f_def.writelines("\n")

    print(word_def)
    print(len(word_def))


if __name__ == '__main__':
    stop_words = [",", ".", "(", ")", "[", "]", "<", ">", "...", "；", "="]
    read_defs("/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/defs.txt",
              "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/defs_processed.txt",
              "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/defs_processed_word.txt",
              "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/defs_processed_def.txt")
