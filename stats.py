def num_of_words(content):
    words = content.split()
    count = 0

    for word in words:
        count += 1

    print(f"Found {count} total words")

def char_count(content):
    result = {}
    cont = list(content)
    for c in cont:
        if result.get(c.lower()) is None:
            result[c.lower()] = 1
        else:
            result[c.lower()] += 1
    result = sort_char_count(result)
    return result

def sort_char_count(char_dict):
    chars = [{k: v} for k, v in char_dict.items()]
    chars.sort(key=key_sort, reverse=True)
    return chars

def key_sort(c):
    return [x for x in c.values()]
