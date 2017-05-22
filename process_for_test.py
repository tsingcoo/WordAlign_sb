# coding:utf-8
import jieba

import sys

default_encoding = 'utf-8'


def split_en_ch(filename):
    en = []
    ch = []
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()  # 跳过第一行
        for line in f.readlines():
            en.append(line.split('\t')[0])
            ch.append(line.split('\t')[1])
    return en, ch


def get_one_word_index(en):  # 返回关键词和对应的行号，跳过第一行，下标从0开始
    many_word_line = 0  # 包含多个词的行
    one_word_line = 0  # 只出现一次的词的行，从0开始
    one_word_index = []
    for line in en:
        words = line.split(" ")
        i = 0
        for word in words:
            if "<vocab>" in word:
                i += 1
        if i > 1:  # 包含多个词
            many_word_line += 1
        else:  # 仅仅一个词
            one_word_index.append(one_word_line)
        one_word_line += 1  # 记录行标
    return one_word_index


def print_final_corpus(one_word_index, en, ch, output_f_e, output_f_c):
    with open(output_f_e, 'w', encoding='utf-8') as f_e, open(output_f_c, 'w', encoding='utf-8') as f_c:
        for i in range(len(one_word_index)):
            f_e.writelines(en[one_word_index[i]])
            f_e.writelines('\n')
            seg_list = list(jieba.cut(ch[one_word_index[i]]))
            f_c.writelines(" ".join(seg_list))


if __name__ == '__main__':
    en, ch = split_en_ch("/root/test/examples_COLLINS.txt")
    one_word_index = get_one_word_index(en)
    print_final_corpus(one_word_index, en, ch, "/root/test/examples_COLLINS.oneword.en",
                       "/root/test/examples_COLLINS.oneword.ch")
