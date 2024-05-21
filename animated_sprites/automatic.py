# Copied from
# https://github.com/ppb/pursuedpybear/blob/master/examples/animated_sprites/animated_sprite.py

import math
import random
import time

import ppb
import ppb.events as events
from ppb.features.animation import Animation


class Blob(ppb.Sprite):
    image = Animation("resources/blob_{0..6}.png", 10)
    target = ppb.Vector(0, 0)
    speed = 1
    repulsion = 0.5

    def on_mouse_motion(self, event: events.MouseMotion, signal):
        self.target = event.position
        print(self.position)

    def on_update(self, event: events.Update, signal):
        target = next(event.scene.get(tag="food"))
        intent_vector = target.position - self.position
        if intent_vector:
            self.position += intent_vector.scale(self.speed * event.time_delta)
            self.rotation = (
                math.degrees(math.atan2(intent_vector.y, intent_vector.x)) - 90
            )
        for sib in self.siblings(event):
            repulsion_vector = sib.position - self.position
            if repulsion_vector:
                self.position -= repulsion_vector.scale(self.repulsion * event.time_delta)


    def siblings(self, event):
        for sprite in event.scene.get(kind=Blob):
            if sprite != self:
                yield sprite



class Food(ppb.Sprite):

    BORED_IN_S = 4

    image = ppb.Image("resources/apple.png")

    def __init__(self, *arg, **kwarg):
        self.last_moved = time.time()
        return super().__init__(*arg, **kwarg)

    def on_mouse_motion(self, event: events.MouseMotion, signal):
        self.position = event.position
        self.last_moved = time.time()

    def on_update(self, event: events.Update, signal):
        if time.time() - self.last_moved > self.BORED_IN_S:
            self.position = ppb.Vector(random.random() * 4 - 2, random.random() * 4 - 2)
            self.last_moved = time.time()

def setup(scene):
    scene.add(Food(), tags=["food"])
    scene.add(Blob(), tags=["blob"])
    scene.add(Blob(), tags=["blob"])
    scene.add(Blob(), tags=["blob"])


ppb.run(setup)
