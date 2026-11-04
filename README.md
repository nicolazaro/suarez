# Francisco Suárez en la Biblioteca Argentina de Rosario

Material expositivo para la ponencia de Nicolás A. Lázaro en el IV Simposio «Fuentes, Figuras y Temas del Renacimiento» (Rosario, 6 de noviembre de 2026).

## Publicar en GitHub Pages

1. Crear un repositorio público (por ejemplo, `suarez-ba`) y subir todo el contenido de esta carpeta a la raíz.
2. En el repositorio: Settings → Pages → «Deploy from a branch» → rama `main`, carpeta `/ (root)`.
3. A los pocos minutos el sitio queda en `https://USUARIO.github.io/suarez-ba/`.

## Tarjetas con QR

Con el sitio ya publicado, abrir `https://USUARIO.github.io/suarez-ba/qr.html`. La página genera los dieciséis códigos a partir de su propia dirección y los compone en tarjetas A6 (cuatro por hoja A4, cuatro hojas en total), con número de orden, número de lista, signatura, título breve y pie de imprenta. Cada código lleva a `…/#libro-NN`.

Para imprimir en papel de 125 g: tamaño A4, escala 100 %, márgenes «Ninguno», sin encabezados ni pies del navegador y con «Gráficos de fondo» activado. Recortar por la línea punteada. Antes de imprimir las cuatro hojas, conviene probar una y escanear un código.

## Uso durante la exposición

- En el celular, la página se lee de corrido; cada QR abre directamente la ficha del ejemplar.
- En la computadora conectada al proyector: flechas ← → (o AvPág/RePág) para pasar de una sección a otra, **P** para el modo proyección (letra más grande), **F** para pantalla completa.
- La proyección no se sincroniza con los celulares: cada persona navega por su cuenta.

## Editar contenidos

Los textos de las fichas están en `data.py`; las secciones generales, en `build.py`. Después de editar, regenerar con `python3 build.py`. También se puede editar `index.html` directamente.
