# 对程序内的进行修改，原本的程序中word所在的那一行没留白
senstence = input("Sentence: ")
screen_width = 80
text_width = len(senstence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
word_margin = (box_width - text_width) // 2
print()
print(' ' * left_margin + '+' + '-' * (box_width) + '+')
print(' ' * left_margin + '|' + ' ' * box_width + '|')
print(' ' * left_margin + '|' + ' ' * word_margin + senstence + ' ' * word_margin + '|')
print(' ' * left_margin + '|' + ' ' * box_width + '|')
print(' ' * left_margin + '+' + '-' * (box_width) + '+')
print()