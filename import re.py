import re
re.search()

# Chuỗi văn bản mẫu
text = "The Quick brown fox jumps over the lazy dog."

""" # ^: Khớp với đầu dòng
pattern_start = r'^The'
matches_start = re.findall(pattern_start, text)
print("Matches for ^The:", matches_start)

# $: Khớp với cuối dòng
pattern_end = r'dog.$'
matches_end = re.findall(pattern_end, text)
print("Matches for dog.$:", matches_end)

# .: Khớp với bất kỳ ký tự nào
pattern_any_char = r'\b...\b'
matches_any_char = re.findall(pattern_any_char, text)
print("Matches for \\b...\\b:", matches_any_char)

# \s: Khớp với khoảng trắng
pattern_whitespace = r'\s'
matches_whitespace = re.findall(pattern_whitespace, text)
print("Matches for whitespace:", matches_whitespace)

# \S: Khớp với bất kỳ ký tự không phải là khoảng trắng
pattern_non_whitespace = r'\S+'
matches_non_whitespace = re.findall(pattern_non_whitespace, text)
print("Matches for non-whitespace:", matches_non_whitespace) 
# *: Lặp lại một ký tự không hoặc nhiều lần
pattern_repeat_zero_or_more = r'\w*'
matches_repeat_zero_or_more = re.findall(pattern_repeat_zero_or_more, text)
print("Matches for \\wo*:", matches_repeat_zero_or_more)

# *?: Lặp lại một ký tự không hoặc nhiều lần (không tham lam)
pattern_non_greedy_repeat = r'\w*?'
matches_non_greedy_repeat = re.findall(pattern_non_greedy_repeat, text)
print("Matches for \\wo*?:", matches_non_greedy_repeat)

# +: Lặp lại một ký tự ít nhất một lần
pattern_repeat_one_or_more = r'\w+'
matches_repeat_one_or_more = re.findall(pattern_repeat_one_or_more, text)
print("Matches for \\w+:", matches_repeat_one_or_more)

# +?: Lặp lại một ký tự ít nhất một lần (không tham lam)
pattern_non_greedy_repeat_one_or_more = r'\w+?'
matches_non_greedy_repeat_one_or_more = re.findall(pattern_non_greedy_repeat_one_or_more, text)
print("Matches for \\w+?:", matches_non_greedy_repeat_one_or_more)

# [aeiou]: Khớp với một ký tự duy nhất trong tập hợp được liệt kê
pattern_vowels = r'[aeiou]'
matches_vowels = re.findall(pattern_vowels, text)
print("Matches for [aeiou]:", matches_vowels) """

# [a-z0-9]: Tập hợp các ký tự có thể bao gồm một dải
pattern_range = r'[a-z0-9]+'
matches_range = re.findall(pattern_range, text)
print("Matches for [a-z0-9]+:", matches_range) 

# (): Chỉ định vị trí bắt đầu của việc trích xuất chuỗi
pattern_start_extraction = r'(\b\w+\b)'
matches_start_extraction = re.findall(pattern_start_extraction, text)
print("Matches for start extraction:", matches_start_extraction)

# (): Chỉ định vị trí kết thúc của việc trích xuất chuỗi
pattern_end_extraction = r'(\b\w+\b).'
matches_end_extraction = re.findall(pattern_end_extraction, text)
print("Matches for end extraction:", matches_end_extraction)
 