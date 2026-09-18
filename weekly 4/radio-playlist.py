import time
def main():
    playlist = ["Boston", "dracula", "i knew it, i knew you", "hate that i made you love me", "risk it all",]
    playlist.append("be by you")
    print(playlist)
    playlist.insert(0, "bohemian rhapsody")
    print(playlist)
    playlist.pop(4)
    print(playlist)
    print(playlist.index("risk it all"))
    print("number of songs in the playlist:" , len(playlist))
    playlist.reverse()#some methods dont work with some variables
    print(playlist)
    playlist.sort()
    print(playlist)

    repeat = 10
    while repeat > 0:
        print(playlist)
        song_played = playlist[0]
        playlist.pop(0)
        playlist.append(song_played)
        time.sleep(3)
        repeat -= 1









if __name__=="__main__":
    main()
