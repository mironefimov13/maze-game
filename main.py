import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800

BLACK = (0,0,0)
WHITE = (225,225,225)
GREEN = (0,225,0)
BACKGROUND_COLOR = WHITE
LINE_COLOR = BLACK

FONT = pygame.font.SysFont("comicsans", 100, bold=True)
FONT_COLOR = GREEN

THICKNESS = 8

FPS = 150
SPEED = 1.5

DOOR_COORDS = [370,690]

coords = [352, 0]
before = ""

# WALLS
wall1 = pygame.Rect(0,0,320,THICKNESS)
wall2 = pygame.Rect(480,0,THICKNESS,160)
wall3 = pygame.Rect(0,160,320,THICKNESS)
wall4 = pygame.Rect(480,0,320,THICKNESS)
wall5 = pygame.Rect(480,160,160,THICKNESS)
wall6 = pygame.Rect(320,160,THICKNESS,160)
wall7 = pygame.Rect(320,320,320,THICKNESS)
wall8 = pygame.Rect(160,320,THICKNESS,160)
wall9 = pygame.Rect(0,480,165,THICKNESS)
wall10 = pygame.Rect(320,480,160,THICKNESS)
wall11 = pygame.Rect(320,480,THICKNESS,160)
wall12 = pygame.Rect(640,480,THICKNESS,160)
wall12 = pygame.Rect(640,480,THICKNESS,160)
wall13 = pygame.Rect(160,640,485,THICKNESS)
wall14 = pygame.Rect(480,640,THICKNESS,160)
wall15 = pygame.Rect(0,0,THICKNESS,800)
wall16 = pygame.Rect(800,0,THICKNESS,800)
wall17 = pygame.Rect(0,795,320,THICKNESS)
wall18 = pygame.Rect(480,795,320,THICKNESS)


door_mask = pygame.Rect(370, 690, 62, 75)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

player = pygame.image.load("maze_game/assets/player.png")#.convert()
door = pygame.image.load("maze_game/assets/door.png")#.convert()

def draw_map(screen):
    pygame.draw.rect(screen, LINE_COLOR, wall1)
    pygame.draw.rect(screen, LINE_COLOR, wall2)
    pygame.draw.rect(screen, LINE_COLOR, wall3)
    pygame.draw.rect(screen, LINE_COLOR, wall4)
    pygame.draw.rect(screen, LINE_COLOR, wall5)
    pygame.draw.rect(screen, LINE_COLOR, wall5)
    pygame.draw.rect(screen, LINE_COLOR, wall6)
    pygame.draw.rect(screen, LINE_COLOR, wall7)
    pygame.draw.rect(screen, LINE_COLOR, wall8)
    pygame.draw.rect(screen, LINE_COLOR, wall9)
    pygame.draw.rect(screen, LINE_COLOR, wall10)
    pygame.draw.rect(screen, LINE_COLOR, wall11)
    pygame.draw.rect(screen, LINE_COLOR, wall12)
    pygame.draw.rect(screen, LINE_COLOR, wall13)
    pygame.draw.rect(screen, LINE_COLOR, wall14)
    pygame.draw.rect(screen, LINE_COLOR, wall15)
    pygame.draw.rect(screen, LINE_COLOR, wall16)
    pygame.draw.rect(screen, LINE_COLOR, wall17)
    pygame.draw.rect(screen, LINE_COLOR, wall18)

def check_end(screen):
    if door_mask.colliderect(player_mask):
        text = FONT.render(str("YOU HAVE ESCAPED"), 1, FONT_COLOR)
        screen.blit(text, (70, 290))

def collision(screen):
    if player_mask.colliderect(wall1) or player_mask.colliderect(wall2) or player_mask.colliderect(wall3) or player_mask.colliderect(wall4) or player_mask.colliderect(wall5) or player_mask.colliderect(wall6) or player_mask.colliderect(wall7) or player_mask.colliderect(wall8) or player_mask.colliderect(wall9) or player_mask.colliderect(wall10) or player_mask.colliderect(wall11) or player_mask.colliderect(wall12) or player_mask.colliderect(wall13) or player_mask.colliderect(wall14) or player_mask.colliderect(wall15) or player_mask.colliderect(wall16) or player_mask.colliderect(wall17) or player_mask.colliderect(wall18):
        if right:
            coords[0] += SPEED
        elif left:
            coords[0] += SPEED
        elif up:
            coords[1] += SPEED
        elif down:
            coords[1] -= SPEED

def main(screen):
    global right
    right = False
    global left
    left = False
    global up
    up = False
    global down
    down = False

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right = True
                    before = "r"
                if event.key == pygame.K_LEFT:
                    left = True
                    before = "l"
                if event.key == pygame.K_DOWN:
                    down = True
                    before = "d"
                if event.key == pygame.K_UP:
                    up = True
                    before = "u"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_DOWN:
                    down = False
                if event.key == pygame.K_UP:
                    up = False
        if right:
            coords[0] += SPEED
        if left:
            coords[0] -= SPEED
        if up:
            coords[1] -= SPEED
        if down:
            coords[1] += SPEED
        
        global player_mask
        player_mask = pygame.Rect(coords[0],coords[1], 100, 100)
        
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, BLACK, player_mask)
        screen.blit(player, coords)
        pygame.draw.rect(screen, BLACK, door_mask)
        screen.blit(door, DOOR_COORDS)
        collision(screen)
        check_end(screen)
        draw_map(screen)

        pygame.display.update()

if __name__ == "__main__":
    main(screen)