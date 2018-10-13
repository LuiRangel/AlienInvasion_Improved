import pygame.font


class Menu:

    def __init__(self, ai_settings, screen, title, sub_title):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Set the dimensions and the properties of the title
        self.title_font = pygame.font.SysFont(None, 200)
        self.sub_title_font = pygame.font.SysFont(None, 100)
        self.alien_point_font = pygame.font.SysFont(None, 50)

        self.title_color = (230, 230, 230)
        self.sub_title_color = (3, 241, 17)
        self.title = title
        self.sub_title = sub_title
        self.alien1_points = '= 10 PTS'
        self.alien2_points = '= 20 PTS'
        self.alien3_points = '= 40 PTS'

        # Initialize title variables (font, rect, ect) (had to do it so i can get a green checkmark
        self.title_image = False
        self.title_image_rect = False
        self.sub_title_image = False
        self.sub_title_image_rect = False

        self.play_button = Button(ai_settings, screen, 'PLAY')
        self.high_scores_button = HighScoreButton(ai_settings, screen, 'High Scores')
        self.prep_title(self.title, self.sub_title)

        # -------------------------- creates image for points for each alien -----------------------------------
        self.alien1_image = pygame.image.load('images/alien_alpha_f1.gif')
        self.alien1_image_rect = self.alien1_image.get_rect()
        self.alien1_image_rect.centerx = self.screen_rect.centerx - 50
        self.alien1_image_rect.centery = self.screen_rect.centery + 10
        self.alien1_points_image = self.alien_point_font.render(self.alien1_points, True, self.title_color, None)
        self.alien1_points_image_rect = self.alien1_points_image.get_rect()
        self.alien1_points_image_rect.left = self.alien1_image_rect.right + 10
        self.alien1_points_image_rect.centery = self.screen_rect.centery

        self.alien2_image = pygame.image.load('images/alien_scouter_f1.gif')
        self.alien2_image_rect = self.alien2_image.get_rect()
        self.alien2_image_rect.centerx = self.screen_rect.centerx - 50
        self.alien2_image_rect.centery = self.alien1_image_rect.centery + 50
        self.alien2_points_image = self.alien_point_font.render(self.alien2_points, True, self.title_color, None)
        self.alien2_points_image_rect = self.alien2_points_image.get_rect()
        self.alien2_points_image_rect.left = self.alien2_image_rect.right + 10
        self.alien2_points_image_rect.centery = self.alien1_points_image_rect.centery + 60

        self.alien3_image = pygame.image.load('images/alien_f1.gif')
        self.alien3_image_rect = self.alien3_image.get_rect()
        self.alien3_image_rect.centerx = self.screen_rect.centerx - 50
        self.alien3_image_rect.centery = self.alien2_image_rect.centery + 50
        self.alien3_points_image = self.alien_point_font.render(self.alien3_points, True, self.title_color, None)
        self.alien3_points_image_rect = self.alien3_points_image.get_rect()
        self.alien3_points_image_rect.left = self.alien3_image_rect.right + 10
        self.alien3_points_image_rect.centery = self.alien2_points_image_rect.centery + 60
        # -------------------------------------------------------------------------------------------------------

    def prep_title(self, title, sub_title):
        # Draw title
        self.title_image = self.title_font.render(title, True, self.title_color, None)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.centery - (self.screen_rect.centery / 2)

        # Draw sub title
        self.sub_title_image = self.sub_title_font.render(sub_title, True, self.sub_title_color, None)
        self.sub_title_image_rect = self.sub_title_image.get_rect()
        self.sub_title_image_rect.centerx = self.screen_rect.centerx
        self.sub_title_image_rect.centery = self.title_image_rect.bottom + 40

    def draw_menu(self):
        self.screen.fill(self.ai_settings.menu_bg_color)
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.sub_title_image, self.sub_title_image_rect)
        self.screen.blit(self.alien1_image, self.alien1_image_rect)
        self.screen.blit(self.alien1_points_image, self.alien1_points_image_rect)
        self.screen.blit(self.alien2_image, self.alien2_image_rect)
        self.screen.blit(self.alien2_points_image, self.alien2_points_image_rect)
        self.screen.blit(self.alien3_image, self.alien3_image_rect)
        self.screen.blit(self.alien3_points_image, self.alien3_points_image_rect)

        self.play_button.draw_button()
        self.high_scores_button.draw_button()


class Button:

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        # self.button_color = (0, 0, 0)
        self.text_color = (3, 241, 17)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + (self.screen_rect.centery / 2)

        # The button message needs to be prepped only once.
        self.msg_image = False
        self.msg_image_rect = False
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turns msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.ai_settings.menu_bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.ai_settings.menu_bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class HighScoreButton(Button):

    def __init__(self, ai_settings, screen, msg):
        super(HighScoreButton, self).__init__(ai_settings, screen, msg)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        # self.button_color = (0, 0, 0)
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.right - 150
        self.rect.centery = self.screen_rect.bottom - 50

        # The button message needs to be prepped only once.
        self.prep_msg('High Scores')

    def prep_msg(self, msg):
        """Turns msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.ai_settings.menu_bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.ai_settings.menu_bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
