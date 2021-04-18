import math
from abc import ABC, abstractclassmethod
class AreaAndVolume(ABC):
    @abstractclassmethod
    def get_area(self):
        raise NotImplementedError()

    @abstractclassmethod
    def get_volume(self):
        raise NotImplementedError()

    @abstractclassmethod
    def get_area_and_volume(self):
        raise NotImplementedError()

class RectangleAreaAndVolume(AreaAndVolume):
    def get_area(self, length: float, width: float, height: float):
        return 2 * length * width + 2 * width * height + 2 * length * height
    
    def get_volume(self, length: float, width: float, height: float):
        return length * width * height

    def get_area_and_volume(self, length: float, width: float, height: float):
        return f'Area: {self.get_area(length, width, height)} Volume: {self.get_volume(length, width, height)}'

class CylinderAreaAndVolume(AreaAndVolume):
    def get_area(self, radius: float, height: float):
        return 2 * math.pi * radius**2 + 2 * math.pi * radius * height
    
    def get_volume(self, radius: float, height: float):
        return math.pi * radius**2 * height

    def get_area_and_volume(self, radius: float, height: float):
        return f'Area: {self.get_area(radius, height)} Volume: {self.get_volume(radius, height)}'

class ConeAreaAndVolume(AreaAndVolume):
    def get_area(self, radius: float, height: float):
        return math.pi * radius * (radius + math.sqrt(height**2 + radius**2))
    
    def get_volume(self, radius: float, height: float):
        return math.pi * radius**2 * (height/3)

    def get_area_and_volume(self, radius: float, height: float):
        return f'Area: {self.get_area(radius, height)} Volume: {self.get_volume(radius, height)}'

class SphereAreaAndVolume(AreaAndVolume):
    def get_area(self, radius: float):
        return 4 * math.pi * radius**2
    
    def get_volume(self, radius: float):
        return 4/3 * math.pi * radius**3

    def get_area_and_volume(self, radius: float):
        return f'Area: {self.get_area(radius)} Volume: {self.get_volume(radius)}'

def match_pattern(user_input):
    match user_input:
        case ['rect', length, width, height]:
            return RectangleAreaAndVolume().get_area_and_volume(
                        float(length), 
                        float(width), 
                        float(height)
                    )
            
        case _:
            return 'whoopsie'
looping = True
while looping: 
    print('rect l w h')
    print('cyl r h')
    print('cone r h')
    print('sphere r')
    print('q to quitl')
    user_input = input("> ").lower()
    user_input = user_input.split(" ")
    
    # shape = user_input[0]
    # dimensions = [float(i) for i in user_input[1:]]
    # if shape == 'rect':
    #     length, width, height = dimensions
    #     print(RectangleAreaAndVolume().get_area_and_volume(length, width, height))
    # if shape == 'cyl':
    #     radius, height = dimensions
    #     print(CylinderAreaAndVolume().get_area_and_volume(radius, height))
    # if shape == 'cone':
    #     radius, height = dimensions
    #     print(ConeAreaAndVolume().get_area_and_volume(radius, height))
    # if shape == 'sphere':
    #     radius = dimensions[0]
    #     print(SphereAreaAndVolume().get_area_and_volume(radius))
    if user_input == 'q':
        break
