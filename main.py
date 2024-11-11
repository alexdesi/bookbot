def count_chars(text):
    counts = {}

    for c in text:
        lc = c.lower()
        if lc in counts:
            counts[lc]+=1
        else:
            counts[lc]=1

    return counts

with open('books/frankenstein.txt') as f:
    book_content = f.read()
    word_count = len(book_content.split())

dict_chars = count_chars(book_content)

print(f"{word_count} words found in the document\n")

sorted_items = sorted(dict_chars.items(), key=lambda x:x[1], reverse=True)

for ch, count in sorted_items:
    if ch.islower():
        print(f"The '{ch}' character was found {count} times")
