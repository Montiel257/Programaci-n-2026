class Playlist:
  def __init__(self, nombre):
    self.nombre = nombre
    self.canciones = []

  def añadir_cancion(self, titulo):
    if len(self.canciones) >= 5:
      print("Alcanzaste el límite máximo de canciones por playlist")
    else:
      if titulo in self.canciones:
        print("La canción ya se encuentra en la playlist")
      else:
        self.canciones.append(titulo)
        print(f"{titulo} añadida a {self.nombre}.")

  def eliminar_cancion(self, titulo):
    if titulo in self.canciones:
      self.canciones.remove(titulo)
      print(f"{titulo} ha sido eliminado de {self.nombre}")
    else:
      print(f"{titulo} no está en {self.nombre}")

  def total_canciones(self):
    return len(self.canciones)

  def mostrar_playlist(self):
    print(f"========== Playlist: {self.nombre} ==========")
    if len(self.canciones) == 0:
      print("La Playlist está vacía actualmente")
    else:
      i = 1
      for titulo in self.canciones:
        print(i, titulo)
        i += 1

  def limpiar_playlist(self):
    self.canciones.clear()
    print("La playlist está vacía")

  def buscador(self, texto):
    if texto in self.canciones:
      print(f"La canción {texto} forma parte de la playlist {self.nombre}")
    else:
      print(f"La canción {texto} no existe en la playlist {self.nombre}")


mi_mix = Playlist("Mi Mix 2026")

mi_mix.añadir_cancion("Ella Baila Sola - Peso Pluma")
mi_mix.añadir_cancion("AMG - Natanael Cano")
mi_mix.añadir_cancion("La Incondicional - Luis Miguel")
mi_mix.añadir_cancion("Tití Me Preguntó - Bad Bunny")

mi_mix.añadir_cancion("Do I Wanna Know? - Arctic Monkeys")

mi_mix.añadir_cancion("Lady Gaga - Peso Pluma")

mi_mix.mostrar_playlist()

print("\n--- Probando el buscador ---")
mi_mix.buscador("AMG - Natanael Cano")