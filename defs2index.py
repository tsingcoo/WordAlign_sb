
def word2index(vcbF_en, inputF, outputF):
    word_index = {}
    with open(vcbF_en, encoding='utf-8') as f1:
        for line in f1.readlines():
            line = line.strip()
            line_list = line.split(" ")
            word_index[line_list[1]] = line_list[0]
    with open(inputF, encoding='utf-8') as f2, open(outputF, 'w', encoding='utf-8') as f3:
        for line in f2.readlines():
            line = line.strip()
            line_list = line.split("\t")
            if line_list[0] in word_index:
                index = word_index[line_list[0]]
                f3.writelines(index)
                f3.writelines("\t")
                f3.writelines(line_list[1])
                f3.writelines("\n")


if __name__ == '__main__':
    word2index("/Users/wangqinglong/Windows/800/LDC.final.en.vcb",
               "/Users/wangqinglong/Windows/800/defs_processed_vec.txt",
               "/Users/wangqinglong/Windows/800/defs_processed_index_vec.txt")
