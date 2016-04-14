from Tkinter import *
from math import *
import thread
import random
import time
import glob

class light_source:
    def __init__(self, lid=0, x_pos=0, y_pos=0, power=0):
        self.light_id = lid
        self.x = x_pos
        self.y = y_pos
        self.intensity = power

class brait_bot:

    speed_mult = 1.0

    def __init__(self, bbid, sz, x_pos, y_pos, w, s, bdy):
        self.bot_id = bbid
        self.size = sz
        self.x = x_pos
        self.y = y_pos
        self.wheel_speeds = w
        self.sensor_readings = s
        self.body = bdy
        self.heading = 0.0
        self.center_x = 0.0
        self.center_y = 0.0
        self.theta = 0.0
    def setup_center(self):
        ##assuming body[0] is rear left, body[1] is front left,
        ##body[2] is rear right, body[3] is front right
        self.center_x = min(self.body[3][0],self.body[0][0]) +\
                        sqrt(pow((self.body[3][0]-self.body[0][0]),2))/2.0
        self.center_y = min(self.body[3][1],self.body[0][1]) +\
                        sqrt(pow((self.body[3][1]-self.body[0][1]),2))/2.0

    def set_heading(self):
        dist_center_b3 = (pow((self.body[3][0]-self.center_x),2)) +\
                         (pow((self.body[3][1]-self.center_y),2))

        distHalf_b1_b3 = sqrt( (pow((self.body[3][0]-self.body[1][0]),2)) +\
                               (pow((self.body[3][1]-self.body[1][1]),2)) )/2.0
        phi = degrees( acos(distHalf_b1_b3/ sqrt(dist_center_b3)) )
        alpha = 90.0-phi

        dist_b3y_centery = sqrt( pow((self.body[3][1]-self.center_y),2) )
        beta = degrees( asin(dist_b3y_centery/ sqrt(dist_center_b3)) )

        if self.body[3][1] > self.center_y:
            self.heading = alpha+beta
        else:
            self.heading = alpha-beta

    def sense(self, lights):
        s1_list = []
        s2_list = []

        slope = (self.body[1][1] - self.body[3][1])/(self.body[1][0] - self.body[3][0])
        #doing some finalgaling here
        boundery = -slope*self.body[1][0] + self.body[3][1]

        for light in lights:
            print str(light.y)+' '+str(light.x)+' '+str(slope)+' '+str(boundery)+' '+str(light.x*slope)+'\n'
            if light.y >= (boundery +( light.x*slope)):
                dist_s1_l = sqrt( (pow((self.body[1][0]-light.x),2)) +\
                                    (pow((self.body[1][1]-light.y),2)) )
                dist_s2_l = sqrt( (pow((self.body[3][0]-light.x),2)) +\
                                    (pow((self.body[3][1]-light.y),2)) )
                s1_list.append(light.intensity/dist_s1_l)
                s2_list.append(light.intensity/dist_s2_l)
                print "Bot sensors: "+str(light.intensity/dist_s1_l)+' '+str(light.intensity/dist_s2_l)+'\n'
            else:
                print "Ignored\n"
        #print str(max(s1_list))+' '+str(max(s2_list))+'\n'
        if ( (len(s1_list) == 0 and len(s2_list) == 0) \
             or fabs( max(s1_list) - max(s2_list) ) < .0001):
            self.theta = 0
        elif max(s1_list) > max(s2_list):
            self.theta += 5
        else:
            self.theta -= 5
        del s1_list[:]
        del s2_list[:]

    def move(self):
        print str(speed_mult*5*cos( radians((self.heading+self.theta)) ))+' '+str(speed_mult*5*sin( radians((self.heading+self.theta)) ))+'\n'

        for i in range(len(self.body)):
            self.body[i][0] = (self.body[i][0] + speed_mult*5*cos( radians((self.heading+self.theta)) ))%800
            self.body[i][1] = (self.body[0][1] + speed_mult*5*sin( radians((self.heading+self.theta)) ))%600

        self.center_x = (self.center_x + speed_mult*5*cos( radians((self.heading+self.theta)) ))%800
        self.center_y = (self.center_y + speed_mult*5*sin( radians((self.heading+self.theta)) ))%600

        self.heading+=self.theta
        self.theta = 0

def circle_coords( center, radius ):
    return [center[0]-radius, center[1]-radius, center[0]+radius+1, center[1]+radius+1]

def init_objects(canvas, n):
    inputBots = inputFile("./Bots/")
    inputLights = inputFile('./Lights/')
    sanitizeBots = sanitize_input(inputBots)
    sanitizeLights = sanitize_input(inputLights)

    init_lights = []
    for lights in sanitizeLights:
        nLight = light_source(lights[0], lights[1], lights[2], lights[3])
        init_lights.append(nLight)

    init_bots = []
    for bot in sanitizeBots:
        nBot = brait_bot(float(bot[0]),2,50,50,[float(bot[1]),float(bot[2])],[float(bot[3]),float(bot[4])],[[float(bot[5]),float(bot[6])],[float(bot[7]),float(bot[8])],[float(bot[9]),float(bot[10])],[float(bot[11]),float(bot[12])]])
        init_bots.append(nBot)

    for light in init_lights:
        canvas.create_oval( circle_coords( [float(light.x),float(light.y)], 2.), fill='yellow' )
        print "Light: "+str(light.x)+' '+str(light.y)+' '+str(light.intensity)+'\n'

    for bot in init_bots:
        bot.setup_center()
        bot.set_heading()
        canvas.create_oval( circle_coords( [float(bot.center_x),float(bot.center_y)], 2. ), fill='green' )
        print "Bot: "+str(bot.center_x)+' '+str(bot.center_y)+'\n'+str(bot.body)+'\n'+str(bot.heading)+'\n'

    # plight = light_source(1,100,100,75)
    # plight2 = light_source(2,150,150,100)
    # pbot = brait_bot(1,2,50,50,[0,0],[0,0],[[1,1],[1,2],[2,1],[2,2]])

    # pbot.setup_center()
    # pbot.set_heading()
    # print "Light: "+str(plight.x)+' '+str(plight.y)+' '+str(plight.intensity)+'\n'
    # print "Bot: "+str(pbot.center_x)+' '+str(pbot.center_y)+'\n'+str(pbot.body)+'\n'+str(pbot.heading)+'\n'

    # pbot_1 = canvas.create_oval( circle_coords( [pbot.center_x,pbot.center_y], 2. ), fill='green' )
    # plight_1 = canvas.create_oval( circle_coords( [plight.x,plight.y], 2.), fill='yellow' )
    # plightw_1 = canvas.create_oval( circle_coords( [plight2.x,plight2.y], 2.), fill='yellow' )


    while( True):#pbot.center_x < 125 and pbot.center_y < 125 ):
        for bot in init_bots:
            bot.sense(init_lights)
            bot.move()
            canvas.coords( bot, *circle_coords([bot.center_x,bot.center_y], 2.) )
            time.sleep(.5)


        # pbot.sense([plight,plight2])
        # print "Bot: "+str(pbot.theta)+'\n'
        # pbot.move()
        # print "Bot: "+str(pbot.center_x)+' '+str(pbot.center_y)+'\n'+str(pbot.body)+'\n'+str(pbot.heading)+'\n'
        # canvas.coords( pbot_1, *circle_coords([pbot.center_x,pbot.center_y], 2.) )
        # time.sleep(.5)

# ===============================
# IMPORT FILE FUNCTION
# ===============================
def inputFile(path):
    print path
    filenames = glob.glob(path+"*.txt")
    print filenames
    text =[]
    for file in filenames:
        text += open(file,'r')
    return text

# ===============================
# SANITIZE INPUT FUNCTION
# ===============================
def sanitize_input(text):
    sanitized_text = []
    for word in text:

#       Get rid of punctuation, convert to lower, remove new line characters
#       text = text.translate(None, string.punctuation).lower()

        sanitize = re.sub("[^\w']|_", " ", word.lower())
        words = list(sanitize.split())

#       List of lists to keep books structure
        sanitized_text.append(words)
        sanitized_text = input_toNumber(sanitized_text)
    return sanitized_text

def input_toNumber(text):
    sanitized_number = []
    for word in text:
        temp = []
        for number in word:
            new = float(number)
            temp.append(new)
        sanitized_number.append(temp)
    return sanitized_number

inputBots = inputFile("./Bots/")
inputLights = inputFile('./Lights/')
sanitizeBots = sanitize_input(inputBots)
sanitizeLights = sanitize_input(inputLights)
# ARRAY OF BOTS
print sanitizeBots
# ARRAY OF LIGHTS
print sanitizeLights


#body_coords = circle_coords( [robot[0].x, robot[0].y], 5. )
#heading_coords = [robot[0].x, robot[0].y, robot[0].x+5*cos(robot[0].orientation), robot[0].y+5*sin(robot[0].orientation)] #the '5' is the radius of the robot
#canvas.coords( robot[1][0], *body_coords ) #I do not understand why the * makes this work
#canvas.coords( robot[1][1], *heading_coords ) #I do not understand why the * makes this work
#[canvas.create_oval( body_coords, fill='' ),\
#canvas.create_line( heading_coords, fill='green',\
#arrowshape=[4,5,2], arrow='last')] #green is for real robot



master = Tk()

w = Canvas(master, width=800, height=600)
w.pack()

thread.start_new_thread( init_objects , (w, 5))

mainloop()
