import pygame, sys
from Button import Button
import questions
from pygame import mixer

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz game to improve English skills")

# Bgm
mixer.music.load("sounds/BGM.wav")
mixer.music.play(-1)

#load images
icon = pygame.image.load("Pictures/icon.png")
pygame.display.set_icon(icon)
BG = pygame.image.load("Pictures/bg.jpg")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = questions.loop()
       
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#FFF9B8")

        OPTIONS_TEXT = get_font(12).render("1.'He' the subject pronoun he is needed to refer to Mr.kim", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(350, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_TEXT2 = get_font(12).render("2. 'Require', the simple present tense of the verb, is needed", True, "Black")
        OPTIONS_RECT2 = OPTIONS_TEXT.get_rect(center=(350, 65))
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        OPTIONS_TEXT3 = get_font(12).render("3. 'Notify', A verb meaning tell or inform should be used.", True, "Black")
        OPTIONS_RECT3 = OPTIONS_TEXT.get_rect(center=(350, 80))
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)
        OPTIONS_TEXT4 = get_font(12).render("4. 'For', for is used to introduce that a design is aimed at biker", True, "Black")
        OPTIONS_RECT4 = OPTIONS_TEXT.get_rect(center=(350, 95))
        SCREEN.blit(OPTIONS_TEXT4, OPTIONS_RECT4)
        OPTIONS_TEXT5 = get_font(12).render("5. 'included', Included in means part of, so it is correct here", True, "Black")
        OPTIONS_RECT5 = OPTIONS_TEXT.get_rect(center=(350, 110))
        SCREEN.blit(OPTIONS_TEXT5, OPTIONS_RECT5)
        OPTIONS_TEXT6 = get_font(12).render("6. 'celebration', noun to use with holiday which can be scheduled", True, "Black")
        OPTIONS_RECT6 = OPTIONS_TEXT.get_rect(center=(350, 125))
        SCREEN.blit(OPTIONS_TEXT6, OPTIONS_RECT6)
        OPTIONS_TEXT7 = get_font(12).render("7. 'Yet', used with most inventive stage to mean until now", True, "Black")
        OPTIONS_RECT7 = OPTIONS_TEXT.get_rect(center=(350, 140))
        SCREEN.blit(OPTIONS_TEXT7, OPTIONS_RECT7)
        OPTIONS_TEXT8 = get_font(12).render("8. 'Account', is correct with for. means represent here", True, "Black")
        OPTIONS_RECT8 = OPTIONS_TEXT.get_rect(center=(350, 155))
        SCREEN.blit(OPTIONS_TEXT8, OPTIONS_RECT8)
        OPTIONS_TEXT9 = get_font(12).render("9.'Your', is used to mean the report belonging to you", True, "Black")
        OPTIONS_RECT9 = OPTIONS_TEXT.get_rect(center=(350, 170))
        SCREEN.blit(OPTIONS_TEXT9, OPTIONS_RECT9)
        OPTIONS_TEXT10 = get_font(12).render("10.'expand', meaning make bigger, someting a firm may do", True, "Black")
        OPTIONS_RECT10 = OPTIONS_TEXT.get_rect(center=(350, 185))
        SCREEN.blit(OPTIONS_TEXT10, OPTIONS_RECT10)
        OPTIONS_TEXT11 = get_font(12).render("11.'or', We use the conjunction 'or' to link two or more thing", True, "Black")
        OPTIONS_RECT11 = OPTIONS_TEXT.get_rect(center=(350, 200))
        SCREEN.blit(OPTIONS_TEXT11, OPTIONS_RECT11)
        OPTIONS_TEXT12 = get_font(12).render("12.'direct', person who says exactly what they mean", True, "Black")
        OPTIONS_RECT12 = OPTIONS_TEXT.get_rect(center=(350, 215))
        SCREEN.blit(OPTIONS_TEXT12, OPTIONS_RECT12)
        OPTIONS_TEXT13 = get_font(12).render("13.'election', noun is needed with the definite article 'The' ", True, "Black")
        OPTIONS_RECT13 = OPTIONS_TEXT.get_rect(center=(350, 230))
        SCREEN.blit(OPTIONS_TEXT13, OPTIONS_RECT13)
        OPTIONS_TEXT14 = get_font(12).render("14.'typically', means 'generally' or 'usually'", True, "Black")
        OPTIONS_RECT14 = OPTIONS_TEXT.get_rect(center=(350, 245))
        SCREEN.blit(OPTIONS_TEXT14, OPTIONS_RECT14)
        OPTIONS_TEXT15 = get_font(12).render("15.'responsibly', An adverb is needed after the verb", True, "Black")
        OPTIONS_RECT15 = OPTIONS_TEXT.get_rect(center=(350, 260))
        SCREEN.blit(OPTIONS_TEXT15, OPTIONS_RECT15)
        OPTIONS_TEXT16 = get_font(12).render("16.'has transferred',the present perfect tense is needed", True, "Black")
        OPTIONS_RECT16 = OPTIONS_TEXT.get_rect(center=(350, 275))
        SCREEN.blit(OPTIONS_TEXT16, OPTIONS_RECT16)
        OPTIONS_TEXT17 = get_font(12).render("17.'trend',used for a change in the type of ingredients", True, "Black")
        OPTIONS_RECT17 = OPTIONS_TEXT.get_rect(center=(350, 290))
        SCREEN.blit(OPTIONS_TEXT17, OPTIONS_RECT17)
        OPTIONS_TEXT18 = get_font(12).render("18.'simple',An adjective to describe melodies is needed", True, "Black")
        OPTIONS_RECT18 = OPTIONS_TEXT.get_rect(center=(350, 305))
        SCREEN.blit(OPTIONS_TEXT18, OPTIONS_RECT18)
        OPTIONS_TEXT19 = get_font(12).render("19.'significant', Meaning 'important' is an adjective", True, "Black")
        OPTIONS_RECT19 = OPTIONS_TEXT.get_rect(center=(350, 320))
        SCREEN.blit(OPTIONS_TEXT19, OPTIONS_RECT19)
        OPTIONS_TEXT20 = get_font(12).render("20.'warm', is used to describe the noun 'welcome'.", True, "Black")
        OPTIONS_RECT20 = OPTIONS_TEXT.get_rect(center=(350, 335))
        SCREEN.blit(OPTIONS_TEXT20, OPTIONS_RECT20)
        OPTIONS_TEXT21 = get_font(12).render("21.'assist',The verb infinitive 'assist' is used with to.", True, "Black")
        OPTIONS_RECT21 = OPTIONS_TEXT.get_rect(center=(350, 350))
        SCREEN.blit(OPTIONS_TEXT21, OPTIONS_RECT21)
        OPTIONS_TEXT22 = get_font(12).render("22.'Negotiating', completes the present continusous tense", True, "Black")
        OPTIONS_RECT22 = OPTIONS_TEXT.get_rect(center=(350, 365))
        SCREEN.blit(OPTIONS_TEXT22, OPTIONS_RECT22)
        OPTIONS_TEXT23 = get_font(12).render("23.'linking', can be used to describe what the bridge does", True, "Black")
        OPTIONS_RECT23 = OPTIONS_TEXT.get_rect(center=(350, 380))
        SCREEN.blit(OPTIONS_TEXT23, OPTIONS_RECT23)
        OPTIONS_TEXT24 = get_font(11).render("24.'phenomenal','very great' can be used to describe the noun 'success'", True, "Black")
        OPTIONS_RECT24 = OPTIONS_TEXT.get_rect(center=(350, 395))
        SCREEN.blit(OPTIONS_TEXT24, OPTIONS_RECT24)
        OPTIONS_TEXT25 = get_font(12).render("25.'reservations', A travel agency makes travel reservations", True, "Black")
        OPTIONS_RECT25 = OPTIONS_TEXT.get_rect(center=(350, 410))
        SCREEN.blit(OPTIONS_TEXT25, OPTIONS_RECT25)
        OPTIONS_TEXT26 = get_font(12).render("26.'for', We use the time preposition 'for' with a length of time", True, "Black")
        OPTIONS_RECT26 = OPTIONS_TEXT.get_rect(center=(350, 425))
        SCREEN.blit(OPTIONS_TEXT26, OPTIONS_RECT26)
        OPTIONS_TEXT27 = get_font(12).render("27.'representative', 'Representative of' means an example of", True, "Black")
        OPTIONS_RECT27 = OPTIONS_TEXT.get_rect(center=(350, 440))
        SCREEN.blit(OPTIONS_TEXT27, OPTIONS_RECT27)
        OPTIONS_TEXT28 = get_font(12).render("28.'from', used here to talk about the origin of the desserts", True, "Black")
        OPTIONS_RECT28 = OPTIONS_TEXT.get_rect(center=(350, 455))
        SCREEN.blit(OPTIONS_TEXT28, OPTIONS_RECT28)
        OPTIONS_TEXT29 = get_font(12).render("29.'Those', those should be used here to mean 'any' people.", True, "Black")
        OPTIONS_RECT29 = OPTIONS_TEXT.get_rect(center=(350, 470))
        SCREEN.blit(OPTIONS_TEXT29, OPTIONS_RECT29)
        OPTIONS_TEXT30 = get_font(12).render("30.'Delighted',complete the clause at the beginning of the sentence", True, "Black")
        OPTIONS_RECT30 = OPTIONS_TEXT.get_rect(center=(350, 485))
        SCREEN.blit(OPTIONS_TEXT30, OPTIONS_RECT30)
        OPTIONS_TEXT31 = get_font(12).render("31.'proposal', is the correct noun to use with marketing", True, "Black")
        OPTIONS_RECT31 = OPTIONS_TEXT.get_rect(center=(350, 500))
        SCREEN.blit(OPTIONS_TEXT31, OPTIONS_RECT31)
        OPTIONS_TEXT32 = get_font(12).render("32.'sold', the past participle of sell", True, "Black")
        OPTIONS_RECT32 = OPTIONS_TEXT.get_rect(center=(350, 515))
        SCREEN.blit(OPTIONS_TEXT32, OPTIONS_RECT32)
        OPTIONS_TEXT33 = get_font(12).render("33.'worse', should be used to complete the comparison", True, "Black")
        OPTIONS_RECT33 = OPTIONS_TEXT.get_rect(center=(350, 530))
        SCREEN.blit(OPTIONS_TEXT33, OPTIONS_RECT33)
        OPTIONS_TEXT34 = get_font(12).render("34.'correctly', talk about the manner of applying the products", True, "Black")
        OPTIONS_RECT34 = OPTIONS_TEXT.get_rect(center=(350, 545))
        SCREEN.blit(OPTIONS_TEXT34, OPTIONS_RECT34)
        OPTIONS_TEXT35 = get_font(12).render("35.'buy', following 'expect' should be a verb infinitive with 'to'", True, "Black")
        OPTIONS_RECT35 = OPTIONS_TEXT.get_rect(center=(350, 560))
        SCREEN.blit(OPTIONS_TEXT35, OPTIONS_RECT35)

        OPTIONS_BACK = Button(image=None, pos=(35, 25), 
                            text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        OPTIONS_NEXT = Button(image=None, pos=(750, 575),
                            text_input="NEXT", font=get_font(15), base_color="Black", hovering_color="Green")

        OPTIONS_NEXT.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_NEXT.update(SCREEN)                    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_NEXT.checkForInput(OPTIONS_MOUSE_POS):
                    options2()


        pygame.display.update()

def options2():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#FFF9B8")
        OPTIONS_TEXT36 = get_font(12).render("36.'discretion', A noun is needed after 'her' ", True, "Black")
        OPTIONS_RECT36 = OPTIONS_TEXT36.get_rect(center=(280, 50))
        SCREEN.blit(OPTIONS_TEXT36, OPTIONS_RECT36)
        OPTIONS_TEXT37 = get_font(12).render("37.'transform', means to change. object followed by into", True, "Black")
        OPTIONS_RECT37 = OPTIONS_TEXT36.get_rect(center=(280, 65))
        SCREEN.blit(OPTIONS_TEXT37, OPTIONS_RECT37)
        OPTIONS_TEXT38 = get_font(12).render("38.'Whether', should be used with or as a double conjunction ", True, "Black")
        OPTIONS_RECT38 = OPTIONS_TEXT36.get_rect(center=(280, 80))
        SCREEN.blit(OPTIONS_TEXT38, OPTIONS_RECT38)
        OPTIONS_TEXT39 = get_font(12).render("39.The adverb 'ever' should be used, meaning 'at any other time'.  ", True, "Black")
        OPTIONS_RECT39 = OPTIONS_TEXT36.get_rect(center=(280, 95))
        SCREEN.blit(OPTIONS_TEXT39, OPTIONS_RECT39)
        OPTIONS_TEXT40 = get_font(12).render("40.'relatively', means 'fairly' is suitable here. modify 'small' ", True, "Black")
        OPTIONS_RECT40 = OPTIONS_TEXT36.get_rect(center=(280, 110))
        SCREEN.blit(OPTIONS_TEXT40, OPTIONS_RECT40)
        OPTIONS_TEXT41 = get_font(12).render("41.'significant',can be used to describe the growth. It means huge", True, "Black")
        OPTIONS_RECT41 = OPTIONS_TEXT36.get_rect(center=(280, 125))
        SCREEN.blit(OPTIONS_TEXT41, OPTIONS_RECT41)
        OPTIONS_TEXT42 = get_font(12).render("42.'recognizably', can be used to modify the adjective 'different'", True, "Black")
        OPTIONS_RECT42 = OPTIONS_TEXT36.get_rect(center=(280, 140))
        SCREEN.blit(OPTIONS_TEXT42, OPTIONS_RECT42)
        OPTIONS_TEXT43 = get_font(12).render("43.'for', used with 'recommend' to indicate the purpose", True, "Black")
        OPTIONS_RECT43 = OPTIONS_TEXT36.get_rect(center=(280, 155))
        SCREEN.blit(OPTIONS_TEXT43, OPTIONS_RECT43)
        OPTIONS_TEXT44 = get_font(12).render("44.'promptly',mean the reports should be delivered 'punctually' ", True, "Black")
        OPTIONS_RECT44 = OPTIONS_TEXT36.get_rect(center=(280, 170))
        SCREEN.blit(OPTIONS_TEXT44, OPTIONS_RECT44)
        OPTIONS_TEXT45 = get_font(12).render("45.'concluded',to bring to an end especially in a particular way", True, "Black")
        OPTIONS_RECT45 = OPTIONS_TEXT36.get_rect(center=(280, 185))
        SCREEN.blit(OPTIONS_TEXT45, OPTIONS_RECT45)
        OPTIONS_TEXT46 = get_font(12).render("46.'Among', used with the plural noun achievements", True, "Black")
        OPTIONS_RECT46 = OPTIONS_TEXT36.get_rect(center=(280, 200))
        SCREEN.blit(OPTIONS_TEXT46, OPTIONS_RECT46)
        OPTIONS_TEXT47 = get_font(12).render("47.'foolish',adjective which can describe a notion should be used", True, "Black")
        OPTIONS_RECT47 = OPTIONS_TEXT36.get_rect(center=(280, 215))
        SCREEN.blit(OPTIONS_TEXT47, OPTIONS_RECT47)
        OPTIONS_TEXT48 = get_font(12).render("48.'Conducted', the past participle of the verb conduct", True, "Black")
        OPTIONS_RECT48 = OPTIONS_TEXT36.get_rect(center=(280, 230))
        SCREEN.blit(OPTIONS_TEXT48, OPTIONS_RECT48)
        OPTIONS_TEXT49 = get_font(12).render("49.'so', as a subordinating conjunction", True, "Black")
        OPTIONS_RECT49 = OPTIONS_TEXT36.get_rect(center=(280, 245))
        SCREEN.blit(OPTIONS_TEXT49, OPTIONS_RECT49)
        OPTIONS_TEXT50 = get_font(12).render("50.'well', The adverb 'well' can be used to modify 'attended'", True, "Black")
        OPTIONS_RECT50 = OPTIONS_TEXT36.get_rect(center=(280, 260))
        SCREEN.blit(OPTIONS_TEXT50, OPTIONS_RECT50)
        OPTIONS_TEXT51 = get_font(12).render("51.'is', ", True, "Black")
        OPTIONS_RECT51 = OPTIONS_TEXT36.get_rect(center=(280, 275))
        SCREEN.blit(OPTIONS_TEXT51, OPTIONS_RECT51)
        OPTIONS_TEXT52 = get_font(12).render("52.'refreshments', ", True, "Black")
        OPTIONS_RECT52 = OPTIONS_TEXT36.get_rect(center=(280, 290))
        SCREEN.blit(OPTIONS_TEXT52, OPTIONS_RECT52)
        OPTIONS_TEXT53 = get_font(12).render("53.'sending', ", True, "Black")
        OPTIONS_RECT53 = OPTIONS_TEXT36.get_rect(center=(280, 305))
        SCREEN.blit(OPTIONS_TEXT53, OPTIONS_RECT53)
        OPTIONS_TEXT54 = get_font(12).render("54.'interfere', ", True, "Black")
        OPTIONS_RECT54 = OPTIONS_TEXT36.get_rect(center=(280, 320))
        SCREEN.blit(OPTIONS_TEXT54, OPTIONS_RECT54)
        OPTIONS_TEXT55 = get_font(12).render("55.'her', ", True, "Black")
        OPTIONS_RECT55 = OPTIONS_TEXT36.get_rect(center=(280, 335))
        SCREEN.blit(OPTIONS_TEXT55, OPTIONS_RECT55)
        OPTIONS_TEXT56 = get_font(12).render("56.'be tested', ", True, "Black")
        OPTIONS_RECT56 = OPTIONS_TEXT36.get_rect(center=(280, 350))
        SCREEN.blit(OPTIONS_TEXT56, OPTIONS_RECT56)
        OPTIONS_TEXT57 = get_font(12).render("57.'firmly', ", True, "Black")
        OPTIONS_RECT57 = OPTIONS_TEXT36.get_rect(center=(280, 365))
        SCREEN.blit(OPTIONS_TEXT57, OPTIONS_RECT57)
        OPTIONS_TEXT58 = get_font(12).render("58.'unless', ", True, "Black")
        OPTIONS_RECT58 = OPTIONS_TEXT36.get_rect(center=(280, 380))
        SCREEN.blit(OPTIONS_TEXT58, OPTIONS_RECT58)
        OPTIONS_TEXT59 = get_font(12).render("59.'substantially', ", True, "Black")
        OPTIONS_RECT59 = OPTIONS_TEXT36.get_rect(center=(280, 395))
        SCREEN.blit(OPTIONS_TEXT59, OPTIONS_RECT59)
        OPTIONS_TEXT60 = get_font(12).render("60.'Although', ", True, "Black")
        OPTIONS_RECT60 = OPTIONS_TEXT36.get_rect(center=(280, 410))
        SCREEN.blit(OPTIONS_TEXT60, OPTIONS_RECT60)
        

        OPTIONS_BACK = Button(image=None, pos=(35, 25), 
                            text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options()
    
        pygame.display.update()



#Main game loop
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(45).render("TOEIC QUIZ GAME", True, "Orange")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 400), 
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 270), 
                            text_input="Answer Sheet", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 530), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

   
   

