class Button:
    """
    A class representing a button object.
    It's used to create buttons with images or text, set its position,
    update its appearance on the screen, check if it has been clicked, and change its color when hovered over.
    """
    def __init__(self, image, position, text_input, font, base_colour, hovering_colour):
        """
        Initializes the Button class with the following parameters:
        :param image: (pygame.Surface) The image to be used for the button.
        :param position: (tuple) The x and y coordinates of the button's position.
        :param text_input: (str) The text to be displayed on the button.
        :param font: (pygame.font.Font) The font used to render the text.
        :param base_colour: (tuple) The base color of the text.
        :param hovering_colour: (tuple) The color of the text when the button is hovered over.
        """
        self._image = image
        self._x_pos, self._y_pos = position
        self._text_input = text_input
        self._font = font
        self._base_color = base_colour
        self._hovering_color = hovering_colour

        self._text = self._font.render(self._text_input, True, self._base_color)
        if not self._image:
            self._image = self._text
        self._rect = self._image.get_rect(center=self.position)
        self._text_rect = self._text.get_rect(center=self.position)

    @property
    def image(self):
        """
        :return: (pygame.Surface) the image of the button
        """
        return self._image

    @property
    def position(self):
        """
        :return: (tuple) the x and y coordinates of the button's position
        """
        return self._x_pos, self._y_pos

    @position.setter
    def position(self, pos):
        """
        :param pos: (tuple) the new position for the button
        """
        self._x_pos, self._y_pos = pos
        self._rect.center = pos
        self._text_rect.center = pos

    def update(self, screen):
        """
        Updates the button's appearance on the screen.
        :param screen: (pygame.Surface) the surface where the button is drawn
        """
        if self._image:
            screen.blit(self._image, self._rect)
        screen.blit(self._text, self._text_rect)

    def check_for_input(self, position):
        """
        Checks if the button has been clicked.
        :param position: (tuple) the x and y coordinates of the mouse click
        :return: (bool) True if the button has been clicked, False otherwise
        """
        x, y = position
        if self._rect.left <= x <= self._rect.right and self._rect.top <= y <= self._rect.bottom:
            return True
        return False

    def change_colour(self, position):
        """
        Changes the color of the button when the mouse is hovering over it.
        :param position: (tuple) the x and y coordinates of the mouse position
        """
        x, y = position
        if (x >= self._rect.left) and (x <= self._rect.right) and (y >= self._rect.top) and (y <= self._rect.bottom):
            self._text = self._font.render(self._text_input, True, self._hovering_color)
        else:
            self._text = self._font.render(self._text_input, True, self._base_color)
