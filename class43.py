from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this."
        "Your Mom would be proud.... if she were smarter."
            "Such a     luser."
            "I have     a small puppy that's better at this."
            "You're     worse than your Dad's jokes."
    ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent(""" 
        The Gothons of Planet
        destroyed...
        """))
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
            Quick
            it
            moving
            """))
            return 'death'
        elif action == "dodge!":
            print(dedent(""" 
            Like
            slide
            past
            """))
            return 'death'
        elif action == 'tell a joke':
            print(dedent(""" 
            Lucky
            the
            Ibhe
            """))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class IaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self,start_scene):
        pass
    def next_scene(self,scene_name):
        pass
    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()