def combineIndex(noch_f, longch_f, longen_f):  # 非中文下标，超长中文下标，超长英文下标
    indexs = []
    # with open(noch_f, 'r')as f:
    #     for line in f.readlines():
    #         line = line.strip()
    #         linelist = line.split(",")
    #         for index in linelist:
    #             indexs.append(int(index))
    with open(longch_f, 'r') as f:
        for line in f.readlines():
            index = line.strip()
            indexs.append(int(index))
    with open(longen_f, 'r')as f:
        for line in f.readlines():
            index = line.strip()
            indexs.append(int(index))
    indexs = list(set(indexs))
    indexs = sorted(indexs)
    return indexs


def getFinalCorpus(indexs, input_f, output_f):
    index = 0  # 记录总的语料的下标变化
    i = 0  # 记录indexs的下标变化
    with open(input_f, 'r', encoding='utf-8') as fi, open(output_f, 'w', encoding='utf-8')as fo:
        for line in fi.readlines():
            if i < len(indexs) and indexs[i] != index:
                fo.write(line)
            else:
                i += 1
            index += 1


if __name__ == '__main__':
    indexs = combineIndex("",
                          "/root/test/examples_COLLINS.oneword.ch.short.index",
                          "/root/test/examples_COLLINS.oneword.notag.token.en.short.index")

    getFinalCorpus(indexs,
                   "/root/test/examples_COLLINS.oneword.ch",
                   "/root/test/examples_COLLINS.oneword.final.ch")
    getFinalCorpus(indexs,
                   "/root/test/examples_COLLINS.oneword.notag.token.en",
                   "/root/test/examples_COLLINS.oneword.notag.token.final.en")
