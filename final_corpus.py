def combineIndex(noch_f, longch_f, longen_f):
    indexs = []
    with open(noch_f, 'r')as f:
        for line in f.readlines():
            line = line.strip()
            linelist = line.split(",")
            for index in linelist:
                indexs.append(int(index))
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
    indexs = combineIndex("/Users/wangqinglong/Windows/800/LDC.noch.index.ch",
                          "/Users/wangqinglong/Windows/800/LDC.long.index.ch",
                          "/Users/wangqinglong/Windows/800/LDC.long.index.en")

    getFinalCorpus(indexs, "/Users/wangqinglong/Windows/800/LDC.nosemi.ch",
                   "/Users/wangqinglong/Windows/800/LDC.nosemi.final.ch")
    getFinalCorpus(indexs, "/Users/wangqinglong/Windows/800/LDC.en", "/Users/wangqinglong/Windows/800/LDC.final.en")
