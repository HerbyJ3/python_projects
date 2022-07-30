def count_substring(string, sub_string):
    list = [i for i in range(len(string)) if string.startswith(sub_string, i)]
    return len(list)
    