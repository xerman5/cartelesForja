#!/usr/bin/env python3
"""Actualiza el catálogo estático de Game-icons; no se necesita para usar el editor."""
import argparse
from collections import Counter
import io
import json
from pathlib import Path
import re
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parent
REPO = 'https://github.com/game-icons/icons'
CC_BY = 'https://creativecommons.org/licenses/by/3.0/'
CC_ZERO = 'https://creativecommons.org/publicdomain/zero/1.0/'
CHUNK_SIZE = 128
AUTHOR_NAMES = {
  'andymeneely': 'Andy Meneely', 'aussiesim': 'Aussiesim',
  'badges': 'Game-icons.net contributors', 'carl-olsen': 'Carl Olsen',
  'caro-asercion': 'Caro Asercion', 'cathelineau': 'Cathelineau', 'catsu': 'Catsu',
  'darkzaitzev': 'DarkZaitzev', 'delapouite': 'Delapouite', 'faithtoken': 'Faithtoken',
  'felbrigg': 'Felbrigg', 'generalace135': 'GeneralAce135', 'guard13007': 'Guard13007',
  'heavenly-dog': 'HeavenlyDog', 'irongamer': 'Irongamer', 'john-colburn': 'John Colburn',
  'john-redman': 'John Redman', 'kier-heyl': 'Kier Heyl', 'lorc': 'Lorc',
  'lord-berandas': 'Lord Berandas', 'lucasms': 'Lucas', 'pepijn-poolman': 'Pepijn Poolman',
  'pierre-leducq': 'Pierre Leducq', 'priorblue': 'PriorBlue', 'quoting': 'Quoting',
  'rihlsul': 'Rihlsul', 'sbed': 'Sbed', 'seregacthtuf': 'SeregaCthtuf', 'skoll': 'Skoll',
  'sparker': 'Sparker', 'spencerdub': 'SpencerDub', 'starseeker': 'Starseeker',
  'various-artists': 'Various artists', 'viscious-speed': 'Viscious Speed',
  'willdabeast': 'Willdabeast', 'zajkonur': 'Zajkonur', 'zeromancer': 'Zeromancer'
}
# Búsqueda por palabras españolas además del nombre original, sin traducir nombres a medias.
SPANISH = dict(pair.split('=', 1) for pair in '''
abstract=abstracto símbolo
ace=as as de cartas
acid=ácido
alien=alienígena extraterrestre
anchor=ancla
angel=ángel
animal=animal
anvil=yunque
apple=manzana
archer=arquero arco
arrow=flecha
axe=hacha
bag=bolsa
ball=pelota balón bola
barrel=barril
bat=murciélago bate
battle=batalla combate
bear=oso
bee=abeja
beer=cerveza
bird=ave pájaro
boat=barco bote
body=cuerpo
bone=hueso
book=libro
boot=bota calzado
bottle=botella
bow=arco
bridge=puente
broken=roto rota
bull=toro
bullet=bala munición
butterfly=mariposa
cage=jaula
camp=campamento
candle=vela
cannon=cañón
car=coche automóvil
card=carta baraja
cards=cartas baraja
castle=castillo fortaleza
cat=gato felino
chain=cadena
chest=cofre pecho
chess=ajedrez
chicken=gallina pollo
circle=círculo
city=ciudad
claw=garra
clock=reloj tiempo
cloud=nube
clover=trébol
cobra=cobra serpiente
coffee=café
cog=engranaje
coin=moneda
coins=monedas dinero
compass=brújula
computer=ordenador computadora
cow=vaca
crab=cangrejo
cross=cruz
crossed=cruzadas cruzados
crown=corona
crystal=cristal gema
cup=taza copa
dagger=daga
death=muerte
deer=ciervo
desert=desierto
diamond=diamante
dice=dado dados azar
boat=barco
wizard=mago hechicero
witch=bruja
knight=caballero caballo
shield=escudo defensa
sword=espada arma
swords=espadas armas
spear=lanza
helmet=casco
king=rey
queen=reina
prince=príncipe
princess=princesa
dragon=dragón
dog=perro
dolphin=delfín
door=puerta
dove=paloma
eagle=águila
earth=tierra planeta
egg=huevo
elephant=elefante
elf=elfo
emblem=emblema heráldica
eye=ojo
eyes=ojos
fairy=hada
fang=colmillo
farm=granja
feather=pluma
fence=valla
fire=fuego incendio
fish=pez pescado
fist=puño
flame=llama fuego
flower=flor
flying=volador vuelo
forest=bosque
fortress=fortaleza
fox=zorro
frog=rana
fruit=fruta
gear=engranaje
gears=engranajes
 gem=gema
 ghost=fantasma
 giant=gigante
 glass=vaso cristal
 globe=globo tierra
 goat=cabra
 gold=oro dorado
 griffin=grifo
 gun=pistola arma
 hammer=martillo
 hand=mano
 heart=corazón vida amor
 hearts=corazones cartas
 horse=caballo
 hourglass=reloj arena tiempo
 house=casa
 ice=hielo
 island=isla
 key=llave
 knife=cuchillo
 lantern=farol linterna
 laurel=laurel
 laurels=laureles
 leaf=hoja
 leaves=hojas
 lightning=rayo relámpago
 lion=león
 lock=cerradura candado
 machine=máquina
 magic=magia mágico
 map=mapa
 mask=máscara
 meeple=meeple peón jugador
 metal=metal
 mine=mina
 moon=luna
 mountain=montaña
 mountains=montañas
 mushroom=seta hongo
 music=música
 ninja=ninja
 oak=roble árbol
 octopus=pulpo
 oil=petróleo aceite
 orb=orbe esfera
 orc=orco
 owl=búho
 padlock=candado
 palm=palmera palma
 paper=papel
 paw=huella pata
 people=personas gente
 person=persona
 pig=cerdo
 pine=pino árbol
 pirate=pirata
 plant=planta
 player=jugador
 pocket=bolsillo
 poker=póker cartas
 potion=poción
 power=energía poder
 rabbit=conejo
 raven=cuervo
 ring=anillo aro
 river=río
 road=carretera camino
 robot=robot autómata
 rock=roca piedra
 rocket=cohete
 rose=rosa flor
 ruin=ruina
 ruins=ruinas
 rune=runa
 sail=vela velero
 salmon=salmón pez
 sand=arena
 scroll=pergamino
 sea=mar
 shark=tiburón
 sheep=oveja
 ship=barco nave
 shovel=pala
 skeleton=esqueleto
 skull=calavera cráneo
 snake=serpiente
 snow=nieve
 soldier=soldado
 space=espacio espacial
 spaceship=nave espacial
 spade=pica pala
 spider=araña
 star=estrella
 stars=estrellas
 stone=piedra
 storm=tormenta
 sun=sol
 sunrise=amanecer
 sunset=atardecer
 tent=tienda campamento
 tiger=tigre
 time=tiempo
 torch=antorcha
 tower=torre
 train=tren
 treasure=tesoro
 tree=árbol
 trophy=trofeo victoria
 turtle=tortuga
 ufo=ovni
 vampire=vampiro
 village=pueblo aldea
 volcano=volcán
 wall=muro pared
 warrior=guerrero
 watch=reloj
 water=agua
 wave=ola
 weapon=arma
 web=telaraña web
 wheel=rueda
 wind=viento
 wing=ala
 winged=alado alada alas
 wings=alas
 wolf=lobo
 wood=madera
 zombie=zombi muerto viviente
'''.strip().splitlines())
SPANISH = {key.strip(): value for key, value in SPANISH.items()}
CATEGORIES = [
  ('Animales', 'animal bear bee bird bull butterfly cat chicken cobra cow crab deer dog dolphin dove eagle elephant fish fox frog goat griffin horse insect lion octopus owl pig rabbit raven salmon shark sheep snake spider tiger turtle wolf'),
  ('Espacio', 'alien astronaut atom galaxy moon planet rocket satellite space spaceship shuttle star ufo'),
  ('Juegos', 'ace card cards chess dice domino meeple pawn player poker puzzle token trophy'),
  ('Armas y combate', 'archer armor arrow axe battle blade bow bullet cannon dagger fist gun helmet knife missile shield spear sword swords tank weapon'),
  ('Magia y criaturas', 'angel demon devil dragon dwarf elf fairy fantasy ghost giant goblin magic monster ninja orc potion rune scroll skeleton skull vampire witch wizard zombie'),
  ('Edificios y lugares', 'bridge building castle church city door dungeon farm fortress gate house hut island mine palace road ruin ruins temple tent tower village wall'),
  ('Naturaleza', 'cloud desert earth feather fire flame flower forest fruit ice leaf leaves lightning mountain mountains mushroom oak palm pine plant river rock rose sand sea snow stone storm sun sunrise sunset tree volcano water wave wind wood'),
  ('Transporte', 'airplane balloon bike boat bus car carriage cart helicopter motorbike plane sail ship tractor train truck vehicle wheel'),
  ('Tecnología', 'android circuit cog computer drone engine factory gear gears machine mechanical metal power robot satellite screen steampunk steam technology'),
  ('Comida y bebida', 'apple banana beer bottle bread cake cheese coffee cooking cup drink egg food fork fruit glass grape meat milk orange pear pizza spoon wine'),
  ('Personas y equipo', 'arm bag body bone boot cloak coat crown eye eyes face foot hand head heart hearts human king knight leg man mask people person prince princess queen shoe soldier trousers warrior woman'),
  ('Símbolos', 'arrow circle compass cross crystal diamond gem hourglass key laurel laurels lock map music orb padlock ring spade symbol time watch'),
]


def category_for(slug, author):
  if author == 'badges':
    return 'Insignias'
  if slug.startswith('abstract-'):
    return 'Abstractos'
  words = set(slug.split('-'))
  for name, keywords in CATEGORIES:
    if words.intersection(keywords.split()):
      return name
  return 'Objetos y otros'


def author_data(folder):
  name = AUTHOR_NAMES[folder]
  url = 'https://game-icons.net/1x1/' + folder + '.html'
  if folder in ('badges', 'various-artists'):
    url = REPO + '/graphs/contributors'
  cc0 = folder in ('viscious-speed', 'zeromancer')
  return {'name': name, 'url': url, 'license': 'CC0 1.0' if cc0 else 'CC BY 3.0',
          'licenseUrl': CC_ZERO if cc0 else CC_BY}


def paths_from_svg(path):
  svg = ET.parse(path).getroot()
  paths = []
  for node in svg:
    tag = node.tag.split('}')[-1]
    if tag == 'path':
      if node.get('d') == 'M0 0h512v512H0z':
        continue
      # MZ es un trazado vacío presente en el original; no aporta geometría.
      if node.get('d') == 'MZ':
        continue
      if set(node.attrib) - {'d', 'fill'} or node.get('fill') != '#fff':
        raise ValueError('Trazado no reconocido: ' + str(path))
      paths.append({'d': node.attrib['d']})
    elif tag == 'circle':
      if not node.get('stroke'):
        continue  # Fondo negro de la insignia.
      if node.get('stroke') != '#fff':
        raise ValueError('Círculo no reconocido: ' + str(path))
      cx, cy, radius, stroke = (float(node.attrib[key]) for key in ('cx', 'cy', 'r', 'stroke-width'))
      outer, inner = radius + stroke / 2, radius - stroke / 2
      def circle(r):
        return f'M{cx-r:g} {cy:g}a{r:g} {r:g} 0 1 0 {2*r:g} 0a{r:g} {r:g} 0 1 0 {-2*r:g} 0z'
      paths.append({'d': circle(outer) + circle(inner), 'fill-rule': 'evenodd'})
    else:
      raise ValueError('Elemento SVG no reconocido: ' + tag + ' en ' + str(path))
  if not paths:
    raise ValueError('Icono sin geometría: ' + str(path))
  return svg.attrib['viewBox'], paths


def build(source, revision):
  overrides = json.loads((ROOT / 'overrides.json').read_text())
  old_ids = {}
  if (ROOT / 'library.js').exists():
    old = (ROOT / 'library.js').read_text().split('window.forjaIcons = ', 1)[1].split(';\n', 1)[0]
    for icon in json.loads(old):
      source_path = icon.get('sourcePath') or icon['source'].split('/1x1/')[1].removesuffix('.html')
      old_ids[source_path] = icon['id']
  all_paths = sorted(source.rglob('*.svg'))
  ids = dict(old_ids)
  ids.update({key: value['id'] for key, value in overrides.items()})
  used_ids = set(ids.values())
  # La primera selección mantiene su orden e identificadores. El resto va alfabético.
  ordered = sorted(all_paths, key=lambda path: (
    0 if str(path.relative_to(source).with_suffix('')) in overrides else 1,
    list(overrides).index(str(path.relative_to(source).with_suffix(''))) if str(path.relative_to(source).with_suffix('')) in overrides else 0,
    path.stem, str(path.relative_to(source))))
  authors, icons, deferred = {}, [], []
  for path in ordered:
    source_path = str(path.relative_to(source).with_suffix(''))
    folder, slug = source_path.split('/')
    authors[folder] = author_data(folder)
    if source_path not in ids:
      candidate = 'badge-' + slug if folder == 'badges' else slug
      if candidate in used_ids:
        candidate = slug + '-' + folder
      if candidate in used_ids:
        raise ValueError('Identificador duplicado: ' + candidate)
      ids[source_path] = candidate
      used_ids.add(candidate)
    view_box, paths = paths_from_svg(path)
    local = overrides.get(source_path, {})
    tags = ' '.join(dict.fromkeys(SPANISH[word] for word in slug.split('-') if word in SPANISH))
    icon = {'id': ids[source_path], 'name': local.get('name', slug.replace('-', ' ').capitalize()),
            'category': local.get('category', category_for(slug, folder)),
            'tags': local.get('tags', tags), 'authorId': folder, 'sourcePath': source_path, 'viewBox': view_box}
    if source_path in overrides:
      icon['paths'] = paths
    else:
      deferred.append((icon, paths))
    icons.append(icon)
  chunks = []
  for offset in range(0, len(deferred), CHUNK_SIZE):
    filename = 'paths-' + str(offset // CHUNK_SIZE + 1).zfill(3) + '.js'
    shapes = {}
    for icon, paths in deferred[offset:offset+CHUNK_SIZE]:
      icon['chunk'] = filename
      shapes[icon['id']] = paths
    chunks.append((filename, '// Game-icons.net, CC BY 3.0 / CC0. Créditos en library.js.\n'
      + 'Object.assign(window.forjaIconPaths || (window.forjaIconPaths = {}), '
      + json.dumps(shapes, ensure_ascii=False, separators=(',', ':')) + ');\n'))
  assert len(icons) == len(all_paths) == len({icon['id'] for icon in icons})
  metadata = {'repository': REPO, 'revision': revision, 'icons': len(icons),
              'regularIcons': sum(icon['authorId'] != 'badges' for icon in icons),
              'badges': sum(icon['authorId'] == 'badges' for icon in icons),
              'licenses': dict(Counter(authors[icon['authorId']]['license'] for icon in icons)),
              'inlineIcons': len(overrides), 'chunks': len(chunks)}
  for filename, contents in chunks:
    (ROOT / filename).write_text(contents)
  # Elimina únicamente bloques generados que ya no formen parte del catálogo.
  for previous in ROOT.glob('paths-*.js'):
    if previous.name not in {filename for filename, _ in chunks}:
      previous.unlink()
  header = '// Catálogo completo de Game-icons.net. CC BY 3.0 / CC0 según autor.\n// Los trazados se cargan por bloques al necesitarlos. Véase README.md.\n'
  (ROOT / 'library.js').write_text(header + 'window.forjaIconCatalog = ' + json.dumps(metadata, separators=(',', ':')) + ';\n'
    + 'window.forjaIconAuthors = ' + json.dumps(authors, ensure_ascii=False, separators=(',', ':')) + ';\n'
    + 'window.forjaIcons = ' + json.dumps(icons, ensure_ascii=False, separators=(',', ':')) + ';\n')
  (ROOT / 'catalog.json').write_text(json.dumps(metadata, indent=2) + '\n')
  (ROOT / 'LICENSE-game-icons.txt').write_bytes((source / 'license.txt').read_bytes())
  print(json.dumps(metadata, indent=2))
  print('Índice:', (ROOT / 'library.js').stat().st_size, 'bytes; trazados:', sum((ROOT / f).stat().st_size for f, _ in chunks), 'bytes')


def fetch(url):
  req = urllib.request.Request(url, headers={'User-Agent': 'Carteles-La-Forja-icon-library'})
  with urllib.request.urlopen(req, timeout=90) as response:
    return response.read()


def main():
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('--source', type=Path, help='Carpeta del repositorio oficial ya descargado')
  parser.add_argument('--revision', default='master', help='Commit o referencia del repositorio oficial')
  args = parser.parse_args()
  if args.source:
    build(args.source, args.revision)
    return
  revision = json.loads(fetch('https://api.github.com/repos/game-icons/icons/commits/' + args.revision))['sha']
  archive = fetch('https://codeload.github.com/game-icons/icons/zip/' + revision)
  with tempfile.TemporaryDirectory(prefix='forja-game-icons-') as directory:
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
      zipped.extractall(directory)
    build(Path(directory) / ('icons-' + revision), revision)


if __name__ == '__main__':
  main()
