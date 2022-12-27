#Read this if you are looking at this code for the first time.
#Welcome! This is the code for the centralized information sharing between self-driving cars.

#(note, if you are viewing this through word, the lines will be different from what the code says, if this is the case, search for the phrase given)

#This code is designed to be run as is, the only dependency is the math python package, which is included in the Python Standard Library (so the installation in this code is all that's needed beyond python itself).
#For Computer Science people (this section isn't required):
# This code is all in one file to make it easier to send, but if you would like to run it in your text editor and set up an import system (which is the way I run the code, but doesn't
# impact functionality), everything will be marked with "math" for the mathematical/generic functions required for the code to work, and "structure" for the things that build the structure of the system.
# Imports should be set up as follows: sections marked with math go in the "math" file, which imports the python math library. "Structure" sections go in the structure file, which should import "math". This can be the end, with work being done in the structure file,
#or you could import structure to another file called "interface" where you actually work with the specific environment/cars/lamps/signs you want.

#Instructions for use begin at line 490 (begins with Hello!)




import math #math

def type_check(lst,types): #math
    new = []
    for x in lst:
        if type(x) in types:
            new.append(True)
        else:
            new.append(False)
    if False in new:
        return False
    else:
        return True

def replace(list,value,new): #math
    list[list.index(value)] = new


def distance_p(p_1, p_2): #math
    d_x = p_1[0] - p_2[0]
    d_y = p_1[1] - p_2[1]
    final = math.hypot(d_y, d_x)
    return final

def simplify(lst): #math
    new = []
    for x in lst:
        if x not in new:
            new.append(x)
        else:
            pass
    return new

class BoundError(Exception): #math
    pass
class OverlapError(Exception): #math
    pass

class matrix(): #math
    def __init__(self,data): #size[0] is collums, size[1] is rows
        if data == None:
            self.data = [[None,None],[None,None]]
        if len(data) == 2 and len(data[0]) == 2 and len(data[1]) == 2:
            if type_check(data[0],[int,float]) and type_check(data[1],[int,float]):
                self.data = data
            else:
                raise ValueError("data must be a list of 2 lists, both with only ints or floats")
        else:
            raise ValueError ("data must be a list of 2 lists, both with only ints or floats")
        self.a = data[0][0]
        self.b = data[0][1]
        self.c = data[1][0]
        self.d = data[1][1]
    def __repr__(self):
        x = str(self.data[0]) + "\n" + str(self.data[1])
        return x
    def replace_row(self,old,new): #old is 0 or 1
        if old == 0:
            new_matrix = matrix([new,self.data[1]])
        if old == 1:
            new_matrix = matrix([self.data[0],new])
        return new_matrix
    def det(self):
        return self.a*self.d - self.b*self.c
    def replace_collum(self,old,new): #old is 0 or 1
        if old == 0:
            new_matrix = matrix([[new[0],self.data[0][1]],[new[1],self.data[1][1]]])
        if old == 1:
            new_matrix = matrix([[self.data[0][0],new[0]],[self.data[1][0],new[1]]])
        return new_matrix
def cramer(eq_1,eq_2): #math
    answers = [eq_1[2],eq_2[2]]
    r_1 = [eq_1[0],eq_1[1]]
    r_2 = [eq_2[0],eq_2[1]]
    coefficent_matrix = matrix([r_1,r_2])
    x_matrix = coefficent_matrix.replace_collum(0,answers)
    y_matrix = coefficent_matrix.replace_collum(1,answers)
    y_co = x_matrix.det()/coefficent_matrix.det()
    x_co = y_matrix.det()/coefficent_matrix.det()
    return (x_co,y_co)
def perp(p_1,p_2): #math
    x = (p_1[0]+p_2[0])/2
    y = (p_1[1]+p_2[1])/2
    mid = (x,y)
    delta_x = p_1[0]-p_2[0]
    delta_y = p_1[1]-p_2[1]
    try:
        slope = -1/(delta_y/delta_x)
        perp_bi = [1, -1 * slope, mid[1] - slope * mid[0]]
    except ZeroDivisionError:
        if delta_x == 0:
            perp_bi = [0, 1, mid[1]]
        if delta_y == 0:
            perp_bi = [0, 1, mid[0]]
    return perp_bi

def box_lines(dim): #returns counterclockwise starting with left #math
    left_line = [0,1,0]
    right_line = [0,1,dim[0]]
    bot_line = [1,0,0]
    top_line = [1,0,dim[1]]
    return [left_line,bot_line,right_line,top_line]

def is_in(box,point): #math
    if point[0] >= 0 and point[1] >= 0 and point[0] <= box[1] and point[1] <=box[0]:
        return True
    else:
        return False


def box_intersections(box,line): #math
    if type(box) == env:
        borders = box_lines(box.dim)
    if type(box) == list or type(box) == tuple:
        borders = box_lines(box)
    else:
        raise TypeError ("Box can only be an env or a list of dimensions")
    points_1 = []
    points = []
    for border in borders:
        points_1.append(cramer(border,line))
    for item in points_1:
        if is_in(box,item):
            points.append(item)
        else:
            pass
    return points
def perp_bi_inter(box,points):#math
    perp_line = perp(points[0],points[1])
    return box_intersections(box,perp_line)


def side(box, points): #math
    b_l = (0, 0)
    b_r = (box[0], 0)
    t_r = (box[0], box[1])
    t_l = (0, box[1])
    line = perp(points[0], points[1])
    corners = [b_l, b_r, t_r, t_l]
    left_corners = []
    right_corners = []
    x_values = [points[0][0], points[1][0]]
    y_values = [points[0][1], points[1][1]]
    left_x = min(x_values)
    if left_x == points[0][0]:
        left_point = points[0]
        right_point = points[1]
    if left_x == points[1][0]:
        left_point = points[1]
        right_point = points[0]
    right_dict = {}
    left_dict = {}
    if x_values[0] != x_values[1] and y_values[0] != y_values[1]:
        for corner in corners:
            if corner[0] > (line[2] / line[1]) - ((line[0] * corner[1]) / line[1]):
                right_corners.append(corner)
            if corner[0] < (line[2] / line[1]) - ((line[0] * corner[1]) / line[1]):
                left_corners.append(corner)
            if corner[0] == (line[2] / line[1]) - ((line[0] * corner[1]) / line[1]):
                pass
                # what if the corner is on the perpendicular bisector?
    else:
        if x_values[0] == x_values[1] and y_values[0] == y_values[1]:
            raise ValueError("These points are the same")
    right_dict[right_point] = right_corners
    left_dict[left_point] = left_corners
    return [left_dict, right_dict]

def get_binary_distance(box,points): #math
    place_holder = list(side(box,points)[0].keys())[0]
    place_holder_2 = list(side(box,points)[1].keys())[0]
    place_holder_1_1 = list(side(box,points)[0].values())[0]
    place_holder_2_1 = list(side(box, points)[1].values())[0]
    distances = []
    for x in place_holder_1_1:
        distances.append(distance_p(x,place_holder))
    for x in place_holder_2_1:
        distances.append(distance_p(x, place_holder_2))
    return max(distances)




class obj: #math
    def __init__(self,pos,env=None):
        if type(env) == env:
            self.env = env
        if type(env) == type(None):
            self.env = env
        else:
            raise TypeError("Env needs to be an enviornment")
        if type(pos) == list or type(pos) == tuple:
            self.x = pos[0]
            self.y = pos[1]
            self.pos = pos
        else:
            raise TypeError ("Position needs to be a list of coordinates")
    def distance(self,other):
        return math.hypot((self.pos[0]-other.pos[0]),(self.pos[1]-other.pos[1]))

class car(obj): #structure
    def __init__(self,pos,ID,vel,acc,dim):
        self.pos = pos
        self.ID = ID
        self.acc = acc
        self.vel = vel
        self.width = dim[0]
        self.length = dim[1]
        self.dim = dim
        self.info = packet(self)
        self.cars_near = []
        self.lamps_near = []
        self.needed_info = []
        self.signs_near = []
    def __repr__(self):
        return self.ID
    def get_lamps_near(self):
        if self.env == None:
            pass
        else:
            for x in self.env.lamps:
                if self in x.near:
                    self.lamps_near.append(x)
                else:
                    pass

    def edit_info(self,id,new_info):
        for x in self.cars_near:
            if x.id == id:
                self.cars_near[self.cars_near.index(x)] = new_info
            else:
                pass
    def set_env(self,env):
        self.env = env
    def send(self,new_info):
        for x in self.lamps_near:
            x.send(new_info)
    def move(self,time):
        delta_distance_x = self.vel.x*time + (1/2)*(self.acc.x)*(time**2)
        delta_distance_y = self.vel.y * time + (1 / 2) * (self.acc.y) * (time ** 2)
        self.info[0] = (self.pos[0]+delta_distance_x,self.pos[1]+delta_distance_y)
        self.pos = (self.pos[0]+delta_distance_x,self.pos[1]+delta_distance_y)
        new_vel_x = self.vel.x + time*(self.acc.x)
        new_vel_y = self.vel.y + time*(self.acc.x)
        self.vel = vector(new_vel_x,new_vel_y)
        self.info[0] = vector(new_vel_x,new_vel_y)
        self.send(self.info)
        self.env.check_car_over()
        self.env.check_bound()
    def update_signs(self):
        self.signs_near = [[x for x in self.signs_near if distance_p((self.pos[0],self.pos[1]),(x.x,x.y))<10],[x for x in self.signs_near if distance_p((self.pos[0],self.pos[1]),(x.x,x.y))>10]]





class vector: #math
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mag = math.hypot(x,y)
        self.dir = math.atan2(y,x)
    def __repr__(self):
        return str((self.x,self.y))
    def __add__(self, other):
        return vector(self.x+other.x,self.y+other.y)
    def __mul__(self, other):
        return vector(self.x*other,self.y*other)


class env: #structure
    def __init__(self,cars,lamps,stopsigns,dim):
        self.cars = cars
        self.lamps = lamps
        self.stopsigns = stopsigns
        self.dim = dim
        self.initialize_adjustments()

    def initialize_adjustments(self):
        for x in self.cars:
            x.set_env(self)
        for x in self.lamps:
            x.set_env(self)
        self.fix_range()
        for x in self.cars:
            x.get_lamps_near()
        for x in self.lamps:
            x.fix_near()
        for x in self.cars:
            x.send(x.info)
        for x in self.lamps:
            if self.stopsigns != None:
                for y in x.near:
                    for z in x.env.stopsigns:
                        if z not in y.signs_near:
                            y.signs_near.append(z)
        for x in self.cars:
            x.update_signs()
        self.check_car_over()
        self.check_lamp_over()
        self.check_bound_car()
        self.check_bound_lamp()


    def fix_range(self):
        ranges = []
        if self.get_lamps() != None and len(self.get_lamps())>1:
            for first_iterator in self.get_lamps():
                for second_iterator in [x for x in self.get_lamps() if x != first_iterator]:
                    ranges.append(get_binary_distance(self.dim,[first_iterator.pos,second_iterator.pos]))
            for lamp in self.get_lamps():
                lamp.set_range(min(ranges))
        if self.get_lamps() != None and len(self.get_lamps()) == 1:
            a = distance_p((self.get_lamps()[0].pos[0],self.get_lamps()[0].pos[1]),(0,0))
            b = distance_p((self.get_lamps()[0].pos[0],self.get_lamps()[0].pos[1]),(0,self.dim[1]))
            c = distance_p((self.get_lamps()[0].pos[0],self.get_lamps()[0].pos[1]),(self.dim[0],0))
            d = distance_p((self.get_lamps()[0].pos[0],self.get_lamps()[0].pos[1]),(self.dim[0],self.dim[1]))
            self.get_lamps()[0].set_range(max([a,b,c,d]))
        else:
            pass
    def check_car_over(self):
        locations = []
        for x in self.cars:
            locations.append(x.pos)
            if len(locations) != len(set(locations)):
                raise OverlapError(
                    "Intentional Error: two of your cars are in the same place (check the positions of all of your cars)")
    def check_lamp_over(self):
        locations = []
        for x in self.lamps:
            locations.append(x.pos)
            if len(locations) != len(set(locations)):
                raise OverlapError("Intentional Error: two of your lamps are in the same place (check the positions of all of your lamps)")
            else:
                locations.append(x.pos)
    def get_range(self):
        return self.get_lamps()[1].range
    def get_cars(self):
        return self.cars
    def get_lamps(self):
        return self.lamps
    def get_stopsigns(self):
        return self.stopsigns
    def add_car(self,car):
        self.cars.append(car)
        car.set_env(self)
        for x in self.lamps:
            x.fix_near()
        car.get_lamps_near()

        for x in self.cars:
            x.get_lamps_near()

        for x in self.cars:
            x.send(x.info)

    def add_lamp(self,lamp):
        if self.lamps == None:
            self.lamps = [lamp]
        else:
            self.lamps.append(lamp)
            self.fix_range()
        lamp.set_env(self)
    def add_stopsign(self,sign):
        self.stopsigns.append(sign)
    def send(self,new_info,sender):
        for my_lamp in self.lamps:
            if my_lamp != sender:
                my_lamp.send_2(new_info)
    def pass_time(self,time):
        for vehicle in self.cars:
            vehicle.move(time)
    def check_bound_car(self):
        for x in self.cars:
            if x.pos[0] > self.dim[0] or x.pos[0] < 0 or x.pos[1] > self.dim[1] or x.pos[1] < 0:
                raise BoundError ("Intentional Error: At least one of your cars has is outside the environment (check your cars' positions, if this was caused by moving or passing time, your car left the environment and the movement' didn't occur.")
    def check_bound_lamp(self):
        for x in self.lamps:
            if x.pos[0] > self.dim[0] or x.pos[0] < 0 or x.pos[1] > self.dim[1] or x.pos[1] < 0:
                raise BoundError ("Intentional Error: At least one of your lamps has is outside the environment (check the positions of your lamps)")




class lamp(obj): #structure
    def __init__(self,pos,range = None,env = None):
        self.pos = pos
        self.near = []
        self.range = range
        self.near_info = [x.info for x in self.near]
        self.near_id = [x.ID for x in self.near]
        self.env = env
    def get_near_info(self):
        return self.near_info
    def get_near_id(self):
        return self.near_id

    def get_env(self):
        return self.env
    def fix_near(self):
        a = []
        if self.env == None:
            pass
        else:
            for x in self.env.cars:
                if distance_p(self.pos,x.pos) <= self.range:
                    a.append(x)
        self.near = a
        self.near_info = [x.info for x in self.near]
        self.near_id = [x.ID for x in self.near]

    def set_range(self,range):
        self.range = range
        self.fix_near()

    def edit_info(self,id,new_info):
        if id in self.near_id:
            for x in self.near_info:
                if x.id == id:
                    self.near_info[self.near_info.index(x)] = new_info
                else:
                    pass
    def return_near(self):
        return self.near
    def set_env(self,env):
        self.env = env

    def send(self, new_info):
        for car_near in self.near:
            if car_near.info != new_info:
                if new_info.id in [car_near.id for car_near in car_near.needed_info]:
                    ind = [car_near.id for car_near in car_near.needed_info].index(new_info.id)
                    replace(car_near.needed_info, car_near.needed_info[ind], new_info)
                else:
                    car_near.needed_info.append(new_info)
        self.env.send(new_info,self)
    def send_2(self, new_info):
        for car_near in self.near:
            if car_near.info != new_info:
                if new_info.id in [car_near.id for car_near in car_near.needed_info]:
                    ind = [car_near.id for car_near in car_near.needed_info].index(new_info.id)
                    replace(car_near.needed_info, car_near.needed_info[ind], new_info)
                else:
                    car_near.needed_info.append(new_info)

class sign(obj): #structure
    def __init__(self,msg,pos):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.msg = msg
    def __repr__(self):
        return (str(self.msg) + " at " + str(self.pos))

class packet: #structure
    def __init__(self,car):
        self.data = [car.ID, [car.pos, car.dim, car.vel, car.acc]]
        self.id = self.data[0]
    def __setitem__(self, key, value):
        self.data[1][key] = value
    def __getitem__(self, item):
        return self.data[1][item]
    def __repr__(self):
        return str(self.data)








#Hello!
#You can use this program in one of two ways. Either read starting at line 495 (begins with "Pre-built" for word users) for complete instructions,or follow the instructions starting at line 530 (begins with "Welcome to" for word users) to build your own system.



#Pre-built system instructions
#Remove the # from the beginning of each line of code until line 527 (ends with "(red_car.signs_near[1]))" for word users). Important note: Unless you have read the use instructions starting at line 530 (begins with "Welcome to" for word users),either use all of this code or none of it.
#The code is designed such that, unless you edit the problematic lines manually, it will raise an error if some but not all lines are activated (done by removing the #)


#red_car = car((1,1),"red",vector(1,1),vector(2,2),(4,3))
#blue_car = car((21,7),"blue",vector(3,2),vector(2,5),(4,3))
#blue_car = car((37,45),"blue",vector(3,2),vector(2,5),(4,3))
#green_car = car((93,6),"blue",vector(4,1),vector(4,2),(6,3))

#stop_sign = sign("Stop",(40,40))
#detour_sign = sign("The speed limit is 50 mph",(4,4))

#lamp_a = lamp((1,3),None,None)
#lamp_b = lamp((77,45),None,None)
#lamp_c = lamp((45,68),None,None)

#test_env = env([red_car,blue_car,green_car],[lamp_a,lamp_b,lamp_c],[stop_sign,detour_sign],(110,120))


#print("This is the range of the lamps in the environment: " + str(test_env.get_range()))

#print("This is the information about the red car (taken directly from the red car): " + str(red_car.info))

#print("This is what the blue_car knows about the red car (taken directly from the blue car): " + str(blue_car.needed_info[0]))

#test_env.pass_time(1)

#print("Red's updated information after moving for one second: " + str(red_car.info))

#print("The red car knows about these signs within 10 units: " + str(red_car.signs_near[0]))

#print("The red car knows about these signs within 10 units: " + str(red_car.signs_near[1]))


#Welcome to the instructions for building your own system. To note, these instructions will be longer than the test cases above, and it's important to read all of them.
#Small errors in setup will cause the program to fail, any intentional failures (ex. placing a car outside of the environment or placing 2 cars in the same position, will be labeled.
#These errors will say "intentional error" and give suggestions with the way to fix the error. All other errors are a function of a mistake in typing the code.

#Step 1: making the cars. Start a new line, and type the name of your car. This name should be simple and can't include spaces. Examples include car_1 or red_car.
#Next, write an equals sign followed by the word car in parentheses. It should look like this: example_car = car()
#Within the parenthesis, write the following (order is important)
# 1. the coordinates of the car, in parenthesis, separated by a comma. (3,4) will work, but (34) or 3,4 will not.
# 2. close the parenthesis, and type a comma. In quotes, write a name for your car. This can be, but doesn't have to be, the name you gave it before the equals sign. This name can include spaces, numbers, and any symbol in the English Language.
# "red car" will work, but red car will not.
# 3. make sure you have an end quote, and type another comma. Here you will type vector(x,y). Don't actually type the letters x and y, these are stand ins for the x and y components of the car's
#velocity vector. Make sure the two are separated by a comma.
#4. type another comma, and do the same process of typing vector = (x,y), except this time it represents the acceleration vector of the car.
#5. type another comma, and type another set of numbers in parenthesis, separated by a comma (the same process as creating the position). This represents the dimensions of the car
#repeat this process for every car you want to create

#step 2:
#repeat a similar process with lamps
#the general formula is name of lamp = lamp()
#just like you did for the car, fill in the lamp with the following parameters in order
# an ordered pair of coordinates for the position, None, None
#example: test_lamp = lamp((1,1),None,None)) Make sure there are the right number of parentheses, and make sure to separate with commas.

#step 3:
#repeat a similar process with signs
#the general formula is name of sign = sign()
#the parameters for the lamp are, in order "the function of the sign" (quotes are important, example: "stop" or "speed limit is 50 mph), followed by a position. The position
#needs to be in parentheses, separated by a comma.
#example: test_sign = sign("stop",(50,50))

#step 4:
#You're finally creating the environment!
#just like the other things you've made, the format is: name of environment = env()
#the parameters for environment are slightly more complex, this is what you need to do
#the first thing to do is type this: []
#within the empty brackets, type the names of each car (the one before the equals sign, not the one in quotes), separated by a comma
#it should look like this: [red_car,blue_car,green_car] (if you only have one that's ok, don't include any commas)
#create another set empty brackets, filled with the lamps (still separated by commas)
#it should look like this [lamp_a,lamp_b,lamp_c]
#do the same thing with signs
#lastly, just like you did with car position, create an ordered pair to represents the dimensions like (40,40)




#very important note!!! Always create your objects in this order, other orders can raise errors.



#congrats! the setup's all done!

#these are some useful commands to use this setup

#name of your environment.pass_time(time)
#name of your environment is whatever you called it before the equals sign and time is the amount of time you want to pass. This will simulate passing time, and all of the cars will move accordingly.
#example: test_env.pass_time(3)
#the pass_time function won't print anything, but it will update the information that is printed after
#to acces the range of your lamps (only after the environment has been created) type: print(name of your lamp.range)
#example: print(lamp_a.range)
#to view a car's information, type print(name of your car.info)
#example: print(red_car.info)
#to view what each car knows about the other cars, type print(name of your car.needed_info)
#example print(red_car.needed_info)
#to view what signs a car knows about, type print(name of your car.signs_near)
#adding [0] or [1] after this will change the output, with [0] giving the signs within 10 units and [1] giving the signs farther
#example: print(red_car.signs near)



