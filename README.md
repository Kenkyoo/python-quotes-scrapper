# Quotes Scrapper

Aplicación de escritorio para extraer citas de páginas web. Detecta automáticamente texto entre comillas y lo exporta a CSV.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![tkinter](https://img.shields.io/badge/UI-tkinter-lightgrey)

## Características

- Interfaz gráfica simple con campo de URL y área de resultados
- Extrae citas entre comillas (`"`, `'`, `"`, `"`) de entre 20 y 200 caracteres
- Elimina duplicados automáticamente
- Exporta los resultados a `quotes.csv`
- Muestra el total de citas encontradas en la barra de estado

## Estructura

```
quotes-scrapper/
├── app.py            # Interfaz gráfica (tkinter)
├── scrapper.py       # Lógica de scraping
├── requirements.txt
└── README.md
```

## Instalación

```bash
git clone https://github.com/tu-usuario/quotes-scrapper.git
cd quotes-scrapper
pip install -r requirements.txt
```

> tkinter viene incluido con Python. Si usás Linux y no lo tenés:
> ```bash
> sudo apt install python3-tk
> ```

## Uso

```bash
python app.py
```

1. Pegá la URL en el campo de texto
2. Presioná **Buscar** o **Enter**
3. Las citas aparecen en el panel de resultados
4. Se genera `quotes.csv` en el directorio actual

## Sitios compatibles

| Sitio | URL |
|-------|-----|
| Quotes to Scrape | https://quotes.toscrape.com/ |
| Goodreads | https://www.goodreads.com/quotes |
| Wikipedia | https://www.wikipedia.org/ |

> El resultado depende de cómo cada sitio estructura su HTML. Páginas con contenido dinámico (JavaScript) pueden no devolver resultados.

## Dependencias

Ver `requirements.txt`. Las principales:

- `requests` — peticiones HTTP
- `beautifulsoup4` — parsing de HTML
- `pandas` — exportación a CSV
