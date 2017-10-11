f = file("words.txt").read()

for word in f.split():
    count = 0
    for char in word:
        count = count + 1
    if(count>20):
        print(word)
