import pygame
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pygame.init()
pygame.mixer.init()

# --------------------
# VENTANA
# --------------------
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Letter For Mongui ❤️")
icon = pygame.image.load(resource_path("assets/icon.png"))
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# --------------------
# COLORES
# --------------------
WHITE = (245, 242, 235)
CREAM = (252, 248, 236)
BLACK = (40, 40, 40)
GRAY = (180, 180, 180)

# --------------------
# FUENTES
# --------------------
font = pygame.font.Font(resource_path("assets/font.ttf"), 26)
big_font = pygame.font.Font(resource_path("assets/font.ttf"), 40)
letter_font = pygame.font.Font(resource_path("assets/font.ttf"), 20)

# --------------------
# IMÁGENES PERSONAJES
# --------------------
girl = pygame.image.load(resource_path("assets/girl.png")).convert_alpha()
girl = pygame.transform.scale(girl, (210, 330))

jose = pygame.image.load(resource_path("assets/jose.png")).convert_alpha()
jose = pygame.transform.scale(jose, (210, 330))

pygame.mixer.music.load(resource_path("assets/music.mp3"))
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

# --------------------
# IMÁGENES CARTA
# --------------------
envelope = pygame.image.load(resource_path("assets/envelope.png")).convert_alpha()
envelope = pygame.transform.scale(envelope, (150, 150))

envelope_closed = pygame.image.load(resource_path("assets/envelope_closed.png")).convert_alpha()
envelope_closed = pygame.transform.scale(envelope_closed, (340, 340))

envelope_open = pygame.image.load(resource_path("assets/envelope_open.png")).convert_alpha()
envelope_open = pygame.transform.scale(envelope_open, (340, 340))

letter_img = pygame.image.load(resource_path("assets/letter.png")).convert_alpha()
letter_img = pygame.transform.scale(letter_img, (420, 520))

# --------------------
# POSICIONES
# --------------------
girl_x = 40
girl_y = 180

jose_x = 620
jose_y = 180

speed = 5

# --------------------
# ESTADOS
# --------------------
letter_given = False

scene = "game"
# game
# closed
# opened
# letter
# read

transition_time = 0
letter_y = 500

running = True

while running:


    # --------------------
    # EVENTOS
    # --------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
            and letter_given
            and scene == "game"
        ):
            scene = "closed"
            transition_time = pygame.time.get_ticks()

    # --------------------
    # MOVIMIENTO
    # --------------------
    keys = pygame.key.get_pressed()

    if scene == "game" and not letter_given:

        if keys[pygame.K_LEFT]:
            girl_x -= speed

        if keys[pygame.K_RIGHT]:
            girl_x += speed

        if keys[pygame.K_UP]:
            girl_y -= speed

        if keys[pygame.K_DOWN]:
            girl_y += speed

    # --------------------
    # ¿LLEGÓ A JOSÉ?
    # --------------------
    if not letter_given and abs(girl_x - jose_x) < 70:
        letter_given = True

    # ==================================================
    # ESCENA PRINCIPAL
    # ==================================================
    if scene == "game":

        screen.fill(WHITE)

        screen.blit(girl, (girl_x, girl_y))
        screen.blit(jose, (jose_x, jose_y))

        name1 = font.render("Isa", True, BLACK)
        name2 = font.render("Jose", True, BLACK)

        screen.blit(
            name1,
            name1.get_rect(center=(girl_x + 105, girl_y - 20))
        )

        screen.blit(
            name2,
            name2.get_rect(center=(jose_x + 105, jose_y - 20))
        )

        if letter_given:

            screen.blit(envelope, (360, 240))

            text1 = font.render(
                "Mongui, te escribí una carta...",
                True,
                BLACK
            )

            text2 = font.render(
                "(Se abre con SPACE (porque estamos en  la compu lol)",
                True,
                BLACK
            )

            screen.blit(
                text1,
                text1.get_rect(center=(WIDTH // 2, 90))
            )

            screen.blit(
                text2,
                text2.get_rect(center=(WIDTH // 2, 125))
            )

    # ==================================================
    # SOBRE CERRADO
    # ==================================================
    elif scene == "closed":

        screen.fill(CREAM)

        screen.blit(
            envelope_closed,
            envelope_closed.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        )

        if pygame.time.get_ticks() - transition_time > 900:
            scene = "opened"
            transition_time = pygame.time.get_ticks()

    # ==================================================
    # SOBRE ABIERTO
    # ==================================================
    elif scene == "opened":

        screen.fill(CREAM)

        screen.blit(
            envelope_open,
            envelope_open.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        )

        if pygame.time.get_ticks() - transition_time > 900:
            scene = "letter"
            letter_y = 500

    # ==================================================
    # CARTA SALE DEL SOBRE
    # ==================================================
    elif scene == "letter":

        screen.fill(CREAM)

        screen.blit(
            envelope_open,
            envelope_open.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        )

        screen.blit(
            letter_img,
            letter_img.get_rect(center=(WIDTH // 2, letter_y))
        )

        if letter_y > 180:
            letter_y -= 3
        else:
            scene = "read"

    # ==================================================
    # CARTA ABIERTA
    # ==================================================
    elif scene == "read":

        screen.fill(CREAM)

        pygame.draw.rect(screen, (255, 255, 255), (110, 50, 580, 500))
        pygame.draw.rect(screen, GRAY, (110, 50, 580, 500), 3)

        title = big_font.render("Para mi mongui", True, BLACK)
        screen.blit(
            title,
            title.get_rect(center=(WIDTH // 2, 90))
        )

        lines = [

            "Hola mongui",
            "Esta es una pequeña cartajuego que hice para ti.",
            "",
            "Hoy aprendiendo a hacer minijuegos",
            "hacerte algo cursi fue lo primero que se me ocurrio.",
            "Todavia no es muy pro",
            "pero lo hice con todo mi amor",
            "",
            "Gracias por llegar a mi vida y hacerme tan feliz.",
            "por amarme asi como soy y por hacerme sentir tan especial.",
            "y por tener paciencia con la distancia.",
            "",
            "Cada día estamos más cerca de poder abrazarnos y darnos besitos.",
            "",
            "te extraño",
            "te amo.",
            "",
            "— Isabella"
        ]

        y = 145

        for line in lines:

            text = letter_font.render(line, True, BLACK)

            screen.blit(
                text,
                text.get_rect(center=(WIDTH // 2, y))
            )

            y += 16

    pygame.display.flip()
    clock.tick(60)

pygame.quit()