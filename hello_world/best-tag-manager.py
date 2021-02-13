import collections

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt


def get_best_tags(file_name: str = "./raw_tags.txt", number_of_tags: int = 13):
    # Read input file, note the encoding is specified here
    # It may be different in your text file
    file = open(file_name, encoding="utf8")
    raw_tags_file = file.read()

    # # Stopwords
    # stopwords = set(line.strip() for line in open('stopwords.txt'))
    # stopwords = stopwords.union(set(['mr', 'mrs', 'one', 'two', 'said']))

    # Instantiate a dictionary, and for every word in the file,
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}
    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in raw_tags_file.lower().split(","):
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    # Print most common word
    print("\nOK. The {} most common words are as follows\n".format(number_of_tags))

    tag_counter = collections.Counter(wordcount)
    for word, count in tag_counter.most_common(number_of_tags):
        print(word, ": ", count)
    # Close the file
    file.close()
    # Create a data frame of the most common words
    # Draw a bar chart
    lst = tag_counter.most_common(number_of_tags)
    data_frame = pd.DataFrame(lst, columns=['Tag', 'Count'])
    result = data_frame.to_csv()
    # data_frame.plot.bar(x='Tag', y='Count')

    # write the result to a file
    file_to_write = open("best_tags.txt", "w")
    file_to_write.write(result)
    file_to_write.close()


if __name__ == "__main__":
    get_best_tags()
