with open("confession.txt", "r", encoding="utf-8") as f1:
    text1 = f1.read().split('\n')

with open("logs.txt", "r", encoding="utf-8") as f2:
    text2 = f2.read().split('\n')

text = [i for i in text1 if i not in text2]
print(text)#removes all already uploaded confessions from "confession.txt"

with open("output.txt", "w", encoding="utf-8") as f:
    for i in text:
        f.write(i + "\n")#writes the new confessions to output.txt


with open("logs.txt", "a", encoding="utf-8") as f:
    for i in text:
        f.write("\n" + i)#appends the new confession to the log file