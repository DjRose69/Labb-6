
trackobjects = [] # list of track objects
artistList = [] # to simplify things, we decided to create a list of artists


class Track:
    # Class for storing tracks
    def __init__(self, trackid, songid, artist, song):
        # the tracks attributes
        self.trackid = trackid
        self.songid = songid
        self.artist = artist
        self.song = song
        

    def __lt__(self, other):
        # returns True if artist is less
        # than other artist, false otherwise
        return self.artist < other.artist

#---------------------------------------------------------------------------------------

''' Code snippet that reads the txt file with a million tracks
and creates a Track() object for every row in the txt file. It
also appends every track object to the list of track objects
and appends every artist to the list of artists. '''

file = open('unique_tracks.txt', 'r')
for line in file.readlines():
    myline = line.replace("<SEP>",",")
    mylist = myline.split(",", 4)
    trackid = mylist[0]
    songid = mylist[1]
    artist = mylist[2]
    song = mylist[3]
    track = Track(trackid, songid, artist, song)
    trackobjects.append(track)
    artistList.append(track.artist)
file.close()


