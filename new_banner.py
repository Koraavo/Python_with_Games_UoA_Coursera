def main():
    banner_word = 'blue'
    banner_indent = 3
    my_banner = banner(banner_word, banner_indent)
    for item in my_banner:
        print(item)
    print(banner_word)

def banner(word, indent):
    new_banner = []
    for letter in word:
        new_banner.append(' ' * indent + letter)
    return new_banner

main()