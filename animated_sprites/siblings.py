# Copied from 
# https://github.com/ppb/pursuedpybear/blob/master/examples/animated_sprites/animated_sprite.py

import math
import random

import ppb
from ppb.features.animation import Animation
import ppb.events as events

def random_pos():
    return ppb.Vector(random.random() * 4 - 2, random.random() * 4 -2)

class Blob(ppb.BaseSprite):
    image = Animation("resources/blob_{0..6}.png", 10)
    target = ppb.Vector(0, 0)
    speed = 1
    repulsion = 0.5 

    def on_mouse_motion(self, event: events.MouseMotion, signal):
        self.target = event.position

    def on_update(self, event: events.Update, signal):
        intent_vector = self.target - self.position
        if intent_vector:
            self.position += intent_vector.scale(self.speed * event.time_delta)
            self.rotation = math.degrees(math.atan2(intent_vector.y, intent_vector.x)) - 90
        for sib in self.siblings(event):
            repulsion_vector = sib.position - self.position
            if repulsion_vector:
                self.position -= repulsion_vector.scale(self.repulsion * event.time_delta)


    def siblings(self, event):
        for sprite in event.scene.get(kind=Blob):
            if sprite != self:
                yield sprite


def setup(scene):
    scene.add(Blob(position = random_pos()))
    scene.add(Blob(position = random_pos()))
    scene.add(Blob(position = random_pos()))


ppb.run(setup)
