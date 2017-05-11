def my_compare(t1, t2):
    if t1[1] == t2[1]:
        if t1[0] < t2[0]:
            return -1
        else:
            return 1
    elif t1[1] < t2[1]:
        return -1
    else:
        return 1

def print_words_from_file(filepath):

    file_words = []
    with open(filepath) as f:
        for line in f.readlines():
            file_words += line.rstrip().split(' ')

    word_counts = {}

    for word in file_words:
        word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in sorted(word_counts.items(), cmp=my_compare):
        print word, count


print_words_from_file("/home/vagrant/src/words.txt")
