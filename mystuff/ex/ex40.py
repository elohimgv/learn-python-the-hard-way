class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

song_1 = ["Happy birthday to you",
          "I don't want to get sued",
          "So I'll stop right there"]

happy_bday = Song(song_1)

song_2 = ["They rally around the family",
          "With pockets full of shells"]

bulls_on_parade = Song(song_2)

song_3 =  ["That's why I'm going to take",
           "to get out of my head that still..."]

despair = Song(song_3)

happy_bday.sing_me_a_song()
print()
bulls_on_parade.sing_me_a_song()
print()
despair.sing_me_a_song()