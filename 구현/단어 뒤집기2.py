s = input()

tag_pos = []
for i in range(len(s)):
    if s[i] == '<':
        tag_pos.append(i)
    elif s[i] == '>':
        tag_pos.append(i)

strat_tag = 0 
end_tag = 0
word = ''
reverse_word = []
i = 0

if(len(tag_pos)) == 0:
    word = s.split(" ")
    for i in word:
        reverse_word.append("".join(reversed(i)))
    print(" ".join(reverse_word), end='')
    exit(0)

while (len(s) > i):
    if i in tag_pos:
        if word != '':
            reverse_word = "".join(reversed(word))
            print(reverse_word,  end='')
            word = ''
        start_tag = tag_pos.pop(0)
        end_tag = tag_pos.pop(0)
        print(s[start_tag:end_tag+1], end='')
        i = end_tag + 1

    else:
        if len(tag_pos) == 0:
            word = s[i:len(s)]
            break
        if(s[i] == ' '):
            print("".join(reversed(word)), end=' ')
            word = ''
            i += 1
        word += s[i]
        i += 1

reverse_word = []
word = word.split(" ")
if(word != ''):
    if len(word) > 0:
        for i in word:
            reverse_word.append("".join(reversed(i)))
        print(" ".join(reverse_word), end='')
    else:
        reverse_word = "".join(reversed(word))
        print(reverse_word)
