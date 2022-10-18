#lower case letters
def lower_case_text():
    path = "./harry_potter_prisoner-of_ascaban.txt"
    with open(path, encoding="utf8") as tf:
        text = tf.read()
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    text = text.lower()
    text1 = ""
    for char in text:
        if char in chars:
            text1 += char
    return text1


def famous_words(words):
    top_10 = words[-10:]
    for index, _ in enumerate(top_10[:-1]):
        if top_10[index][1] == top_10[index + 1][1]:
            relocate(words, top_10, index)
    return top_10


def relocate(words, top_10, index):
    for idx, _ in enumerate(top_10[: index + 1]):
        top_10[index - idx] = words[-len(top_10[index:]) - 1 - idx]

def categorization(text_ascii, char_len=None):
    if char_len is None:
        end = lambda word: len(word)
    else:
        end = lambda word: char_len
    segmentation = {}
    for word in text_ascii:
        if len(word) < end(word):
            continue
        segmentation[word[: end(word)]] = segmentation.get(word[: end(word)], 0) + 1
    segmentation = sorted(segmentation.items(), key=lambda x: x[1],reverse=True)[0:10] # sorting by second argument
    return segmentation



def main():

    final_text = lower_case_text()
    text_ascii = final_text.split(sep=" ")
    words = categorization(text_ascii)
    two_len = categorization(text_ascii, char_len=2)
    three_len = categorization(text_ascii, char_len=3)
    two_len_final=two_len[0:3]
    three_len_final=three_len[0:3]
    top_10= famous_words(words)
    print("Most 10 common words:",top_10)
    print("3 most common  two characters:",two_len_final)
    print("3 most common  three characters:",three_len_final)

main()
