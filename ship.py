import pygame

class Ship:
    """Classe que gerencia o navio."""

    def __init__(self, ai_game):
        """Inicializa o navio e configura a posição inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # carregando a imagem do navio an pegando seu retângulo.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # inicia cada novo barco na parte baixa e ao centro da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenha o barco em sua localização atual."""
        self.screen.blit(self.image, self.rect)