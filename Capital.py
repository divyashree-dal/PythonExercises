words = ["bHargaV","Kaushik","SanthOsh"]
count = 0
for every_word in words:
    for every_letter in every_word:
        if every_letter.isupper():
            count+=1
        else:
            continue
        print every_letter + " " + str(count)
print "total count" + str(count)