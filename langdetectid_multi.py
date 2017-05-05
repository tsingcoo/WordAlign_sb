import langid
import multiprocessing


def read_f(input_f):
    lines = []
    with open(input_f, 'r') as f:
        for line in f.readlines():
            lines.append(line)
    return lines


def detect_line(index, line):
    try:
        lang = langid.classify(line)[0]
        if lang != 'zh':
            print(str(index) + " ", lang)
    except Exception as e:
        print(str(index) + " ", e)


if __name__ == '__main__':
    lines = read_f("/Users/wangqinglong/Windows/800/LDC.ch")

    pool = multiprocessing.Pool(processes=4)
    for i in range(len(lines)):
        pool.apply_async(detect_line, (i, lines[i],))
