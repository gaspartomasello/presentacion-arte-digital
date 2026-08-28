# Cómo poner Casa Sim a disposición de los alumnos

`index.html` es **un solo archivo que no le pide nada a internet**: Three.js viene
adentro y no hay tipografías, imágenes ni scripts externos. Verificado con todo
el tráfico externo bloqueado: cero pedidos a otros dominios.

Eso importa mucho en una red escolar con filtro: el único dominio que tiene que
estar permitido es el del lugar donde subas la página. Si además el filtro
bloquea todo, siguen funcionando la opción LAN y la de repartir el archivo.

---

## Opción 1 — Online con GitHub Pages (la más cómoda)

El repositorio ya está en GitHub, así que es gratis y sale en dos minutos.

1. Llevá esta rama a `main` (merge o pull request).
2. En GitHub: **Settings → Pages**.
3. En *Source* elegí **Deploy from a branch**, rama **main**, carpeta **/ (root)**, y **Save**.
4. Esperá uno o dos minutos. La dirección para los alumnos queda:

       https://gaspartomasello.github.io/presentacion-arte-digital/sims/

**Probalo desde la escuela antes de la clase**: entrá a esa dirección con el
celular conectado al wifi del colegio. Si abre, ya está.

Si el filtro bloquea `github.io`, probá subir la misma carpeta a otro lado. Es
arrastrar y soltar, sin cuenta ni configuración:

| Servicio | Dirección | Cómo |
|---|---|---|
| Netlify Drop | app.netlify.com/drop | Arrastrás la carpeta `sims`, te da una URL `*.netlify.app` |
| Cloudflare Pages | pages.cloudflare.com | Subís la carpeta, te da `*.pages.dev` |
| Vercel | vercel.com | Igual, te da `*.vercel.app` |
| Neocities | neocities.org | Hosting simple de páginas, `*.neocities.org` |

No puedo verificar desde acá qué dominios habilita el wifi de la escuela, así que
la única forma segura es probar una dirección y, si no abre, pasar a la siguiente.
Conviene tener elegida de antemano una alternativa.

---

## Opción 2 — En la red del aula (LAN), sin internet

Sirve cuando no hay internet o está todo bloqueado. Una sola computadora hace de
servidor y las demás entran por la red.

En la compu del docente, dentro de esta carpeta:

```bash
python3 servidor-lan.py
```

En Windows alcanza con hacer doble click en **`servidor-lan.bat`**.

El programa imprime en pantalla la dirección que tienen que escribir los alumnos,
algo como `http://192.168.1.45:8080/`. Se corta con `Ctrl+C`.

Dos cosas a tener en cuenta:

- Todas las máquinas tienen que estar en la **misma red** (mismo wifi o mismo switch).
- Si no entra nadie, casi siempre es el **firewall de Windows**: cuando aparezca el
  cartel, permitile a Python el acceso a redes privadas. Si el puerto está ocupado,
  usá otro: `python3 servidor-lan.py 8081`.

---

## Opción 3 — Repartir el archivo (siempre funciona)

Como el juego es un archivo suelto y autosuficiente, podés pasarles `index.html`
por Classroom, mail, Drive o pendrive. Lo bajan, le hacen doble click y juegan,
con o sin internet. Conviene renombrarlo a `casa-sim.html` para que se entienda.

Es la salida más robusta si el filtro de la escuela no deja pasar nada.

---

## Para tener en cuenta en el aula

- **Dónde quedan las casas**: el botón 💾 guarda en el navegador de esa máquina
  (`localStorage`). Es por computadora y por navegador, así que si los alumnos
  cambian de máquina no se llevan la casa, y si el laboratorio borra los perfiles
  al reiniciar se pierde. Si necesitás que entreguen el trabajo, decime y agrego
  un botón para **bajar la casa como archivo** y otro para volver a abrirla.
- **Máquinas con poca potencia**: el juego usa sombras en tiempo real. Si va lento
  en las netbooks, apagá *Sombras de contacto* en el panel Vista y bajá el zoom.
  También puedo agregar un modo de calidad baja.
- **Navegador**: cualquiera moderno con WebGL (Chrome, Edge, Firefox). Anda con
  mouse y teclado; todavía no está adaptado a pantalla táctil.
