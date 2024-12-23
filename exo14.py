wordd = input("Word: ")

frame_width = 30

word_length = len(wordd)
left_padding = (frame_width - word_length) // 2
right_padding = frame_width - word_length - left_padding

print("*" * frame_width)
print("*" + " " * left_padding + wordd + " " * right_padding + "*")
print("*" * frame_width)
