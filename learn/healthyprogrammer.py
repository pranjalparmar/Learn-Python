from pygame import mixer

# Starting the mixer 
mixer.init()

# Loading the song 
mixer.music.load("F:\Kahani Ansuni\Background Music\y2mate.com - Best of Sad Cinematic Background Music  Emotional Dramatic Music Instrumental - by AShamaluevMusic_uIFFF8p11Hk.mp3")

# Setting the volume 
mixer.music.set_volume(100)

# Start playing the song 
mixer.music.play()

# infinite loop 
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':

        # Pausing the music 
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music 
        mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer 
        mixer.music.stop()
        break