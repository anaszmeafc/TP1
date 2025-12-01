import emoji

wordToEmoji = {
    'super': ':thumbs_up:',
    'coeur': ':red_heart:',
    'sourire': ':smiley:',
}


def translate(word):
    if word in wordToEmoji.keys():
        return wordToEmoji[word]
    else:
        return word


def convert(word):
    # emoji.emojize convertit le code smiley en smileys
    return emoji.emojize(word, use_aliases=True)

if __name__ == "__main__":

    print("super")
