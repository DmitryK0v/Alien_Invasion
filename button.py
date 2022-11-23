import pygame.font


class Button(object):
    def __init__(self, ai_settings, screen):
        """Initializes button attributes"""
        self.msg_image_rect = None
        self.msg_image = None
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Assigning sizes and properties to buttons.
        self.width, self.height = 200, 75
        self.button_color = (0, 0, 0)
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont('Comic Sans', 48)

        # Constructing the rect object of the button and aligning it to the center of the screen.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

    def prep_msg_play(self, msg):
        """Converts msg to a rectangle and aligns the text to the center."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_msg_pause(self, msg):
        """Converts msg to a rectangle and aligns the text to the bottom."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button_play(self, msg):
        self.prep_msg_play(msg)
        # Displaying an empty button and displaying a message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_button_pause(self, msg):
        self.prep_msg_pause(msg)
        # Displaying an empty button and displaying a message.
        self.rect = pygame.Rect(500, 500, self.width, self.height)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
