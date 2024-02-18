"""
try:
    a = 1 / 0
except ZeroDivisionError as e:
    print(e)
"""

# try:
#     x = 1/0
# finally:
#     print("finally")

# words_file = open("words.txt", "w")
# words_file.write("Avraham" + "\n")

# words_file = open("words.txt", "r")
# for name in words_file.readlines():
#     print(f"Hello {name}")
# words_file.close()

# hebrew_file = open("words.txt", "w", encoding='utf-8')
# hebrew_file.write("אברהם1")
# hebrew_file.close()

hebrew_file = open("words.txt", 'r', encoding='utf-8')
name = hebrew_file.read()
print(name)
hebrew_file.close()