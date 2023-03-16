# Instructions 

Utilize isolated Python enviroment (venv).
This is a standrad Sphinix project with added document generations extensions. 


### To start auto-build serve 

This will start the web serve.
Sensitive to changes and changes can be previewed live in localhost:8000

```
sphinx-autobuild docs/source/ docs/build/_web
```

### To build .docx 
Run the following command to generate .docx file in `docs/build/_docx`

```
sphinx-build -b docx docs/source/ docs/build/_docx
```
### To build .pdf

Run the following command to generate .pdf file in `docs/build/_rinoh`
```
sphinx-build -b rinoh docs/source/ docs/build/_rinoh
```
## Know Issues 

Tall Image Resizing loop in Rinoh [Issue](https://github.com/brechtm/rinohtype/issues/351)
> Setting Screenshot image Size 500X250 will allow you to get arround this

Using a image resizing tool like [magick](https://imagemagick.org) will do the trick.
```
convert img_01.png -resize 500x250 -normalize -density 180  img_01_size.png
```
Or relaying on html image emmbeddings will be the way to go.