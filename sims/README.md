# Casa Sim — constructor de casas (Three.js)

Juego web de construcción de casas inspirado en el modo Construir/Comprar de **Los Sims 1**.
Todo en un solo archivo: `index.html`. Se abre en el navegador, sin build ni servidor.

> Carga Three.js r160 desde unpkg, así que la primera vez necesita conexión a internet.

## Controles

| Acción | Cómo |
|---|---|
| Colocar | Click izquierdo |
| Paredes / pisos en línea o rectángulo | Click y arrastrar |
| Rotar el objeto antes de colocarlo | `R` |
| Mover la cámara | Arrastrar con el botón derecho, flechas o `WASD` |
| Rotar la cámara 90° | `,` y `.` (o `Q` / `E`, o los botones de la brújula) |
| Zoom | Rueda del mouse o `+` / `-` |
| Demoler | `X` o `Supr` (también está la herramienta 💥) |
| Cancelar la herramienta | `Esc` |
| Cambiar de piso | `1` planta baja · `2` piso 1 |

## Qué se puede hacer

- **Construir**: paredes sobre la cuadrícula, puertas y ventanas (dejan pasar el sol y proyectan
  sombras reales), seis tipos de piso, escaleras que abren solas el hueco en la losa de arriba.
- **Comprar**: asientos, mesas, cocina completa, baño (inodoro, bidet, lavamanos, ducha, bañera),
  dormitorio (cama de 1 y 2 plazas, cama infantil, cuna, placard), electrodomésticos
  (tele, computadora, equipo de música), lámparas y plantas.
- **Dos pisos**, con vista de paredes altas / cortadas / bajas.
- **Ciclo de día y noche** con reloj y velocidades: al anochecer las lámparas se encienden solas
  (o se fuerzan con los botones Encendidas / Apagadas).
- **Guardar y cargar** la casa en el navegador (`localStorage`).

Algunos objetos se apoyan sobre otros (el microondas sobre la mesada, la lámpara sobre la mesa de
luz, la planta chica sobre una mesa) y otros se cuelgan de la pared o del techo.

Desde la consola del navegador hay un hook para trastear: `casaSim.setTime(22*60)`, `casaSim.state`, etc.
