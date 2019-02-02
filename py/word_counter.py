from collections import Counter
import sys

'''
    Usage in command line:
    >word_counter.py input output
        Output is optional, default value is output (to output.txt)
        Reads a .txt document, counts the number of words and outputs it
        Not sure if it works for non .txt documents
'''
def start():
    if len(sys.argv) == 3:
        input = sys.argv[1]
        output = sys.argv[2]
    elif len(sys.argv) == 2:
        input = sys.argv[1]
        output = 'output'
    else:
        print('At least one argument (input name) is required.\n'
              'Usage:\n'
              'word_counter.py input output')
        return
    logs = open(input + '.txt').read()
    cut = []
    split_logs = logs.split()
    #remove everything that isn't an alphanumerical value
    for word in split_logs:
        cut.append(''.join(filter(str.isalpha, word)))

    cloud = sorted(Counter(cut).items(), key=lambda x: x[1])
    cloud.reverse()
    try:
        f = open(output + '.txt', 'w')
        for l in cloud:
            f.write("%s\n" % str(l))
    except IOError as e:
        print(e)

if __name__ == '__main__':
    start()
