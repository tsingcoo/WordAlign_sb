# coding:utf-8
import jieba

import sys

default_encoding = 'utf-8'


# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)

def split_en_ch(filename):
    # i = 0
    en = []
    ch = []
    with open(filename, 'r') as f:
        line = f.readline()  # 跳过第一行
        for line in f.readlines():
            # i += 1
            # if i < 14632:
            #     print(line.split('\t')[1])
            en.append(line.split('\t')[0])
            ch.append(line.split('\t')[1])
    return en, ch


def split_punc_of_en(en, one_word_index):
    for i in range(len(one_word_index)):
        line = en[i]
        end = line[-1]
        line = line[:-1]
        line += " "
        line += end
        print(line)


def get_key_words(en):  # 返回关键词和对应的行号，跳过第一行，下标从0开始
    key_words = []
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
            for word in words:
                if "<vocab>" in word:
                    word = word.split("<vocab>")[1]  # 去掉关键词左边的部分
                    word = word.split("</vocab>")[0]  # 去掉关键词右边的部分
                    word = word.lower()
                    key_words.append(word)
                    one_word_index.append(one_word_line)
        one_word_line += 1  # 记录行标
    return key_words, one_word_index


# 对中文进行分词
def word_seg(ch, ch_seg_filename):
    ch_seg = []
    with open(ch_seg_filename, "w") as f:
        for line in ch:
            seg_list = list(jieba.cut(line))
            f.writelines(" ".join(seg_list))



def construct_keyword_ch(key_words, one_word_index, ch_seg_finename, stopwords_filename):  # 这里有一步过滤停用词
    ch_seg = []
    ch_seg_of_key_words = []  # ch_seg_of_key_words和ch_seg的区别是前者过滤了那些含有多个关键词的行
    ch_seg_of_key_words_no_stopwords = []
    with open(ch_seg_finename, 'r') as f:
        for line in f:
            line = line.strip()
            # print (line)
            line = line.split(" ")
            # print (line)
            ch_seg.append(line)
    # print (ch_seg)

    stopwords = []  # 停用词
    # with open(stopwords_filename, 'r') as f:
    #     for line in f:
    #         line = line.strip()
    #         stopwords.append(line)
    #
    # print(stopwords)

    for i in range(len(one_word_index)):
        # ch_seg_of_key_words.append(ch_seg[i])#这样写是错误的
        ch_seg_of_key_words.append(ch_seg[one_word_index[i]])

    for i in range(len(ch_seg_of_key_words)):
        ch_seg_of_key_words_no_stopwords.append([])
        for j in range(len(ch_seg_of_key_words[i])):
            if ch_seg_of_key_words[i][j] not in stopwords:
                ch_seg_of_key_words_no_stopwords[i].append(ch_seg_of_key_words[i][j])

    # print(ch_seg_of_key_words_no_stopwords)
    return ch_seg_of_key_words_no_stopwords


def word2index(key_words, vocab_filename):
    vocab = {}
    with open(vocab_filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            vocab[line[1]] = line[0]

    for i in range(len(key_words)):
        if key_words[i] in vocab:
            index = vocab[key_words[i]]
        else:
            index = '-1'
        key_words[i] = index
    # print(key_words)
    return key_words


def ch_seg2index(ch_seg, vocab_filename):
    vocab = {}
    with open(vocab_filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            vocab[line[1]] = line[0]
    for i in range(len(ch_seg)):
        for j in range(len(ch_seg[i])):
            if ch_seg[i][j] in vocab:
                index = vocab[ch_seg[i][j]]
            else:
                index = '-1'
            ch_seg[i][j] = index
    # print(ch_seg[2797])
    return ch_seg


def get_align2(key_words_index, ch_seg_of_key_words_index, prob_filename):  # 从中文向英文方向找对齐
    align = []
    prob = {}
    with open(prob_filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            if line[0] in prob:
                prob[line[0]][line[1]] = float(line[2])
            else:
                prob[line[0]] = {}
                prob[line[0]][line[1]] = float(line[2])
    for i in range(len(key_words_index)):
        tmp = 0
        tar = '-1'
        if key_words_index[i] == '-1':
            # print('-1'+' '+'-1')
            align.append('-1' + ' ' + '-1')
        else:
            for j in range(len(ch_seg_of_key_words_index[i])):
                if ch_seg_of_key_words_index[i][j] != '-1':
                    if ch_seg_of_key_words_index[i][j] in prob:
                        if key_words_index[i] in prob[ch_seg_of_key_words_index[i][j]]:
                            if prob[ch_seg_of_key_words_index[i][j]][key_words_index[i]] > tmp:
                                tmp = prob[ch_seg_of_key_words_index[i][j]][key_words_index[i]]
                                tar = ch_seg_of_key_words_index[i][j]
            align.append(key_words_index[i] + ' ' + tar)
    # print(ch_seg_of_key_words_index[2797])
    # print(ch_seg_of_key_words_index[2797][4])
    print(key_words_index[2128])
    # print(key_words_index)
    for i in range(len(key_words_index)):
        if key_words_index[i] == '3332':
            print(i)
    # print(prob[ch_seg_of_key_words_index[2797][4]][key_words_index[2797]])
    return align


def get_align(key_words_index, ch_seg_of_key_words_index, prob_filename):
    align = []
    prob = {}
    with open(prob_filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            if line[0] in prob:
                prob[line[0]][line[1]] = float(line[2])
            else:
                prob[line[0]] = {}
                prob[line[0]][line[1]] = float(line[2])
    # print(prob)
    for i in range(len(key_words_index)):
        tmp = 0
        tar = '-1'
        if key_words_index[i] == '-1':
            # print('-1'+' '+'-1')
            align.append('-1' + ' ' + '-1')
        else:
            for j in range(len(ch_seg_of_key_words_index[i])):
                if ch_seg_of_key_words_index[i][j] != '-1':
                    if key_words_index[i] in prob:
                        if ch_seg_of_key_words_index[i][j] in prob[key_words_index[i]]:
                            if prob[key_words_index[i]][ch_seg_of_key_words_index[i][j]] > tmp:
                                tmp = prob[key_words_index[i]][ch_seg_of_key_words_index[i][j]]
                                tar = ch_seg_of_key_words_index[i][j]
            # print(key_words_index[i] + ' '+ tar)
            align.append(key_words_index[i] + ' ' + tar)
    # print(align)
    return align


def align2word(key_words_index, one_word_index, align, vocab_en_filename, vocab_ch_filename):
    vocab_en = {}
    vocab_ch = {}
    with open(vocab_en_filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            vocab_en[line[0]] = line[1]
    with open(vocab_ch_filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            vocab_ch[line[0]] = line[1]

    for i in range(len(align)):
        align_line = align[i].split(" ")
        if align_line[0] == "-1":
            word_en = "-1"
        else:
            word_en = vocab_en[align_line[0]]
        if align_line[1] == "-1":
            word_ch = "-1"
        else:
            word_ch = vocab_ch[align_line[1]]
        print(str(one_word_index[i]) + " " + word_en + " " + word_ch)


def main():
    en, ch = split_en_ch("/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/examples.txt")
    key_words, one_word_index = get_key_words(en)
    # 对中文进行分词
    word_seg(ch, "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/ch_seg.txt")

    # 得到提取的关键词对应的中文行
    ch_seg_of_key_words = construct_keyword_ch(key_words, one_word_index,
                                               "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/ch_seg.txt",
                                               "/Users/wangqinglong/Library/Mobile Documents/com~apple~CloudDocs/Shanbay/stopwords.txt")
    # print(key_words)
    # print(len(ch_seg_of_key_words))

    # 把关键词转换为index
    key_words_index = word2index(key_words, "/Users/wangqinglong/Windows/800/LDC.final.en.vcb")
    # 把关键词对应的中文行转化成index
    ch_seg_of_key_words_index = ch_seg2index(ch_seg_of_key_words,
                                             "/Users/wangqinglong/Windows/800/LDC.nosemi.final.ch.vcb")
    # align = get_align(key_words_index, ch_seg_of_key_words_index, "/Users/wangqinglong/Windows/t2s64.t1.5")

    # 从中文方向向英文找对齐
    align = get_align2(key_words_index, ch_seg_of_key_words_index, "/Users/wangqinglong/Windows/800/LDC.final.t")
    align2word(key_words_index, one_word_index, align, "/Users/wangqinglong/Windows/800/LDC.final.en.vcb",
               "/Users/wangqinglong/Windows/800/LDC.nosemi.final.ch.vcb")
    # split_punc_of_en(en, one_word_index)


if __name__ == '__main__':
    main()
