import copy as cp
import pygame
import math


class Clock():
    whiteColor = (255, 255, 255)
    patternSetting = True

    def __init__(self, centerX: int, centerY: int, radius: int, baseSpeed):
        self.location1 = 0
        self.location2 = 180
        self.baseSpeed = baseSpeed
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius
        self.patternSetting = False
        self.allowUpdate = True
        self.speed1 = 0
        self.speed2 = 0

    def reinitiate(self, i: int, j: int, idirec, jdirec, allowUpdate):
        idirec = idirec*2 - 1
        jdirec = jdirec*2 - 1
        i = i % 628
        j = j % 628
        self.location1Goal = i
        self.location2Goal = j
        self.speed1 = self.baseSpeed * idirec
        self.speed2 = self.baseSpeed * jdirec
        self.allowUpdate = allowUpdate
        self.patternSetting = True

    def settingPattern(self):
        if self.patternSetting:
            self.patternSetting = False
            if self.location1 != self.location1Goal:
                self.location1 = (self.location1 + self.speed1) % 628
                self.patternSetting = True

            if self.location2 != self.location2Goal:
                self.location2 = (self.location2 + self.speed2) % 628
                self.patternSetting = True

    def update(self):
        if self.allowUpdate:
            self.location1 = (self.location1 + self.speed1) % 628
            self.location2 = (self.location2 + self.speed2) % 628

    def display(self, screen):
        pygame.draw.circle(screen, self.whiteColor,
                           (self.centerX, self.centerY), self.radius, 1)
        pygame.draw.line(screen, self.whiteColor, (self.centerX, self.centerY), (self.centerX + math.cos(
            self.location1/100.0) * (self.radius-5), self.centerY + math.sin(self.location1/100.0) * (self.radius-5)), 4)
        pygame.draw.line(screen, self.whiteColor, (self.centerX, self.centerY), (self.centerX + math.cos(
            self.location2/100.0) * (self.radius-5), self.centerY + math.sin(self.location2/100.0) * (self.radius-5)), 4)
