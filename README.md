# Instructions 

Utilize isolated Python environment (venv).
This is a standard Sphinix project with added document generations extensions. 


### To start auto-build serve 

This will start the web serve.
Sensitive to changes and changes can be previewed live in localhost:8000

```bash
sphinx-autobuild docs/source/ docs/build/_web
```

### To build Single Page HTML

```bash
sphinx-build -b singlehtml docs/source/ docs/build/_singleHtml
```

### To build .docx 
Run the following command to generate .docx file in `docs/build/_docx`

```bash
sphinx-build -b docx docs/source/ docs/build/_docx
```
Otherwise you can use utility like [Pandoc](https://pandoc.org).

```bash
sphinx-build -b singlehtml docs/source/ docs/build/_singleHtml
cd docs/build/_singleHtml
pandoc -o index.docx index.html
```
Pandoc utility can be used with [python wrapper](#pypandoc-workflow)

### To build .pdf

Run the following command to generate .pdf file in `docs/build/_rinoh`
```bash
sphinx-build -b rinoh docs/source/ docs/build/_rinoh
```

### Pypandoc Workflow
This is method uses a [Pypandoc](https://github.com/JessicaTegner/pypandoc) wrapper for[Pandoc](https://pandoc.org)

> Generates the file at ./docs/build/_pandoc

```bash
cd ./docs/source/
python app.py
```

## Know Issues 

Tall Image Resizing loop in Rinoh [Issue](https://github.com/brechtm/rinohtype/issues/351)
> Setting Screenshot image Size 500X250 will allow you to get around this

Using a image resizing tool like [magick](https://imagemagick.org) will do the trick.

```bash
convert img_01.png -resize 500x250 -normalize -density 180  img_01_size.png
```

Or relaying on html image embeddings will be the way to go.

```bash
pandoc week_01.md -f markdown -o Lab_Log_Book_W1761889.docx

```