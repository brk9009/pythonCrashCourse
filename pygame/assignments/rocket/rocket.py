import pygame

class Rocket():
    
    def __init__(self, settings, screen):
        """Initialize the rocket"""
        self.screen = screen
        self.settings = settings
        
        # Load the rocket
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start the rocket in the middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        # Store a decimal value for the rockets center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the ship's postion based on the movement flag"""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.rocket_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.rocket_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.settings.rocket_speed_factor
            
        # Update rect object from self.center 
        if self.moving_up or self.moving_down:
            self.rect.centery = self.centery
        if self.moving_left or self.moving_right:
            self.rect.centerx = self.centerx
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        