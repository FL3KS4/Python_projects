import window
import xml.etree.ElementTree as ET

class Atom(object):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, size, color):
        self.pos_x = float(pos_x)
        self.pos_y = float(pos_y)
        self.size = float(size)
        self.speed_x = float(speed_x)
        self.speed_y = float(speed_y)
        self.color = color

    def move(self, width, height):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        #TODO 1: Bounding in window
        if not (width - self.size > self.pos_x > self.size):
            self.speed_x = -self.speed_x
        if not (height - self.size > self.pos_y > self.size):
           self.speed_y = -self.speed_y
        
        


#TODO 4: Implement a method to bounce atoms from each other.

    def bounce(self, atoms):
        if(atoms[0][0] != self.pos_x):
            if -self.size < (atoms[0][0] - self.pos_x) < self.size:
                if -self.size < (atoms[0][1] - self.pos_y) < self.size:
                    self.speed_x = -self.speed_x
                    self.speed_y = -self.speed_y
        

    def to_tuple(self):
        return (self.pos_x, self.pos_y, self.size, self.color)


"""
TODO 2:
Create class FallDownAtom which will inherit from Atom. This new class will be affected by gravity.
At the end of the lifetime of FallDownAtom object it will stop completely.
"""
class FallDownAtom(Atom):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, size, color, lifetime):
        super().__init__(pos_x, pos_y, speed_x, speed_y, size, color)

        self.lifetime = float(lifetime)
        
    def move(self, width, height):
        if(self.lifetime == 0 and (self.pos_y + self.size) == height):
            self.speed_x = self.speed_x - 1 
            self.speed_y = self.speed_y - 1          
            
        else:    
            self.pos_x += self.speed_x
            self.speed_y += 10
            self.pos_y += self.speed_y
            if(self.lifetime != 0):
                self.lifetime = self.lifetime - 1

            if (self.pos_y + self.size) > height:
                self.pos_y = height - self.size
                self.speed_y = -self.speed_y
            elif (self.pos_y - self.size) < 0:
                self.pos_y = 0 + self.size
                self.speed_y = -self.speed_y
            elif (self.pos_x + self.size) > width:
                self.pos_x = width - self.size
                self.speed_x = -self.speed_x
            elif (self.pos_x - self.size) < 0:
                self.pos_x = 0 + self.size
                self.speed_x = -self.speed_x
        

    def to_tuple(self):
        return (self.pos_x, self.pos_y, self.size, self.color)


class Word(object):

    def __init__(self, width, height):
        self.size_x = width
        self.size_y = height
        self.atoms = []
        self.normal_atoms = 0
        self.falldown_atoms = 0
        self.load_from_xml("atoms.xml")

    #TODO 3: load from XML 'atoms.xml'
    def load_from_xml(self, filename):
        tree = ET.parse('atoms.xml')
        atoms = tree.findall('atom')
        for a in atoms:
            position = a.find('position').text
            px, py = position.split(',')
            velocity = a.find('velocity').text
            vx, vy = velocity.split(',')
            radius = a.find('radius').text
            color = a.find('color').text
            self.atoms.append(FallDownAtom(px, py, vx, vy, radius, color,200))
            self.falldown_atoms += 1

    def tick(self, size_x, size_y):
        ret = []
        for atom in self.atoms:
            
            
            atom.move(size_x, size_y)
            ret.append(atom.to_tuple())
            atom.bounce(ret)
        return tuple(ret)
        

    def get_size(self):
        return (self.size_x, self.size_y)
        
    def __str__(self):
        return "World size={}x{}\nNumber of normal atoms = {}\nNumber of falldown atoms = {}".format(self.size_x, self.size_y, self.normal_atoms, self.falldown_atoms)



if __name__ == '__main__':
    size_x, size_y = 640, 480
    world = Word(size_x, size_y)
    print(world)
    window.run(world.get_size(), world)
