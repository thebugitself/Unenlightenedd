import pygame

image_0 = '../graphics/map/messages/0.png'
image_1 = '../graphics/map/messages/1.png'
image_2 = '../graphics/map/messages/2.png'
image_coordinate = '../graphics/map/messages/coordinate.png'
image_cute = '../graphics/map/messages/cute.png'
image_path = '../graphics/map/messages/path.png'
image_info = '../graphics/map/messages/info.png'
image_suffer = '../graphics/map/messages/suffer.png'
image_tolong = '../graphics/map/messages/tolong.png'
image_tutorial = '../graphics/map/messages/tutorial.png'
image_close = '../graphics/map/messages/close.png'
image_diedie = '../graphics/map/messages/diedie.png'
image_cold = '../graphics/map/messages/cold.png'
image_lastclue = '../graphics/map/messages/lastclue.png'
image_keepgoing = '../graphics/map/messages/keepgoing.png'
image_goodbye = '../graphics/map/messages/goodbye.png'

class Pesan: #enkapsulasi
    def draw(self, surface, path):
        self.__path = path
        self.__notes = pygame.image.load(self.__path).convert_alpha()
        surface.blit(self.__notes, (320, 180))