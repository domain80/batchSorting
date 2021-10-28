oldTBooks = [
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numbers",
    "Deuteronomy",
    "Joshua",
    "Judges",
    "Ruth",
    "I Samuel",
    "II Samuel",
    "I Kings",
    "II Kings",
    "I Chronicles",
    "II Chronicles",
    "Ezra",
    "Nehemiah",
    "Esther",
    "Job",
    "Psalms",
    "Proverbs",
    "Ecclesiastes",
    "Song of Solomon",
    "Isaiah",
    "Jeremiah",
    "Lamentations",
    "Ezekiel",
    "Daniel",
    "Hosea",
    "Joel",
    "Amos",
    "Obadiah",
    "Jonah",
    "Micah",
    "Nahum",
    "Habakkuk",
    "Zephaniah",
    "Haggai",
    "Zechariah",
    "Malachi"
]

newTBooks = [
    "Matthew",
    "Mark",
    "Luke",
    "John",
    "Acts",
    "Romans",
    "1st Corinthians",
    "2nd Corinthians",
    "Galatians",
    "Ephesians",
    "Philippians",
    "Colossians",
    "1st Thessalonians",
    "2nd Thessalonians",
    "1st Timothy",
    "2nd Timothy",
    "Titus",
    "Philemon",
    "Hebrews",
    "James",
    "1st Peter",
    "2nd Peter",
    "1st John",
    "2nd John",
    "3rd John",
    "Jude",
    "Revelation",
]

i = 1
# print(len(books))


oldTestmnt = []
for book in oldTBooks:
    if(i < 10):
        book = book[:0] + "A0" + str(i) + "__" + book[0:]
    else:
        book = book[:0] + "A" + str(i) + "__" + book[0:]
    oldTestmnt.append(book)
    i += 1

i = 1
newTestmnt = []
for book in newTBooks:
    if(i < 10):
        book = book[:0] + "B0" + str(i) + "__" + book[0:]
    else:
        book = book[:0] + "B" + str(i) + "__" + book[0:]
    newTestmnt.append(book)
    i += 1


cmdOrganizeOldT = "@echo off \n"

i = 1
for folder in oldTestmnt:
    if(i < 10):
        cmd = "mkdir " + '"' + str(folder) + '"' + " | move A0" + \
            str(i) + "__*.mp3 " + '"' + str(folder) + '"' + "\n"
    else:
        cmd = "mkdir " + '"' + str(folder) + '"' + " | move A" + \
            str(i) + "__*.mp3 " + '"' + str(folder) + '"' + "\n"
    cmdOrganizeOldT += cmd
    i += 1

i = 1
for folder in newTestmnt:
    if(i < 10):
        cmd = "mkdir " + '"' + str(folder) + '"' + " | move B0" + \
            str(i) + "__*.mp3 " + '"' + str(folder) + '"' + "\n"
    else:
        cmd = "mkdir " + '"' + str(folder) + '"' + " | move B" + \
            str(i) + "__*.mp3 " + '"' + str(folder) + '"' + "\n"
    cmdOrganizeOldT += cmd
    i += 1

sortFolders = 'mkdir "Old Testament" |'

cmdOrganizeOldT += "pause"
print(cmdOrganizeOldT)

# Print commands to file.
batFile = open("organizeFiles.bat", "w")
print(cmdOrganizeOldT, file=batFile)
batFile.close()
