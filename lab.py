from remote_gui import *

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False

    def mute(self):
        if self.status == True:
            if self.muted == False:
                self.muted = True
            elif self.muted == True:
                self.muted = False

    def channel_up(self):
        if self.status == True:
            if self.channel < Television.MAX_CHANNEL:
                self.channel += 1
            elif self.channel == Television.MAX_CHANNEL:
                self.channel = Television.MIN_CHANNEL
        #print(Television().MIN_CHANNEL)

    def channel_down(self):
        if self.status == True:
            if self.channel > Television.MIN_CHANNEL:
                self.channel -= 1
            elif self.channel == Television.MIN_CHANNEL:
                self.channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.status == True:
            if self.volume < Television.MAX_VOLUME:
                self.volume += 1
            elif self.volume == Television.MAX_VOLUME:
                pass

    def volume_down(self):
        if self.status == True:
            if self.volume > Television.MIN_VOLUME:
                self.volume -= 1
            elif self.volume == Television.MIN_VOLUME:
                pass

    def __str__(self):
        if self.muted == True:
            return f'TV status: Power = {self.status}, Channel = {self.channel}, Volume = 0'
        elif self.muted == False:
            return f'TV status: Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
#print(Television().channel_up())