import pygame, sys
from Button import Button
import Questions
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

        PLAY_TEXT = Questions.loop()


       
    
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
        OPTIONS_TEXT51 = get_font(12).render("51.'is', used with singular noun, 'is on'", True, "Black")
        OPTIONS_RECT51 = OPTIONS_TEXT36.get_rect(center=(280, 275))
        SCREEN.blit(OPTIONS_TEXT51, OPTIONS_RECT51)
        OPTIONS_TEXT52 = get_font(12).render("52.'refreshments', are drinks and small amounts of food", True, "Black")
        OPTIONS_RECT52 = OPTIONS_TEXT36.get_rect(center=(280, 290))
        SCREEN.blit(OPTIONS_TEXT52, OPTIONS_RECT52)
        OPTIONS_TEXT53 = get_font(12).render("53.'sending', past tense, past participle sent", True, "Black")
        OPTIONS_RECT53 = OPTIONS_TEXT36.get_rect(center=(280, 305))
        SCREEN.blit(OPTIONS_TEXT53, OPTIONS_RECT53)
        OPTIONS_TEXT54 = get_font(12).render("54.'interfere', mean they get involved in it", True, "Black")
        OPTIONS_RECT54 = OPTIONS_TEXT36.get_rect(center=(280, 320))
        SCREEN.blit(OPTIONS_TEXT54, OPTIONS_RECT54)
        OPTIONS_TEXT55 = get_font(12).render("55.'her', is a third person singular pronoun.", True, "Black")
        OPTIONS_RECT55 = OPTIONS_TEXT36.get_rect(center=(280, 335))
        SCREEN.blit(OPTIONS_TEXT55, OPTIONS_RECT55)
        OPTIONS_TEXT56 = get_font(12).render("56.'be tested', past tense, When you test something, you try it ", True, "Black")
        OPTIONS_RECT56 = OPTIONS_TEXT36.get_rect(center=(280, 350))
        SCREEN.blit(OPTIONS_TEXT56, OPTIONS_RECT56)
        OPTIONS_TEXT57 = get_font(12).render("57.'firmly', adverb, If something is firm, it does not shake", True, "Black")
        OPTIONS_RECT57 = OPTIONS_TEXT36.get_rect(center=(280, 365))
        SCREEN.blit(OPTIONS_TEXT57, OPTIONS_RECT57)
        OPTIONS_TEXT58 = get_font(12).render("58.'unless', except under the circumstances that", True, "Black")
        OPTIONS_RECT58 = OPTIONS_TEXT36.get_rect(center=(280, 380))
        SCREEN.blit(OPTIONS_TEXT58, OPTIONS_RECT58)
        OPTIONS_TEXT59 = get_font(12).render("59.'substantially', adverb, mean a lot or is very different. ", True, "Black")
        OPTIONS_RECT59 = OPTIONS_TEXT36.get_rect(center=(280, 395))
        SCREEN.blit(OPTIONS_TEXT59, OPTIONS_RECT59)
        OPTIONS_TEXT60 = get_font(12).render("60.'Although', despite the fact that; even though", True, "Black")
        OPTIONS_RECT60 = OPTIONS_TEXT36.get_rect(center=(280, 410))
        SCREEN.blit(OPTIONS_TEXT60, OPTIONS_RECT60)
        OPTIONS_TEXT61 = get_font(12).render("61.'shrinking',present participle, it becomes smaller", True, "Black")
        OPTIONS_RECT61 = OPTIONS_TEXT36.get_rect(center=(280, 425))
        SCREEN.blit(OPTIONS_TEXT61, OPTIONS_RECT61)
        OPTIONS_TEXT62 = get_font(12).render("62.'terminate', When you terminate something it ends completely.", True, "Black")
        OPTIONS_RECT62 = OPTIONS_TEXT36.get_rect(center=(280, 440))
        SCREEN.blit(OPTIONS_TEXT62, OPTIONS_RECT62)
        OPTIONS_TEXT63 = get_font(12).render("63.'stamped',A stamped envelope or package has a stamp stuck on it.", True, "Black")
        OPTIONS_RECT63 = OPTIONS_TEXT36.get_rect(center=(280, 455))
        SCREEN.blit(OPTIONS_TEXT63, OPTIONS_RECT63)
        OPTIONS_TEXT64 = get_font(12).render("64.'Other',You use other to refer to an additional thing or person", True, "Black")
        OPTIONS_RECT64 = OPTIONS_TEXT36.get_rect(center=(280, 470))
        SCREEN.blit(OPTIONS_TEXT64, OPTIONS_RECT64)
        OPTIONS_TEXT65 = get_font(12).render("65.'calculated', deliberately planned or intended", True, "Black")
        OPTIONS_RECT65 = OPTIONS_TEXT36.get_rect(center=(280, 485))
        SCREEN.blit(OPTIONS_TEXT65, OPTIONS_RECT65)
        OPTIONS_TEXT66 = get_font(12).render("66.'opposition', a person or group antagonistic in aims to another", True, "Black")
        OPTIONS_RECT66 = OPTIONS_TEXT36.get_rect(center=(280, 500))
        SCREEN.blit(OPTIONS_TEXT66, OPTIONS_RECT66)
        OPTIONS_TEXT67 = get_font(12).render("67.'distinct', easily sensed or understood; clear; precise", True, "Black")
        OPTIONS_RECT67 = OPTIONS_TEXT36.get_rect(center=(280, 515))
        SCREEN.blit(OPTIONS_TEXT67, OPTIONS_RECT67)
        OPTIONS_TEXT68 = get_font(12).render("68.'were', is the plural of the past tense of 'be'", True, "Black")
        OPTIONS_RECT68 = OPTIONS_TEXT36.get_rect(center=(280, 530))
        SCREEN.blit(OPTIONS_TEXT68, OPTIONS_RECT68)
        OPTIONS_TEXT69 = get_font(12).render("69.'throughout', through the whole of some specified period or area", True, "Black")
        OPTIONS_RECT69 = OPTIONS_TEXT36.get_rect(center=(280, 545))
        SCREEN.blit(OPTIONS_TEXT69, OPTIONS_RECT69)
        OPTIONS_TEXT70 = get_font(12).render("70.'their', of, belonging to, or associated in some way with them", True, "Black")
        OPTIONS_RECT70 = OPTIONS_TEXT36.get_rect(center=(280, 560))
        SCREEN.blit(OPTIONS_TEXT70, OPTIONS_RECT70)
        
        

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
                    options()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_NEXT.checkForInput(OPTIONS_MOUSE_POS):
                    options3()        
    
        pygame.display.update()

def options3():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#FFF9B8")
        OPTIONS_TEXT71 = get_font(12).render("71.'athletic', means relating to athletes and athletics.", True, "Black")
        OPTIONS_RECT71 = OPTIONS_TEXT71.get_rect(center=(340, 50))
        SCREEN.blit(OPTIONS_TEXT71, OPTIONS_RECT71)
        OPTIONS_TEXT72 = get_font(12).render("72.'being built', is the past tense and past participle of build.", True, "Black")
        OPTIONS_RECT72 = OPTIONS_TEXT71.get_rect(center=(340, 65))
        SCREEN.blit(OPTIONS_TEXT72, OPTIONS_RECT72)
        OPTIONS_TEXT73 = get_font(12).render("73.'strategically',adverb,relating to the most important aspects.", True, "Black")
        OPTIONS_RECT73 = OPTIONS_TEXT71.get_rect(center=(340, 80))
        SCREEN.blit(OPTIONS_TEXT73, OPTIONS_RECT73)
        OPTIONS_TEXT74 = get_font(12).render("74.'attractive', arousing interest in interest rate", True, "Black")
        OPTIONS_RECT74 = OPTIONS_TEXT71.get_rect(center=(340, 95))
        SCREEN.blit(OPTIONS_TEXT74, OPTIONS_RECT74)
        OPTIONS_TEXT75 = get_font(12).render("75.'take over', adverb, to assume the control or management of", True, "Black")
        OPTIONS_RECT75 = OPTIONS_TEXT71.get_rect(center=(340, 110))
        SCREEN.blit(OPTIONS_TEXT75, OPTIONS_RECT75)
        OPTIONS_TEXT76 = get_font(12).render("76.'costly', of great price or value; expensive", True, "Black")
        OPTIONS_RECT76 = OPTIONS_TEXT71.get_rect(center=(340, 125))
        SCREEN.blit(OPTIONS_TEXT76, OPTIONS_RECT76)
        OPTIONS_TEXT77 = get_font(12).render("77.'had begun', is the past participle of begin.", True, "Black")
        OPTIONS_RECT77 = OPTIONS_TEXT71.get_rect(center=(340, 140))
        SCREEN.blit(OPTIONS_TEXT77, OPTIONS_RECT77)
        OPTIONS_TEXT78 = get_font(12).render("78.'frequently',adverb, at frequent or brief intervals; often ", True, "Black")
        OPTIONS_RECT78 = OPTIONS_TEXT71.get_rect(center=(340, 155))
        SCREEN.blit(OPTIONS_TEXT78, OPTIONS_RECT78)
        OPTIONS_TEXT79 = get_font(12).render("79.'Because of', Phrase, by reason of; due to", True, "Black")
        OPTIONS_RECT79 = OPTIONS_TEXT71.get_rect(center=(340, 170))
        SCREEN.blit(OPTIONS_TEXT79, OPTIONS_RECT79)
        OPTIONS_TEXT80 = get_font(12).render("80.'who', used to introduce relative clauses referring to humans.", True, "Black")
        OPTIONS_RECT80 = OPTIONS_TEXT71.get_rect(center=(340, 185))
        SCREEN.blit(OPTIONS_TEXT80, OPTIONS_RECT80)
        OPTIONS_TEXT81 = get_font(12).render("81.'either', one or the other (of two)", True, "Black")
        OPTIONS_RECT81 = OPTIONS_TEXT71.get_rect(center=(340, 200))
        SCREEN.blit(OPTIONS_TEXT81, OPTIONS_RECT81)
        OPTIONS_TEXT82 = get_font(12).render("82.'securely', free from danger, damage, etc ", True, "Black")
        OPTIONS_RECT82 = OPTIONS_TEXT71.get_rect(center=(340, 215))
        SCREEN.blit(OPTIONS_TEXT82, OPTIONS_RECT82)
        OPTIONS_TEXT83 = get_font(12).render("83.'finally', after a long delay; at last; eventually ", True, "Black")
        OPTIONS_RECT83 = OPTIONS_TEXT71.get_rect(center=(340, 230))
        SCREEN.blit(OPTIONS_TEXT83, OPTIONS_RECT83)
        OPTIONS_TEXT84 = get_font(12).render("84.'be submitted',past tense, to refer (something to someone) ", True, "Black")
        OPTIONS_RECT84 = OPTIONS_TEXT71.get_rect(center=(340, 245))
        SCREEN.blit(OPTIONS_TEXT84, OPTIONS_RECT84)
        OPTIONS_TEXT85 = get_font(12).render("85.'due to', caused by; resulting from ", True, "Black")
        OPTIONS_RECT85 = OPTIONS_TEXT71.get_rect(center=(340, 260))
        SCREEN.blit(OPTIONS_TEXT85, OPTIONS_RECT85)
        OPTIONS_TEXT86 = get_font(12).render("86.'negotiate',to work or talk with others to achieve an agreement", True, "Black")
        OPTIONS_RECT86 = OPTIONS_TEXT71.get_rect(center=(340, 275))
        SCREEN.blit(OPTIONS_TEXT86, OPTIONS_RECT86)
        OPTIONS_TEXT87 = get_font(12).render("87.'Both', the two; two considered together ", True, "Black")
        OPTIONS_RECT87 = OPTIONS_TEXT71.get_rect(center=(340, 290))
        SCREEN.blit(OPTIONS_TEXT87, OPTIONS_RECT87)
        OPTIONS_TEXT88 = get_font(12).render("88.'highest',superlative, being at its peak", True, "Black")
        OPTIONS_RECT88 = OPTIONS_TEXT71.get_rect(center=(340, 305))
        SCREEN.blit(OPTIONS_TEXT88, OPTIONS_RECT88)
        OPTIONS_TEXT89 = get_font(12).render("89.'will be published',to produce and issue for distribution", True, "Black")
        OPTIONS_RECT89 = OPTIONS_TEXT71.get_rect(center=(340, 320))
        SCREEN.blit(OPTIONS_TEXT89, OPTIONS_RECT89)
        OPTIONS_TEXT90 = get_font(12).render("90.'permitted',Past tense, to allow the possibility(of) ", True, "Black")
        OPTIONS_RECT90 = OPTIONS_TEXT71.get_rect(center=(340, 335))
        SCREEN.blit(OPTIONS_TEXT90, OPTIONS_RECT90)
        OPTIONS_TEXT91 = get_font(12).render("91.'demolish', to tear down or break up (buildings, etc) ", True, "Black")
        OPTIONS_RECT91 = OPTIONS_TEXT71.get_rect(center=(340, 350))
        SCREEN.blit(OPTIONS_TEXT91, OPTIONS_RECT91)
        OPTIONS_TEXT92 = get_font(12).render("92.'agreeable', to one's liking ", True, "Black")
        OPTIONS_RECT92 = OPTIONS_TEXT71.get_rect(center=(340, 365))
        SCREEN.blit(OPTIONS_TEXT92, OPTIONS_RECT92)
        OPTIONS_TEXT93 = get_font(12).render("93.'highest',superlative, being at its peak ", True, "Black")
        OPTIONS_RECT93 = OPTIONS_TEXT71.get_rect(center=(340, 380))
        SCREEN.blit(OPTIONS_TEXT93, OPTIONS_RECT93)
        OPTIONS_TEXT94 = get_font(12).render("94.'that',refer back to an idea expressed in a previous sentence", True, "Black")
        OPTIONS_RECT94 = OPTIONS_TEXT71.get_rect(center=(340, 395))
        SCREEN.blit(OPTIONS_TEXT94, OPTIONS_RECT94)
        OPTIONS_TEXT95 = get_font(12).render("95.'vacate', to give up the occupancy of a place ", True, "Black")
        OPTIONS_RECT95 = OPTIONS_TEXT71.get_rect(center=(340, 410))
        SCREEN.blit(OPTIONS_TEXT95, OPTIONS_RECT95)
        OPTIONS_TEXT96 = get_font(12).render("96.'immensely', to emphasize the degree of a quality, feeling", True, "Black")
        OPTIONS_RECT96 = OPTIONS_TEXT71.get_rect(center=(340, 425))
        SCREEN.blit(OPTIONS_TEXT96, OPTIONS_RECT96)
        OPTIONS_TEXT97 = get_font(12).render("97.'appearance', the act or an instance of appearing ", True, "Black")
        OPTIONS_RECT97 = OPTIONS_TEXT71.get_rect(center=(340, 440))
        SCREEN.blit(OPTIONS_TEXT97, OPTIONS_RECT97)
        OPTIONS_TEXT98 = get_font(12).render("98.'at', used to indicate location or position ", True, "Black")
        OPTIONS_RECT98 = OPTIONS_TEXT71.get_rect(center=(340, 455))
        SCREEN.blit(OPTIONS_TEXT98, OPTIONS_RECT98)
        OPTIONS_TEXT99 = get_font(12).render("99.'By',Preposition, not later than; before ", True, "Black")
        OPTIONS_RECT99 = OPTIONS_TEXT71.get_rect(center=(340, 470))
        SCREEN.blit(OPTIONS_TEXT99, OPTIONS_RECT99)
        OPTIONS_TEXT100 = get_font(12).render("100.'advancements', progress or improvement; furtherance ", True, "Black")
        OPTIONS_RECT100 = OPTIONS_TEXT71.get_rect(center=(340, 485))
        SCREEN.blit(OPTIONS_TEXT100, OPTIONS_RECT100)
    
        OPTIONS_BACK = Button(image=None, pos=(35, 25), 
                            text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Green")                      

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        OPTIONS_MENU = Button(image=None, pos=(750, 25), 
                            text_input="MENU", font=get_font(15), base_color="Black", hovering_color="Green")                      

        OPTIONS_MENU.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MENU.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options2()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_MENU.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()        
          
        
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

   
   

