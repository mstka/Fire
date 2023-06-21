import pygame
import sys
import random

class fire_simulation:
    def __init__(self,w,h):
        self.dot = [[0 for i in range(h)] for i in range(w)]
        self.w = w
        self.h = h
        self.new = [[0 for i in range(h)] for i in range(w)]
    
    def set_fire(self,mode, x = 0, y = 0):
        if mode == 'center':
            for i in range(51):
                for e in range(51):
                    self.dot[int(self.w/2)-25+i][int(self.h/2)-25+e] = 255
        elif mode == 'manual':
            self.dot[x][y] = 255
    
    def step(self):
        self.new = [[0 for i in range(h)] for i in range(w)]
        for i in range(self.w):
            for e in range(self.h):
                if e > 2 and i > 3 and i < self.w-4:
                    if self.dot[i][e] > 0:
                        for j in range(3):
                            rnd_x = random.randint(-3,3)
                            rnd_y = random.randint(-3,0)
                            percent = random.uniform(0, 1)
                            num = self.dot[i][e] * percent
                            self.new[i + rnd_x][e + rnd_y] += num
                            self.dot[i][e] -= num
                        self.dot[i][e] = 0
        for i in range(self.w):
            for e in range(self.h):
                self.dot[i][e] += self.new[i][e]
                if self.dot[i][e] >= 255:
                    self.dot[i][e] = 255
    def output_dot(self):
        return self.dot




