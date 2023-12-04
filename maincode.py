qu_button_x, qu_button_y=(305+150,296+100)

# 클릭 말풍선 이미지 
click_image_path="D:\python응용\pygame/def start_screen()\click.png"
click_image=pygame.image.load(click_image_path)
cilck_width,click_height=click_image.get_size()

st_click_button_x,st_click_button_y=(1000,1000)
qu_click_button_x,qu_click_button_y=(1000,1000)

# 시작화면 함수
def start_screen():
    x=0 #화면 루프 변수 
    
    background_image = pygame.image.load("D:/python응용/pygame/def start_screen()/start_back_ground.png")  # 실제 이미지 파일 경로로 대체해
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0)) 
    # 버튼을 그림
    screen.blit(start_button_image, (st_button_x, st_button_y))
    screen.blit(question_button_image, (qu_button_x, qu_button_y))
    screen.blit(title_image,(title_x,title_y))
    start_button_rect=draw_button("시작",(305-65,437))
    question_button_rect=draw_button("설명하기",(550,437))

    pygame.display.update() # 화면 업뎃

    while True:
        for event in pygame.event.get(): # 이벤트에 있는 모든 이벤트 가져옴
            if event.type == pygame.QUIT: # 이벤트 타입이 윈도우 닫기 이벤트인지 확인
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                # 이벤트 타입이 마우스버튼을 누르기 이벤트인지 확인 
                if start_button_rect.collidepoint(event.pos):
                    return "story" 
                if question_button_rect.collidepoint(event.pos):
                    return "next_question"
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_x,mouse_y):
                screen.blit(click_image,(st_click_button_x-725,st_click_button_y-730+100))
        pygame.display.update()

def story_screen():
    story1_image = pygame.image.load("D:\python응용\pygame\story\story_1.png")  
    story1_image = pygame.transform.scale(story1_image, (width, height))
    screen.blit(story1_image, (0, 0))

    next_button_path="D:/python응용/pygame/def start_screen()/button_start.png"
    next_story_button=pygame.image.load(next_button_path)
    button_width,button_height=next_story_button.get_size()
    nx_button_x, nx_button_y=(400,400)

    next_button_rect=draw_button("next",(420,420))

    story2_image = pygame.image.load("D:\python응용\pygame\story\story_1.png")  
    story2_image = pygame.transform.scale(story2_image, (width, height))
    
    screen.blit (next_story_button,(nx_button_x,nx_button_y))
    
    mouse_x,mouse_y=pygame.mouse.get_pos()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                # 이벤트 타입이 마우스버튼을 누르기 이벤트인지 확인 
                if next_button_rect.collidepoint(event.pos):
                    screen.blit(story2_image, (0, 0))

                    return "next_story"

# 시작 버튼 다음 화면
# 시작 배경음악 있어야 하나..?
# 시작 누르고 다음화면으로 넘어가서 음악고르는 화면

def next_start_screen():
# 게임 선택 배경화면 
    background_path = pygame.image.load("D:/python응용/pygame/def next_start_screen()/next_back_grond.jpg")  # 실제 이미지 파일 경로로 대체해
    background_image = pygame.transform.scale(background_path, (width, height))
    screen.blit(background_image, (0, 0))

    return_button_rect=draw_button("<< back",(125,45))


    pygame.draw.rect(screen,(225,225,255),[50,110,320,270])

    music_albom_path="D:/python응용/pygame/def next_start_screen()/music_albom_picture.png"
    music_albom_image=pygame.image.load(music_albom_path)
    music_albom_width,music_albom_height=music_albom_image.get_size()
    music_albom_x, music_albom_y=(60,120)

    music_choice=draw_button("music",(203,90))
    stage1_name=draw_button("<stage1>",(203,410))
    stage1_music=draw_button("-The Way to You-",(203,450))

    game_start_button_path = "D:/python응용/pygame/def next_start_screen()/button_question_copy.png"
    game_start_button = pygame.image.load(game_start_button_path)
    game_start_button_width, game_start_button_height = game_start_button.get_size()
    screen.blit(game_start_button, (123, 480))

    game_start_button_rect=draw_button("start!",(203,515))

    screen.blit(music_albom_image, (music_albom_x,music_albom_y))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if return_button_rect.collidepoint(event.pos):
                    return "start"
        mouse_x,mouse_y=pygame.mouse.get_pos()

# 설명버튼 다음화면
# 설명에 들어가야할 내용
# 뒤로가기 키 설정 
# 일시정지 키 설정 
# 키를 이용하여 캐릭터를 어떻게 움직일 수 있는지 설명
def next_question_screen():
    screen.fill(white)

    text=font.render("설명",True,(0,0,0))
    text_rect=text.get_rect(center=(width// 2,height//2))
    screen.blit(text,text_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()


# 버튼그림,rect반환시킴

def draw_button(text, position):
    button_image = font.render(text, True, (0, 0, 0))
    button_rect = button_image.get_rect(center=position)
    screen.blit(button_image, button_rect)
    return button_rect # 꼭 반환시켜야함

current_state = start_screen()
next_state= next_start_screen() # 시작화면 표시
story_state=story_screen() 

running = True # True로 초기화
while running:
    for event in pygame.event.get(): # 사용자의 입력을 감지하고 동작처리
        if event.type == pygame.QUIT: # quit를 감지>> running을 False로 설정
            running = False

    if current_state == "story":
        story_screen()
        if story_state =="next_story":
            next_start_screen()
    if current_state=="next_question":
        next_question_screen()

    if next_state=="start":
        start_screen()

    mouse_x,mouse_y=pygame.mouse.get_pos()    
    pygame.display.flip()

pygame.quit()
sys.exit()

