def read_file(file_name):
    lines = []
    with open(file_name, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    # person = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        line_s = line.split(' ')
        print(line_s)
        time = line_s[0]
        name = line_s[1]
        line_a = line_s[2:]
        if name == 'Allen':
            if line_s[2] == '貼圖':
                allen_sticker_count += 1
            elif line_s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in line_s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if line_s[2] == '貼圖':
                viki_sticker_count += 1
            elif line_s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in line_s[2:]:
                    viki_word_count += len(m)
    print(allen_word_count)
    print(allen_sticker_count)
    print(allen_image_count)
    print(viki_word_count)
    print(viki_sticker_count)
    print(viki_image_count)
    return new

# def write_file():
#     with open(file_name,)


def main():
    lines = read_file('076 -LINE-Viki.txt')
    lines = convert(lines)

main()


