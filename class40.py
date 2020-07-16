import mystuff
mystuff.apple()
print(mystuff.tangerine)

class mystuff1(object):
    def __init__(self):
        self.tangerine = "and now a thousand years between"

    def apple(self):
        print("I am ciassy apples!")

thing = mystuff1()
thing.apple()
print(thing.tangerine)

class Song(object):
    def __init__(self,lyrics):
        self.abc = lyrics
    
    def sing_me_a_song(self):
        for line in self.abc:
            print(line)

happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get used",
    "So I'll stop right there"
])

happy_bday.sing_me_a_song()