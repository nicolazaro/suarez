import html, re
from data import BOOKS
E=html.escape
def short(t):
    s=t.split(",")[0].split(". Tomo")[0]
    return s
def year(i): return i.split(",")[-1].strip()

fichas=[]
for b in BOOKS:
    o=b['o']; nid=f"libro-{o:02d}"
    prev = f"libro-{o-1:02d}" if o>1 else "indice"
    nxt  = f"libro-{o+1:02d}" if o<16 else "recapitulacion"
    com="".join("<p>"+re.sub(r"\*(.+?)\*", r"<i>\1</i>", E(c))+"</p>" for c in b['com'])
    fichas.append(f'''
<section class="slide ficha" id="{nid}" aria-labelledby="{nid}-t">
  <div class="col">
    <header class="ficha-cab">
      <span class="orden" aria-label="Ejemplar número {o}">{o}</span>
      <p class="refs">Lista n.º {b['n']}<br>Signatura {E(b['sig'])}<br><span class="sede">{E(b['sede'])}</span></p>
    </header>
    <h2 id="{nid}-t" class="titulo-libro">{E(b['t'])}</h2>
    <p class="pie">{E(b['imp'])}</p>
    <div class="comentario">{com}</div>
    <details class="asiento">
      <summary>Asiento del catálogo</summary>
      <p>{E(b['cat'])}</p>
    </details>
    <nav class="paso" aria-label="Navegación entre ejemplares">
      <a href="#{prev}">Anterior</a>
      <a href="#indice">Índice</a>
      <a href="#{nxt}">Siguiente</a>
    </nav>
  </div>
</section>''')

indice="".join(f'<li><a href="#libro-{b["o"]:02d}"><span class="i-num">{b["o"]}</span><span class="i-tit"><i>{E(short(b["t"]))}</i></span><span class="i-anio">{year(b["imp"])}</span></a></li>' for b in BOOKS)

page=f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="theme-color" content="#140b07">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Francisco Suárez en la Biblioteca Argentina de Rosario</title>
<meta name="description" content="Exposición bibliográfica: dieciséis ediciones de Francisco Suárez (1592–1625) en la Biblioteca Argentina Dr. Juan Álvarez. IV Simposio «Fuentes, Figuras y Temas del Renacimiento», Rosario, 6 de noviembre de 2026.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📜</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="estilo.css">
</head>
<body>
<a class="saltar" href="#indice">Ir al índice de ejemplares</a>

<section class="slide portada" id="inicio" aria-label="Portada">
  <div class="portada-caja">
    <p class="p-evento">IV Simposio «Fuentes, Figuras y Temas del Renacimiento»</p>
    <p class="p-sup">Exposición bibliográfica plenaria</p>
    <h1>Francisco Suárez en la Biblioteca Argentina de Rosario</h1>
    <p class="p-sub">Comentarios sobre sus ediciones monumentales renacentistas</p>
    <p class="p-fecha">Viernes 6 de noviembre, 10:00 hs.</p>
    <p class="p-autor">Nicolás A. Lázaro<br><span>Universidad Católica de Santa Fe y Universidad Nacional de Rosario</span></p>
    <p class="p-lugar">Biblioteca Argentina Dr. Juan Álvarez<br><span>Pasaje Dr. Álvarez 1550, Rosario</span></p>
    <a class="empezar" href="#introduccion">Comenzar</a>
  </div>
</section>

<section class="slide" id="introduccion" aria-labelledby="t-intro">
  <div class="col">
    <h2 id="t-intro">Dieciséis volúmenes, 1592–1625</h2>
    <p>La documentación del proyecto <i>Un Renacimiento Rosarino</i> mencionaba «una veintena de volúmenes teológicos de Francisco Suárez». El relevamiento de la base documental permite precisar la cifra: son dieciséis, impresos entre 1592 y 1625.</p>
    <p>No nos proponemos exponer la doctrina suareciana, sino interrogar a estos libros en cuanto libros: qué ediciones son, de dónde proceden, qué lugar ocupan en la trayectoria de su autor y qué dicen sobre la circulación europea de la segunda escolástica y sobre la formación de las colecciones rosarinas.</p>
    <p class="nota">Sus fechas los sitúan en el umbral del Barroco. Si los traemos a un simposio sobre el Renacimiento es porque la segunda escolástica es una de sus herencias: se valió de la filología, de la imprenta y de las redes que el Renacimiento había hecho posibles.</p>
  </div>
</section>

<section class="slide" id="suarez" aria-labelledby="t-suarez">
  <div class="col">
    <h2 id="t-suarez">Francisco Suárez, 1548–1617</h2>
    <p>Nació en Granada y murió en Lisboa. Jesuita desde 1564, enseñó filosofía y teología en las principales casas de estudio de la Compañía y fue llamado <i>Doctor Eximius</i>. Su obra se suele leer como gozne entre el saber medieval y el pensamiento moderno.</p>
    <ol class="sedes">
      <li><span>1561–1570</span>Salamanca: estudios de derecho, ingreso en la Compañía y formación</li>
      <li><span>1571–1580</span>Segovia, Valladolid y Ávila: primeras cátedras</li>
      <li><span>1580–1585</span>Colegio Romano</li>
      <li><span>1585–1593</span>Alcalá de Henares</li>
      <li><span>1593–1597</span>Salamanca</li>
      <li><span>1597–1617</span>Coimbra: cátedra de Prima de Teología</li>
    </ol>
    <p class="nota">Cada ficha indica la sede en la que se gestó la obra. Casi siempre, lo que Suárez explicaba en el aula llegaba a la imprenta años después.</p>
  </div>
</section>

<section class="slide" id="monumentales" aria-labelledby="t-mon">
  <div class="col">
    <blockquote class="horacio" lang="la"><p>Exegi monumentum aere perennius</p><cite>Horacio, <i>Odas</i> III, 30</cite></blockquote>
    <h2 id="t-mon">¿Por qué «monumentales»?</h2>
    <dl class="sentidos">
      <dt>Por su materialidad</dt><dd>Grandes infolios en serie, de muchas páginas y a dos columnas.</dd>
      <dt>Por la empresa editorial</dt><dd>Los Cardon de Lyon reimprimieron a Suárez volumen por volumen durante más de veinte años, incluso después de su muerte.</dd>
      <dt>Por la arquitectura doctrinal</dt><dd>Lo monumental es también el edificio de comentarios y tratados que estos volúmenes materializan.</dd>
      <dt>Por su función de <i>monumenta</i></dt><dd>Son testimonios que permiten reconstruir dos épocas: la de su impresión y la de su llegada a Rosario.</dd>
    </dl>
  </div>
</section>

<section class="slide" id="indice" aria-labelledby="t-ind">
  <div class="col ancha">
    <h2 id="t-ind">Los ejemplares</h2>
    <p class="nota">El número coincide con la tarjeta que acompaña a cada libro en la sala. Escaneá su código QR o elegilo en esta lista.</p>
    <ol class="indice">{indice}</ol>
  </div>
</section>
{''.join(fichas)}

<section class="slide" id="recapitulacion" aria-labelledby="t-rec">
  <div class="col">
    <h2 id="t-rec">El conjunto</h2>
    <dl class="sentidos">
      <dt>Un fondo casi enteramente lionés</dt><dd>Trece de los dieciséis volúmenes son de Lyon. Ninguno es una princeps ibérica: el fondo documenta la difusión europea de Suárez.</dd>
      <dt>Series completas o casi completas</dt><dd>Los cuatro tomos del <i>De virtute et statu religionis</i>, las dos partes del <i>De gratia</i> disponibles en 1620 y los comentarios a la Tercera Parte, salvo el tomo II. Todo sugiere que el conjunto se adquirió como corpus.</dd>
      <dt>Más teología que filosofía política</dt><dd>Está el <i>De legibus</i>, pero no las <i>Disputationes metaphysicae</i> ni la <i>Defensio fidei</i>.</dd>
      <dt>Velocidad de circulación</dt><dd>Lyon reimprimía a Suárez uno o dos años después de las princeps: las primeras piezas son contemporáneas de su docencia.</dd>
    </dl>
    <p class="nota">La pregunta que queda abierta es cómo, cuándo y desde qué biblioteca llegó este corpus a Rosario. Responderla requiere examinar las marcas de procedencia de cada ejemplar.</p>
  </div>
</section>

<section class="slide cierre" id="cierre" aria-labelledby="t-cie">
  <div class="col">
    <h2 id="t-cie"><i lang="la">Monumentum</i>, de <i lang="la">monere</i></h2>
    <p>Recordar, advertir, hacer pensar. Un monumento solo cumple su función cuando alguien lo visita; sin lectores, se vuelve un objeto mudo en un depósito.</p>
    <p>Exhibir hoy estos libros no tiene como fin venerarlos como reliquias, sino devolverles la palabra: que vuelvan a ser consultados, estudiados y discutidos.</p>
    <footer class="creditos">
      <p>Nicolás A. Lázaro, <a href="mailto:nicolazaro@ucsf.edu.ar">nicolazaro@ucsf.edu.ar</a>, <a href="https://orcid.org/0000-0002-6066-332X">ORCID 0000-0002-6066-332X</a></p>
      <p>Proyecto <i>Un Renacimiento Rosarino</i>, Centro «Studium», Facultad de Humanidades y Artes, UNR, con la Facultad de Ciencias Médicas, la Facultad de Arquitectura, Planeamiento y Diseño (UNR) y la Biblioteca Argentina Dr. Juan Álvarez.</p>
      <p>Material elaborado con asistencia de IA generativa (Claude, Anthropic), revisado por el autor. Véase la declaración completa en la ponencia.</p>
      <p><a href="#inicio">Volver al inicio</a></p>
    </footer>
  </div>
</section>

<p class="ayuda" aria-hidden="true">Flechas para avanzar, P para el modo proyección, F para pantalla completa</p>
<script src="navegacion.js"></script>
</body>
</html>'''
open("index.html","w").write(page)

# QR page: tarjetas A6 (cuatro por hoja A4) para imprimir en 125 g
def tarjeta(b):
    return f"""<article class="tarjeta">
  <header><p>IV Simposio «Fuentes, Figuras y Temas del Renacimiento»</p><p>Francisco Suárez en la Biblioteca Argentina</p></header>
  <div class="cuerpo">
    <div class="datos"><p class="t-num">{b["o"]}</p><p class="t-ref">Lista n.º {b["n"]}<br>{b["sig"]}</p></div>
    <div class="qr" data-id="libro-{b["o"]:02d}" role="img" aria-label="Código QR del ejemplar {b["o"]}"></div>
  </div>
  <p class="t-tit"><i>{E(short(b["t"]))}</i><br>{E(b["imp"])}</p>
  <p class="t-inv">Escaneá el código para leer la ficha de este ejemplar</p>
</article>"""
hojas="".join('<section class="hoja">'+"".join(tarjeta(x) for x in BOOKS[i:i+4])+'</section>' for i in range(0,16,4))
css="""
@page { size: A4 portrait; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; background: #e9e4de; font-family: "Playfair Display", Georgia, serif; color: #241510; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.instr { max-width: 44rem; margin: 1.5rem auto; padding: 0 1rem; line-height: 1.5; }
.instr code { font-size: .85em; }
.hoja { width: 210mm; height: 297mm; margin: 0 auto 1rem; background: #fff; display: grid; grid-template-columns: 105mm 105mm; grid-template-rows: 148.5mm 148.5mm; break-after: page; }
.tarjeta { padding: 0 8mm 7mm; display: flex; flex-direction: column; outline: .2mm dashed #b9b0a6; outline-offset: -.1mm; overflow: hidden; }
.tarjeta header { background: #140b07; color: #f4ede6; margin: 0 -8mm 6mm; padding: 4mm 8mm 3.5mm; font-size: 7.5pt; line-height: 1.35; }
.tarjeta header p { margin: 0; }
.tarjeta header p + p { font-style: italic; color: #e3a874; }
.cuerpo { display: flex; flex-direction: column; }
.datos { display: flex; align-items: flex-end; gap: 4mm; }
.t-num { font-size: 60pt; font-weight: 700; line-height: .8; margin: 0; color: #b4561c; }
.t-ref { font-size: 9.5pt; line-height: 1.35; margin: 0; color: #5b4a40; }
.qr { width: 60mm; height: 60mm; flex: none; margin: 6mm auto 0; }
.qr img, .qr canvas { width: 100% !important; height: 100% !important; image-rendering: pixelated; }
.t-tit { margin: 5mm 0 0; font-size: 10.5pt; line-height: 1.3; border-top: .3mm solid #b4561c; padding-top: 3mm; }
.t-inv { margin: auto 0 0; font-size: 8.5pt; color: #5b4a40; }
@media print { html, body { background: #fff; } .instr { display: none; } .hoja { margin: 0; } }
"""
qr=f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tarjetas con QR de los ejemplares</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<div class="instr">
<p>Cuatro tarjetas A6 por hoja A4, pensadas para papel de 125 g. Imprimí desde el sitio ya publicado: tamaño A4, escala 100 %, márgenes «Ninguno», sin encabezados ni pies del navegador y con «Gráficos de fondo» activado para que salga la franja oscura. Recortá por la línea punteada.</p>
<p>Cada código lleva a <code id="base"></code><code>#libro-NN</code>.</p>
</div>
{hojas}
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<script>
var base = location.href.split("#")[0].replace(/qr\\.html.*$/, "");
document.getElementById("base").textContent = base;
document.querySelectorAll(".qr").forEach(function(el){{
  new QRCode(el, {{ text: base + "#" + el.dataset.id, width: 512, height: 512, colorDark: "#140b07", colorLight: "#ffffff", correctLevel: QRCode.CorrectLevel.Q }});
}});
</script></body></html>"""
open("qr.html","w").write(qr)
print("ok")
