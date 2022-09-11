import os
import pygame, sys
import pygame.gfxdraw
import time
import random
from random import randint
import game
# the Label class is this module below
from label import *
import Buttonpic

pygame.init()
pygame.mixer.init()
right = pygame.mixer.Sound("sounds/right.wav")
wrong = pygame.mixer.Sound("sounds/wrong.wav")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
background = pygame.image.load("Pictures/bg.jpg")
Re = pygame.image.load('Pictures/reuse.png')
Exit = pygame.image.load('Pictures/exit_btn.png')
buttons = pygame.sprite.Group()
ReScore = pygame.image.load('Pictures/reset.png')
Menu = pygame.image.load('Pictures/menu.png')    


#create button instances
Re_button = Buttonpic.Button(600, 150, Re, 0.15)
Exit_button = Buttonpic.Button(600, 300, Exit, 0.5)
ReScore_button = Buttonpic.Button(500, 530, ReScore, 0.2)
Menu_button = Buttonpic.Button(150, 320, Menu, 0.5)

class Button(pygame.sprite.Sprite):
    ''' A button treated like a Sprite... and killed too '''
    
    def __init__(self, position, text, size,
        colors="",
        hover_colors="",
        style="",
        borderc=(),
        command=lambda: print("No command activated for this button")):

        # the hover_colors attribute needs to be fixed
        super().__init__()
        global num

        self.text = text
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        # hover_colors
        if hover_colors == "":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
        # styles can be button1 or button2 (more simple this one)
        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render(self.text)
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, 500, self.h)
        self.position = position
        self.pressed = 1
        # the groups with all the buttons
        buttons.add(self)


    def render(self, text):
        # we have a surface
        self.text_render = self.font.render(text, 1, self.fg)
        # memorize the surface in the image attributes
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == "button1":
            self.draw_button1()
        elif self.style == "button2":
            self.draw_button2()
        if self.command != None:
            self.hover()
            self.click()

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        lcolor = (150, 150, 150)
        lcolor2 = (50, 50, 50)
        pygame.draw.line(screen, lcolor, self.position,
            (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, lcolor, (self.x, self.y - 2),
            (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, lcolor2, (self.x, self.y + self.h),
            (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, lcolor2, (self.x + self.w , self.y + self.h),
            [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, self.rect)  

    def draw_button2(self):
        ''' a linear border '''
        # the width is set to 500 to have the same size not depending on the text size
        pygame.draw.rect(screen, self.bg, (self.x - 50, self.y, 500 , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x - 50, self.y, 500 , self.h), self.borderc)

    def check_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors
            # pygame.mouse.set_cursor(*pygame.cursors.arrow)


    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''

        self.check_collision()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("Your answer is:'" + self.text + "'")
                self.command()
                self.pressed = 0

            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1

new_r = []
i = 1
while( i <= 50 ):
    r = randint(1, 100)
    if( r not in new_r ):
        new_r.append( r )
        i = i + 1
print( new_r )
     

# ACTION FOR BUTTON CLICK ================

def on_click():
    print("Click on one answer")

def on_right():
    check_score("right")

def on_false():
    ''' if there is no 'right' as arg it means it's false '''
    check_score()

def check_score(answered="wrong"):
    ''' here we check if the answer is right '''
    global qnumc,qnum, points, high_score, x
    
    # until there are questions (before last)
     
    if qnumc < len(new_r):
        print(qnumc, len(new_r))
        if answered == "right":
            right.play() # click sound
            time.sleep(.1) # to avoid adding more point when pressing too much
            points += 1
            # Show the score text
        x += 1
        print(x)
        qnum = new_r[x]
        qnumc += 1  
       

        
        score.change_text("Your score: "+str(points), color="black")
        Your_on.change_text("You are currently on questions number "+str(qnumc)+" out of "+str(len(new_r))+" questions.", color="black")
        # Change the text of the question
        title.change_text(questions[qnum-1][0], color="black")
        # change the question number
        num_question.change_text(str(qnum))
        show_question(qnum) # delete old buttons and show new

        if answered == "wrong":
            wrong.play() # click sound
            time.sleep(.1)

     

    # for the last question...
    elif qnumc == len(new_r):
        print(qnumc, len(new_r))
        if answered == "right":
            right.play()
            kill()
            time.sleep(.1)
            points +=1
        x += 1

        score.change_text("You reached a score of " + str(points) +" / "+ str(len(new_r)),color="black")
        title.change_text("CONGRATULATIONS!")
        thank.change_text("THANK YOU FOR PLAYING") 
        if answered == "wrong":
            wrong.play()
            time.sleep(.1)
            kill()   
       
      
    


    time.sleep(.5)




questions = [
    ["Because of the severe weather, Mr.kim asked if ___ could leave the office a little earlier than usual.", ["he", "him", "himself", "his"]],
    ["If you ___ additional assistance, please do not hesitate to contact us.", ["require", "to require", "requiring", "requires"]],
    ["Please ___ your supervisor as soon as possible in the event of a machinery failure.",["notify", "express", "declare", "announce"]],
    ["The All-Bright safety vest is designed ___ bikers who travel at night.",["for", "of", "among", "from"]],
    ["Customers need not pay for shipping because it is ___ in the total price of the item.",["included", "balanced", "checked", "earned"]],
    ["All Gruner Corporation employees will be invited to the holiday ___ scheduled for next Friday.", ["celebration", "management", "attendance", "circumstance"]],
    ["Great Hope is Toshi Raymond's most inventive stage production ___", ["yet", "only", "once", "when"]],
    ["Dairy exports ___ for only five percent of the country's total agricultural sales.",["account", "assign", "charge", "contribute"]],
    ["When you are finished analyzing the survey data,please give ___ report to Ms.Chin",["your", "you", "yourself", "yours"]],
    ["The auditors'report indicates that the firm should ___ its manufacturing division.",["expand", "discover", "excel", "devise"]],
    #11
    ["It is not the company's policy to grant sick leave ___ overtime pay to part-time employees.",["or",'yet','if','but']],
    ["Negotiators should be aware that the Prime Minister has a very ___ manner of speaking.",["direct",'mutual','adjacent','existing']],
    ["The ___ of the Board of Directors is scheduled for Monday.",["election",'elected','elects','electable']],
    ["Investors who lose faith in a company ___ sell off their stocks and invest elsewhere.",["typically",'exactly','greatly','approximately']],
    ["The park service asks visitors to behave ___ and show respect for wildlife.",["respondsibly",'responsible','responsibility','responsibilities']],
    ["Ms.Walters ___ to another branch, so your new financial advisor will be Mr.Merenda.",["has transferred","transfer","transferring","transferable"]],
    ["A growing ___ in the cosmetics industry is the use of natural and organic ingredients.",["trend","product","scent","sale"]],
    ["Because of its ___ melodies and upbeat rhythms, Toby Nathan's music has broad appeal.",["simple","patient","kind","blank"]],
    ["Dr.Viella Diop is best known for her ___ contributions to the field of physics.",["significant","signify","significance","significantly"]],
    ["The Smithson Bank is well-known for the ___ welcome that it extends to all new exployees.",["warm","warmth","warmly","warmed"]],
    #21
    ["We will be hiring five part-time employees to ___ staff in the operations department.",["assist","assists","assisting","assisted"]],
    ["The two companies are now ___ the price Luco Ltd. will pay Gnose for the property in Quebec.",["negotiating","negotiate","negotiation","negotiated"]],
    ["Construction on the bridge ___, the two cities has progressed more rapidly than anticipated",["linking","was to link","linked","will be linked"]],
    ["Many analysts attribute Kramar Industries' ___ success to its state-of-the-art research department.",["phenomenal","phenomenon","phenomena","phenomenally"]],
    ["The travel agency will make your travel ___ and send your tickets to the end of the week.",["reservations","release","experiences","diagram"]],
    ["___ the past ten years,PTelecom has rewarded all of its employees with a generous vacation package.",["For","From","Before","After"]],
    ["This exciting new product is ___ of the new software that our developers are working on.",["representative","represents","representing","representation"]],
    ["The restaurant offers a wide selection of gourmet desserts ___ several regions of the world",["from","with","by","until"]],
    ["___interested in viewing an apartment should contact the property manager to arrange an appoinment.",["Those","These","This","That"]],
    ["___by the audience's positive reaction to its music, the Gary Jones Band played well past midnight.",["Delighted","Delightedly","Delightful","Delight"]],
    #31
    ["The Tourist Board is developing a marketing ___ to help them increase tourism to the region.",["proposal","permission","appliance","employment"]],
    ["The number of new textbooks ___ by the american publisher dropped for the 2nd year in a row.",["sold","priced","marked","instructed"]],
    ["Traffic congestion is ___ than usual because of road construction.",["worse","badly","bad","worst"]],
    ["garden maintenance companies must choose the right products and apply them ___",["correctly","correction","corrected","correcting"]],
    ["CTC announced that a European media group is expected to ___ its online music store.",["buy","buying","bought","has bought"]],
    ["The CEO will use her ___ in determining how the reorganization of the company will be conducted.",["discretion","discretionary","discrete","discretely"]],
    ["For more than two decades, Bee Construction has helped clients ___ their ideas into executed projects.",["transform","prevail","inspire","involve"]],
    ["___ you are buying or selling a house, be sure to use a real estate agent",["Whether","Until","Mainly","Only"]],
    ["The application process for loans from Inhouse Financing is easier than ___",["ever","once","never","not"]],
    ["Income from online advertising has been growing, but is still a ___ small part of newspaper revenue.",["relatively","nearly","closely","precisely"]],
    #41
    ["Companies that care more about customers than investors often achieve ___ growth",["significant","chief","prior","official"]],
    ["The fashion designer wanted to create dress styles ___ different from those of her contemporaries.",["recognizably","recognize","recognizing","recognizable"]],
    ["The Action Shot X52 underwater camera is recommended ___ depths of up to two hundred feet.",["for","as","but","out"]],
    ["Monthly reports from all divisions must be delivered to the human resources office ___ by 5 P.M. today.",["promptly","recently","formerly","briefly"]],
    ["The location of next month’s financial seminar is yet to be ___.",["concluded","prevented","restricted","invited"]],
    ["___ the firm's notable achievements this past year was the opening of a new research center in Seoul.",["Among","Into","Despite","Around"]],
    ["The revival of the ferry service was viewed as a ___ notion by many",["foolish","mobile","talkative","dedicated"]],
    ["According to a survey ___ by the Institute, advertising on the TV accounted for 60% of total advertising.",["conducted","conductor","conducting","conducts"]],
    ["Choosing the best software tool is not simple, ___ it is important to seek expert advice.",['so',"and","but","for"]],
    ["In spite of the rainy weather, last evening's holiday reception was ___ attended by staff and admins.",["well","quite","many","some"]],
    #51
    ["The report concerning the sales figures that you requested ___ on your desk.",["is","am","are","were"]],
    ["After Mr. Kently’s speech, some ___ will be served in the main lobby.",["refreshments","refresh","refreshing","refreshes"]],
    ["Before ___ us your resume, be sure to check that it meets our requirements precisely.",["sending","sends","to send","sent"]],
    ["During the factory tour, visitors must not ___ with any of the operations inside the plant.",["interfere","comply","attain","observe"]],
    ["The passenger was asked to place ___ luggage in the overhead compartments after boarding the plane.",["her","she","herself","hers"]],
    ["It is vital that the accuracy of measuring instruments ___ yearly.",["be tested","is tested","were testing","will test"]],
    ["Check that the lid is ___ sealed to prevent its contents from leaking.",["firmly","firm","firming","firmness"]],
    ["Mark will handle receptionist duties ___ a more urgent matter requires his attention.",["unless","since","so","because"]],
    ["Housing prices in the city are ___ more expensive than those in the suburb.",["substantially","personally","unanimously","individually"]],
    ["___ the logos had a remarkably similar design, they were created by two different companies.",["Although","Since","However","Because of"]], 
   #61
    ["The most important rule to prevent your T-Shirts from ___ is to avoid heat.",["shrinking","shrink","shrank","shrunk"]],
    ["After a 3-hour meeting, the board of directors decided to ___ our contract with Marcy Construction.",["terminate","attend","donate","benefit"]],
    ["Patient records ___ with “Confidential” in red ink are subject to stronger protection measures.",["stamped","are stamped","stamps","stamping"]],
    ["___ hotels charge a fee for cancellation within 24 hours of check-in, but the Fresia Hotel does not.",["Other","Another","Others","Each"]],
    ["Upon examination, Mr. Clark discovered that the figures Ms. Rose ___ last week were incorrect.",["calculated","calculate","has been calculated","will calculate"]],
    ["Records of all ___ between the landlord and the tenants should be kept on record.",["correspondence","opposition","instruction","substitution"]],
    ["The European Union is made up of 15 nations with ___ cultural, linguistic and economic roots.",["distinct","unclear","tentative","widespread"]],
    ["The novels he recommended ___ very boring and had no special character development.",["were","is","does","was"]],
    ["The software was designed to update the data continuously ___ the day.",["throughout","every","besides","regarding"]],
    ["Applicants will be asked to provide proof of ___ accounting certification at the first interview.",["their","they","theirs","them"]],
    #71
    ["The annual community football tournament welcomes teams of all ages and ___ abilities.",["athletic","athletes","athlete","athletically"]],
    ["We still enjoyed staying at Sunset Hotel despite many new apartments ___.",["being built","are being built","are built","build"]],
    ["Misuri Co. decided to ___ expand its product options to fulfill customers' needs",["strategically","flexibly","alternatively","accurately"]],
    ["The bank was able to attract many new customers by offering an ___ interest rate.",["attractive","attracts","attraction","attractively"]],
    ["Mr. Schmidt will ___ as Ms. Fabrey's replacement when she retires from her position.",["take over","make up","step down","break through"]],
    ["The company has decided to shut down one of its facilities due to its ___ maintenance.",["costly","costing","cost","costs"]],
    ["James Sullen ___ his career as a film director even before he graduated from Paris Art School.",["had begun","will begin","is beginning","has begun"]],
    ["Since the current printers ___ malfunction, we’ve decided to buy some newer models.",["frequently","frequent","frequented","frequency"]],
    ["___ a temporary shortage of natural resources, we’ve been forced to raise our prices.",["Because of","Therefore","While","Although"]],
    ["Most of the people ___ attended the workshop yesterday have submitted their feedback.",["who","which","whose","when"]], 
    #81
    ["Ruby Tech ___ needs to make improvements to its customer service policy or replace it altogether.",["either","both","neither","but"]],
    ["After replacing the ink cartridge, don’t forget to close the lid of the printer ___.",["securely","secure","securing","security"]],
    ["After Abby had worked for more than 10 years, she was ___ promoted to a managerial position.",["finally","final","finalize","finalizing"]],
    ["Applications for the annual BAC contest should ___ by no later than May 31st.",["be submitted","submit","be submitting","submitting"]],
    ["The KGH Bank collapsed ___ the uncertainty that investors had about the American economy.",["due to","besides","because","even though"]],
    ["Ms.Heartford suggested that I ___ with the client again before talking to the manager.",["negotiate","negotiating","will negotiate","have negotiated"]],
    ["___ domestic and overseas markets must be considered when exporting the products for a company.",["Both","Never","Neither","Either"]],
    ["Golden Goose Manufacturers has maintained the ___ safety standards of any company in its industry.",["highest","as high as","higher","height"]],
    ["The new novel by Stephen Muller ___ no later than the 13th of October according to a reliable source.",["will be published","will publish","is being published","published"]],
    ["The Nature Museum’s VIP members are ___ to enter the workshop and enjoy exclusive exhibitions.",["permitted","permit","permitting","permits"]],
    #91
    ["The owner of CC Tower may ___ the building if it does not pass the upcoming safety inspection.",["demolish","demolished","demolishing","demolishes"]],
    ["After extensive discussions, the two parties were finally able to find an ___ solution to the issue.",["agreeable","agree","agreeably","agreement"]],
    ["Fizzy Cola was found to have the ___ sugar content of all the soft drinks included in this study.",["highest","height","high","higher"]],
    ["Items ___ have been left behind will be stored at the lost-and-found office for three business days.",["that","who","by","when"]],
    ["Hotel guests should ___ the building promptly if they hear the fire alarm goes off.",["vacate","to vacate","vacated","vacating"]],
    ["KTV’s new series has proven to be ___ popular with viewers under the age of 30.",["immensely","immense","immensity","immensities"]],
    ["The names of the musical’s performers are listed in the program in order of ___.",["appearance","appear","appears","appeared"]],
    ["Participants in the walking tour should gather ___ Old Tree Coffee Shop on Saturday morning.",["at","with","like","among"]],
    ["___ this time next year, Renda Tech will have acquired three new subsidiaries.",["By","After","To","Quite"]],
    ["GFO was able to expand its network thanks to several important ___ in technology.",["advancements","celebrations","announcements","conclusions"]],
    #101 random 2-100
    ["",["","","",""]],

]


def show_question(qnum):
    # Kills the previous buttons/sprites
    kill()

    
    # The 4 position of the buttons
    pos = [100, 150, 200, 250]
    # randomized, so that the right one is not on top
    random.shuffle(pos)

    Button((10, 100), "A. ", 36, "blue on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)
    Button((10, 150), "B. ", 36, "blue on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)
    Button((10, 200), "C. ", 36, "blue on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)
    Button((10, 250), "D. ", 36, "blue on yellow",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=None)


    # ============== TEXT: question and answers ====================
    Button((50, pos[0]), questions[qnum-1][1][0], 36, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_right)
    Button((50, pos[1]), questions[qnum-1][1][1], 36, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_false)
    Button((50, pos[2]), questions[qnum-1][1][2], 36, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_false)
    Button((50, pos[3]), questions[qnum-1][1][3], 36, "black on white",
        hover_colors="blue on orange", style="button2", borderc=(255,255,0),
        command=on_false)


def kill():
    for _ in buttons:
        _.kill()
qnumc = 1
qnum = new_r[0]
points = 0
x = 0

#reset and new random
def reset():
    global qnumc,qnum,points,x,new_r,i
    new_r = []
    i = 1
    while( i <= 50 ):
        r = randint(1, 100)
        if( r not in new_r ):
            new_r.append( r )
            i = i + 1
    print( new_r )
    qnumc = 1
    qnum = new_r[0]
    points = 0
    x = 0
    thank.change_text("")
    score.change_text("Your score: "+str(points), color="black")
    Your_on.change_text("You are currently on questions number "+str(qnumc)+" out of "+str(len(new_r))+" questions.", color="black")
    title.change_text(questions[qnum-1][0], color="black")
    num_question.change_text(str(qnum))
    
    
    
    

# ================= SOME LABELS ==========================
num_question = Label(screen, str(qnum), 10, 15, size=50)
score = Label(screen, "Your score will be display here", 45, 500,size=30 ,color="Black")
high = Label(screen, "Your high score will be display here", 45, 530, size=30, color="black")
title = Label(screen, questions[qnum-1][0], 50, 30, size=20, color="black")
Your_on = Label(screen,"The questions you are currently on will be display here", 45, 470, size=30, color="black" )
thank = Label(screen, "", 45, 250,size=50 ,color="Black")

def loop():
    
    global game_on

    

    show_question(qnum)
    run = True
    while run:
        screen.blit(background,(0,0))   
        if x < len(new_r):
            if Re_button.draw(screen):
                loop()   

        if Exit_button.draw(screen):
            if points > high_score:
                 high_score = points
            with open('score.txt', 'w') as file:
                 file.write(str(high_score))
            pygame.quit()
        if os.path.exists('score.txt'):
            with open('score.txt', 'r') as file:
             high_score = int(file.read())
        else:
            high_score = 0 

        if ReScore_button.draw(screen):
            #Reset high score
            high_score = 0 
            with open('score.txt', 'w') as file:
                 file.write(str(high_score))
                 file.close()

        if x == len(new_r): 
            # Return to Main menu
             if Menu_button.draw(screen):
                #reset and new random
                reset()
                game.main_menu()
                

        if True:
            #update high score
            if points > high_score:
                high_score = points
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))
            high.change_text('Your high score: '+str(high_score), color="black")



        
        for event in pygame.event.get(): # ====== quit / exit 
            if (event.type == pygame.QUIT):
                if points > high_score:
                 high_score = points
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
        buttons.update() #                     update buttons
        buttons.draw(screen)
        show_labels()        #                 update labels
            
    
      
        clock.tick(60)
        pygame.display.update()  
          

if __name__ == '__main__':
    pygame.init()
    game_on = 1
    loop()