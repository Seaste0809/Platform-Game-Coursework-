import pygame
import time


def fading_animation():
    pygame.init()
    screen_fade_in = 0
    screen_fade_out = 1
    clock = pygame.time.Clock()
    screen_size = width, height = 1280, 736
    screen_window = pygame.display.set_mode(screen_size)
    font = pygame.font.SysFont('Comic Sans MS', 160, True)
    background2 = pygame.transform.scale(pygame.image.load("Images/download.jpg"), (1280, 736))
    rendered_text2 = pygame.transform.scale(pygame.image.load("screenshot2.jpg"), (1280, 736))
    death_screen = (pygame.image.load("screenshot.jpg"))
    mid_screen = pygame.transform.scale(pygame.image.load("Images/download.jpg"), (1280, 736))
    rendered_text1 = font.render("", True, (255, 0, 0))
    fade_in = 3
    fade_out = 1
    fade = lambda x: x

    text_rect1 = rendered_text1.get_rect(center=(width / 2, height / 2))
    screen_type = screen_fade_in
    previous_state_change = time.time()

    count = 0
    while count == 0:

        screen_window.blit(death_screen, (0, 0))
        state_time = time.time() - previous_state_change

        if screen_type == screen_fade_in:
            if state_time >= fade_in:
                screen_type = screen_fade_out
                state_time -= fade_in
                previous_state_change = time.time() - state_time

        elif screen_type == screen_fade_out:
            if state_time >= fade_out:
                count = 1

        if screen_type == screen_fade_in:
            fade_setting = fade(1.0 * state_time / fade_in)
            rendered_text = rendered_text1
        elif screen_type == screen_fade_out:
            fade_setting = fade(1.0 * state_time / fade_in)

        surface_plot_1 = pygame.surface.Surface((text_rect1.width, text_rect1.height))

        if screen_type == screen_fade_in:
            surface_plot_1.blit(rendered_text, (0, 0))
            screen_window.blit(background2, (0, 0))
            surface_plot_1.set_alpha(255 * fade_setting)
            background2.set_alpha((400 * fade_setting))
            screen_window.blit(surface_plot_1, text_rect1)

        if screen_type == screen_fade_out:
            screen_window.blit(mid_screen, (0, 0))
            rendered_text2.set_alpha(1200 * fade_setting)
            screen_window.blit(rendered_text2, (0, 0))

        pygame.display.flip()
        clock.tick(60)
