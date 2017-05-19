
def testCnt(inputF):
    with open(inputF,'r', encoding= 'utf-8') as f:
        line = f.readline()
        line = line.split('\t')[1]
        line = line.split(" ")
        print(len(line))

if __name__ == '__main__':
    testCnt("/Users/wangqinglong/Windows/800/defs_processed_index_vec.txt")
