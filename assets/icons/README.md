# Biblioteca completa de Game-icons

Incluye **todos los 4.239 SVG** del [repositorio oficial de Game-icons.net](https://github.com/game-icons/icons): **4.180 iconos y 59 insignias circulares**. La revisión exacta está en [catalog.json](catalog.json). Las variantes con el mismo nombre y distinto autor se conservan por separado.

La mayoría de los dibujos son **CC BY 3.0**; los 123 de Viscious Speed y Zeromancer son **CC0 1.0**. Se incluye el aviso original en [LICENSE-game-icons.txt](LICENSE-game-icons.txt). Cada icono conserva autor, procedencia y licencia. Las insignias se atribuyen al colectivo de colaboradores de Game-icons.net, como están agrupadas en el repositorio; no se inventan autores individuales.

Adaptaciones: eliminación del fondo negro; conversión del borde circular de las insignias a trazado; el editor ajusta el color, encuadre y tamaño. No se han generado dibujos con IA.

## Carga y búsqueda

- `library.js` es un índice de unos **900 KB**, con los metadatos de todos los iconos y los trazados de los 59 iniciales.
- `paths-001.js` a `paths-033.js` contienen el resto de los dibujos en bloques de hasta 128 iconos. **No se cargan al abrir la página**: solo al ver miniaturas, elegir un icono o restaurar un cartel que lo utiliza. Cada bloque se carga una vez por página.
- Se normalizan los nombres, categorías, autores y palabras relacionadas una sola vez para buscar sin distinguir mayúsculas ni tildes. Los filtros por categoría y autor se combinan con todas las palabras escritas.
- Se crean hasta **96 resultados por página**. Las miniaturas se cargan al entrar en la zona visible; Anterior / Siguiente recorre los demás resultados.
- Los nombres originales están en inglés; los 59 nombres españoles iniciales se mantienen. Se añaden equivalencias de búsqueda en español para muchos términos habituales. Las categorías de las nuevas incorporaciones se asignan por palabras clave; son una ayuda de navegación, no una taxonomía oficial ni una traducción completa del catálogo.

Se usan scripts clásicos para que la carga funcione también con `file://`, sin servidor, `fetch`, APIs ni dependencias. Conserva **toda esta carpeta** al mover o publicar el editor. Las exportaciones esperan a que se carguen los iconos utilizados y llevan los trazados dentro: no dependen de estos bloques al compartir el PNG o SVG.

## Uso y atribución

Los iconos son gratuitos, también para uso comercial, con las condiciones de su licencia: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) o [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

**Créditos de los iconos utilizados** prepara el texto de atribución correspondiente a cada autor y permite descargarlo en `.txt`. También se incrusta en `<desc>` del SVG y en el bloque `iTXt` / `Description` del PNG. Acompaña los créditos de los dibujos CC BY al publicar o imprimir el cartel; los metadatos pueden perderse al subir imágenes a otras plataformas. Los dibujos CC0 no requieren atribución, aunque el editor también recoge su procedencia.

## Actualizar el catálogo

El editor sigue siendo una aplicación estática: no hay instalación ni compilación. El siguiente script de mantenimiento es opcional y requiere únicamente Python 3 y conexión para volver a descargar el repositorio oficial:

```sh
python3 assets/icons/update-library.py
```

Para reproducir la versión incluida, usa el commit de `catalog.json`:

```sh
python3 assets/icons/update-library.py --revision 82d948812bfe3f269ef8f731dcdb07b08160edc4
```

También puede importar una descarga ya descomprimida, sin red:

```sh
python3 assets/icons/update-library.py --source /ruta/al/repositorio/icons --revision COMMIT
```

El generador conserva los identificadores existentes, reconoce las licencias CC0 de los autores indicados en el aviso oficial y se detiene si encuentra SVG con elementos o atributos no reconocidos. Los metadatos españoles de la selección inicial se mantienen en `overrides.json`; puedes ampliar ese archivo usando como clave `autor/nombre-del-icono` y los campos `id`, `name`, `category` y `tags`.

No cambies identificadores ya publicados: los proyectos guardan referencias como `[icon:elephant]` o `[icon:elephant:#d2ad43]` en `settings.txt`, dentro del formato `.cartel.json` versión 1. Las insignias usan el prefijo `badge-`; las demás variantes que comparten nombre añaden el autor cuando es necesario. No se añaden claves de almacenamiento ni se cambia el formato JSON.

Después de actualizar, comprueba búsqueda, paginación, carga desde `file://`, guardado de proyectos y exportaciones PNG/SVG. La carpeta completa ocupa unos 7 MB; el navegador carga solo los bloques necesarios.
