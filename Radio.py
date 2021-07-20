#!/usr/bin/env python3

import nowplaying
import vlc

class Radio():
    def __init__(self):

        error_flag = 0

        try:
            self.create_name_list()
        except IndexError:
            error_flag = 1
        except IOError:
            error_flag = 2
        if error_flag == 1:
            print("Error: Wrong formatting radiolists.txt!")
        if error_flag == 2:
            print("Error: radiolists.txt not found")

        self.paused = False
        self.i = 0
        self.label_text = (self.a[self.i])
     #   print(self.radio[self.a[self.i]])
        nowplaying.np = self.label_text
        self.play(self.radio[self.a[self.i]])
        self.pause_ch()



    # Creations of list with web radio names and addresses
    def create_name_list(self):
        self.i=0
        self.radio = {}
        # Let's open text file with web radio list
        radiolist = "radiolist.txt"
        fw = open(radiolist, "r")
        # Let' s read text file line by line
        record = fw.readline()
        while len(record) > 0:
            record_ok = record.rstrip('\n')
            splittedrecord = record_ok.split(",")
            self.radio[splittedrecord[0]] = splittedrecord[1]
            record = fw.readline()
        fw.close()
        self.a = []
        for name in enumerate(sorted(self.radio.keys())): # enumerate return tuple
            # name[1] is web radio name   name[0] is record number.
            # Record number is not needed in this app as it is now. Maybe useful for future development.
            # Let's create a list with radio names
                self.a.append(name[1])

    # Handler for player's buttons
    def next_ch(self):
        self.i += 1
        if self.i == len(self.a):
            self.i = 0
        self.label_text = (self.a[self.i])
        #print(self.label_text)
        nowplaying.np = self.label_text

        self.player.stop()
        self.play(self.radio[self.a[self.i]])

    def prev_ch(self):
        self.i -= 1
        if self.i < 0:
            self.i = len(self.a)-1
        self.label_text = (self.a[self.i])
        print(self.label_text)
        nowplaying.np = self.label_text

        self.player.stop()
        self.play(self.radio[self.a[self.i]])


    def pause_ch(self):
        if not self.paused:
            self.player.stop()
            self.paused = True
            print("paused!")
        elif self.paused:
            self.player.play()
            print("playing!")
            self.paused = False


    # Playback the selectded radio
    def play(self,url):
        self.player = vlc.MediaPlayer(url)
        self.player.play()

    # When you click to exit, this function is called
    def on_exit(self):
       pass 
