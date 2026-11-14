# Carteles La Forja

Dos editores de carteles en una aplicación web estática, sin instalación de dependencias:

- **Partidas** (`index.html`): portada, descripción, fecha, horario, lugar, plazas y valoraciones BGG. Exporta PNG y WebP.
- **Tipográfico** (`tipografico.html`): texto ajustado al ancho, alturas por línea, fuentes variables o propias, papel, grano, arrugas y datos de evento con zona inferior de altura automática, integrada en el cartel o como anexo pegado debajo. Exporta PNG y SVG, con formatos para pantalla e imprenta.

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

En **Estilo → Imagen**, sube una foto o textura y elige **Aplicar imagen a → Fondo o Letras**. En Letras, la imagen rellena el título sobre el color del papel, con el mismo zoom, encaje y opacidad. La elección se guarda en el proyecto y se incluye al exportar PNG o SVG.

[Comparativa de la misma imagen aplicada al fondo o a las letras](docs/imagen-fondo-letras.jpg).

En **Estilo → Arrugas y pegado**, el selector **Arrugas** ofrece ocho capas extraídas de fotografías de papel, además del motor por semilla. Las capas están incluidas para uso sin conexión y se incrustan al exportar. El [registro de la prueba](docs/arrugas-fotograficas.md) recoge las imágenes de origen, la extracción y las comprobaciones realizadas.
