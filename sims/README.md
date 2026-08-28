# Casa Sim — constructor de casas (Three.js)

Juego web de construcción de casas inspirado en el modo Construir/Comprar de **Los Sims 1**.
Todo en un solo archivo: `index.html`. Se abre en el navegador, sin build ni servidor.

> **No necesita internet.** Three.js viene incluido dentro del archivo y no hay
> tipografías ni recursos externos: cero pedidos a otros dominios. Anda igual
> abriéndolo con doble click, servido en una LAN o subido a cualquier hosting.

Para ponerlo a disposición de un grupo (aula, taller), ver **[COMO-PUBLICAR.md](COMO-PUBLICAR.md)**:
GitHub Pages, servidor en la red local (`servidor-lan.py`) o repartir el archivo.

## Controles

| Acción | Cómo |
|---|---|
| Colocar | Click izquierdo |
| Paredes / pisos en línea o rectángulo | Click y arrastrar (la cinta amarilla muestra la medida) |
| Seleccionar y mover lo ya colocado | Herramienta 🖐 Mover (`V`): click para seleccionar, arrastrar para mover |
| Rotar | `R` (90°) · `Shift+R` (45°) — o los botones ↺ ↻ 45° del panel |
| Pintar / llenar un ambiente entero | `Shift` + click con la brocha o con un solado |
| Deshacer / rehacer | `Ctrl+Z` / `Ctrl+Y` (también ↶ ↷ arriba) |
| Mover la cámara | Arrastrar con el botón derecho, flechas o `WASD`, o llevar el cursor al borde de la pantalla |
| Rotar la cámara 90° | `,` y `.` (o `Q` / `E`, o los botones de la brújula) |
| Zoom | Rueda del mouse o `+` / `-` |
| Demoler | `X` o `Supr` (también la herramienta 💥) |
| Cuadrícula sí/no | `G` o el botón ▦ del panel Vista |
| Cambiar de piso | `1` planta baja · `2` piso 1 |

## Qué se puede hacer

**Construir**
- Paredes rectas y **en diagonal a 45°**, cercos de jardín y cuatro aberturas: puerta,
  ventana, **ojo de buey** (redonda, con el agujero calado de verdad) y **puerta ventana**
  de dos hojas vidriadas. Todas dejan pasar el sol y proyectan sombras reales.
- **Pintura y empapelado por cara de pared**: 21 revestimientos — lisos, papel a rayas,
  de flores, de **nubes** (tipo cuarto de Woody), de estrellas, ladrillo visto, madera y
  azulejos. Cada lado del muro se pinta aparte, y con **Shift** se pinta el ambiente entero:
  por dentro el cuarto completo, por fuera la vuelta entera de la casa.
- Nueve solados con textura propia (se ve el damero, las vetas de la madera, las juntas de
  la vereda y las piedras del camino). Con **Shift** se llena de una un ambiente cerrado.
- Escaleras que abren solas el hueco en la losa de arriba.

**Comprar**
- Asientos, mesas, cocina completa, baño (inodoro, bidet, lavamanos, ducha, bañera),
  dormitorio (cama de 1 y 2 plazas, cama infantil, cuna, placard), electrodomésticos,
  lámparas y plantas de interior.
- **Exterior**: árboles, pinos, arbustos, tulipanes, canteros de flores, buzón, farol de
  jardín, reposera, parrilla, banco, mesa con sombrilla y pileta.

**Vista**
- Dos plantas, con paredes **Altas / Auto / Cortadas / Bajas**. En modo **Auto** bajan solas
  las paredes que taparían la habitación desde el ángulo actual de la cámara, como en el Sims.
- Sombras de contacto bajo los muebles (se pueden apagar).
- Contorno de resaltado al pasar el mouse, para saber qué vas a mover o demoler.
- Ciclo de día y noche con reloj y velocidades: al anochecer las lámparas se encienden solas.

**Guardar**: 💾 guarda la casa en el navegador (`localStorage`) y 📂 la vuelve a cargar.
Con **⬇** la bajás como archivo `.json` (para entregarla o llevarla a otra máquina) y
con **⬆** abrís cualquiera de esos archivos.

Algunos objetos se apoyan sobre otros (el microondas sobre la mesada, la lámpara sobre la mesa de
luz, la planta chica sobre una mesa) y otros se cuelgan de la pared o del techo.

Desde la consola del navegador hay un hook para trastear: `casaSim.setTime(22*60)`,
`casaSim.state`, `casaSim.undo()`, etc.
