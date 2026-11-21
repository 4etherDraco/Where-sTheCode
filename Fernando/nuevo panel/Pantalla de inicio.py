import sys
import pygame


class Boton:

  def __init__(self, ruta_imagen, posicion, escala=2, accion=None):
    imagen_orig = pygame.image.load(ruta_imagen).convert_alpha()
    ancho, alto = imagen_orig.get_size()
    self.imagen = pygame.transform.scale(
        imagen_orig, (ancho * escala, alto * escala)
    )
    self.rect = self.imagen.get_rect(center=posicion)
    self.accion = accion

  def dibujar(self, superficie):
    superficie.blit(self.imagen, self.rect)

  def manejar_evento(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if self.rect.collidepoint(event.pos) and self.accion:
        self.accion()


class PantallaInicio:

  def __init__(self, ancho=800, alto=600, titulo="Pantalla de inicio"):
    pygame.init()
    self.ancho = ancho
    self.alto = alto
    self.ventana = pygame.display.set_mode((self.ancho, self.alto))
    pygame.display.set_caption(titulo)
    self.reloj = pygame.time.Clock()
    self.color_fondo = (33, 33, 33)

    panel_orig = pygame.image.load("preview.png").convert_alpha()
    p_ancho, p_alto = panel_orig.get_size()
    self.panel = pygame.transform.scale(panel_orig, (p_ancho * 2, p_alto * 2))
    self.panel_rect = self.panel.get_rect(
        center=(self.ancho // 2, self.alto // 2)
    )

    self.boton_izq = Boton(
        ruta_imagen="Botón.jpeg",
        posicion=(305, 405),
        escala=2,
        accion=self.reiniciar_partida,
    )
    self.boton_der = Boton(
        ruta_imagen="Botón.jpeg",
        posicion=(480, 405),
        escala=2,
        accion=self.salir_al_menu,
    )
    self.botones = [self.boton_izq, self.boton_der]

  def reiniciar_partida(self):
    print("Reiniciar partida")

  def salir_al_menu(self):
    print("salir al menú")

  def manejar_eventos(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      for boton in self.botones:
        boton.manejar_evento(event)

  def dibujar(self):
    self.ventana.fill(self.color_fondo)
    self.ventana.blit(self.panel, self.panel_rect)

    for boton in self.botones:
      boton.dibujar(self.ventana)

    pygame.display.flip()

  def ejecutar(self):
    while True:
      self.manejar_eventos()
      self.dibujar()
      self.reloj.tick(60)


if __name__ == "__main__":
  app = PantallaInicio()
  app.ejecutar()





