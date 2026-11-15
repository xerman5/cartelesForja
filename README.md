# Carteles La Forja

Dos editores de carteles en una aplicación web estática, sin instalación de dependencias:

- **Partidas** (`index.html`): portada, descripción, fecha, horario, lugar, plazas y valoraciones BGG. Exporta PNG y WebP.
- **Tipográfico** (`tipografico.html`): líneas de texto o iconos, alturas por línea, fuentes variables o propias, papel, grano, arrugas y datos de evento con zona inferior de altura automática, integrada en el cartel o como anexo pegado debajo. Exporta PNG y SVG, con formatos para pantalla e imprenta.

## Uso local

Desde la carpeta del proyecto:

```sh
python3 -m http.server 8000
```

Abre <http://localhost:8000>. La barra superior permite cambiar de editor. También puedes abrir los HTML directamente; Tusker se carga automáticamente, incluso sin servidor.

## Llevar una partida al editor tipográfico

En Partidas, pulsa **Usar esta partida en Tipográfico** y confirma. Se copian título, fecha, horario, lugar y plazas, sustituyendo esos textos del editor tipográfico. El diseño de cada editor se conserva por separado; la portada y los ajustes visuales no se transfieren.

Ambos editores recuerdan su trabajo en el navegador. Guarda además los proyectos en JSON para conservarlos o moverlos a otro equipo. Cada editor abre su propio formato: `.json` en Partidas y `.cartel.json` en Tipográfico.

## Tipografías y ayuda

En el editor tipográfico, Tusker aparece automáticamente en el selector, agrupada por peso y con sus distintos anchos. **Usar Tusker Super · 9 anchos** selecciona el grupo de mayor amplitud. El archivo `fonts/tusker/bundled.js` incluye los TTF para permitir su carga sin servidor. También puedes añadir archivos OTF, TTF, WOFF y WOFF2 mediante el botón **+**. Las fuentes propias se procesan y guardan en el navegador.

Las fuentes de Google necesitan conexión. Las fuentes locales permiten trabajar sin ella. El JSON y el SVG del editor tipográfico pueden incluir las fuentes utilizadas.

Consulta la [ayuda completa de Cartel a caja](docs/cartel-a-caja.txt) para los efectos, los formatos de impresión y la exportación.

## Iconos en el cartel tipográfico

En **Texto**, cada línea tiene un selector **Texto / Icono**. Usa **+ Texto** o **+ Icono** para añadir líneas, las flechas para ordenarlas y **×** para eliminarlas. Puedes pegar varias líneas en un campo de texto o usar **Edición multilínea**. Se admiten hasta 14 líneas no vacías en el cartel.

La biblioteca incluye el catálogo completo del repositorio de Game-icons.net: **4.239 SVG** (4.180 iconos y 59 insignias circulares). Busca por nombre original en inglés, por los nombres españoles de la selección inicial o por palabras relacionadas en español, como «caballo», «dragón», «barco» o «dado». Puedes combinar palabras y filtrar por categoría y autor. Los resultados se muestran en páginas de hasta 96 iconos; las miniaturas se cargan al aparecer en pantalla.

Los iconos se centran en su línea y conservan sus proporciones en todos los repartos. En **Por línea** puedes reservarles más o menos altura; **Color propio** permite darles una tinta distinta. Comparten los efectos del cartel y se incluyen como vectores en el SVG y en la descarga PNG.

Los iconos funcionan sin conexión, también abriendo el HTML directamente: conserva **toda** la carpeta `assets/icons/` junto al editor. El índice ocupa unos 900 KB y los dibujos adicionales se cargan por bloques solo al necesitarlos; el catálogo completo ocupa unos 7 MB. Los 59 iconos anteriores conservan sus identificadores. No cambian las claves de almacenamiento ni el formato `.cartel.json`: se representan dentro del texto como `[icon:elephant]` o `[icon:elephant:#d2ad43]`. Los proyectos anteriores siguen abriéndose.

Incluye obras de **Lorc, Delapouite, Skoll y el resto de colaboradores**, bajo **CC BY 3.0** o **CC0** según el autor. En **Créditos de los iconos utilizados** puedes copiar o descargar la atribución correspondiente; también se incrusta en los metadatos de PNG y SVG. Consulta la [procedencia y actualización de la biblioteca](assets/icons/README.md).

[Vista de la biblioteca](docs/iconos-biblioteca.png) · [Cartel de ejemplo con icono](docs/iconos-cartel.png). El águila del ejemplo es de Lorc, de [Game-icons.net](https://game-icons.net/1x1/lorc/eagle-emblem.html), con licencia [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/); se ha eliminado el fondo y ajustado el color y el tamaño.

En **Estilo → Papel y pegado** hay 16 combinaciones de papel y tinta. **Invertir papel y tinta** permite obtener sus variantes sin repetir muestras. Las cinco nuevas son burdeos/mantequilla, violeta/lima, petróleo/coral, azul pizarra/lavanda y oliva/rosa empolvado. [Ver las cinco combinaciones en un cartel](docs/paletas-nuevas.png). La ayuda recoge los colores y sus referencias de diseño.

En **Estilo → Imagen**, sube una foto o textura y elige **Aplicar imagen a → Fondo o Letras**. En Letras, la imagen rellena el título sobre el color del papel, con el mismo zoom, encaje y opacidad. La elección se guarda en el proyecto y se incluye al exportar PNG o SVG.

[Comparativa de la misma imagen aplicada al fondo o a las letras](docs/imagen-fondo-letras.jpg).

En **Estilo → Arrugas y pegado**, el selector **Arrugas** ofrece ocho capas extraídas de fotografías de papel, además del motor por semilla. Las capas están incluidas para uso sin conexión y se incrustan al exportar. El [registro de la prueba](docs/arrugas-fotograficas.md) recoge las imágenes de origen, la extracción y las comprobaciones realizadas.
