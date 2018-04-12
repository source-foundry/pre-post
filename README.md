# pre-post

pre-post is a web font specimen sheet that renders two versions of web fonts simultaneously for the comparison of changes in font designs between builds.  It is built with Flask + Jinja2 templates (Python).

It supports the following:

- Pre/post pangram string with selector for modification of displayed text size
- Pre/post specimens of Basic Latin set glyphs
- Pre/post waterfall of Basic Latin alphabetic and numeral glyphs
- Pre/post test source code specimen - dark on light
- Pre/post test source code specimen - light on dark

The text specimens are defined in HTML templates and can be easily modified to address other needs.  See the [Modify Text Specimen](#modify-text-specimen) documentation below for details.

## Install

Clone the git source repository:

```
$ git clone https://github.com/source-foundry/pre-post.git
```

Navigate to the pre-post directory:

```
$ cd pre-post
```

## Usage

#### Add fonts for comparison

Place the "pre" font version files in the directory on the path `static/fonts/pre`.  Place the "post" font version files in the directory on the path `static/fonts/post`.

#### Start Flask server

Start the Flask server with the shell script included in the source repository:

```
$ ./run.sh
```

The server runs on the URL `http://localhost:5000`

#### Define your font comparisons in the URL

The URL string can be used to define font variants and sizes for comparison using the following syntax:

```
http://localhost:5000/[woff|woff2]/(variant)/(size)
```

Variant is an optional value.  The regular variant is displayed by default when variant is not specified.  

Size is an optional value.  A range of sizes that include 8, 9, 10, 11, 12, 13, 14, 16, 20, 24, 30, 36 are displayed by default.

#### Define variant

Define other variants in the URL as follows (woff2 builds shown, replace with `woff` for woff builds):

##### Bold variant

```
http://localhost:5000/woff2/bold/
```

##### Italic variant

```
http://localhost:5000/woff2/italic/
```

##### Bold italic variant

```
http://localhost:5000/woff2/bolditalic/
```

#### Define size

Add a font size to your URL to exclude all other default sizes in the specimen.  Acceptable values include 8, 9, 10, 11, 12, 13, 14, 16, 20, 24, 30, 36, 48, 60, 72, 90.

##### Display regular variant at size 36

```
http://localhost:5000/woff2/regular/36/
```

##### Display bold variant at size 24

```
http://localhost:5000/woff2/bold/24/
```

## Modify Template for Other Projects

This project was created for the development of the [Hack typeface](https://github.com/source-foundry/Hack).  It can be easily adapted to other typeface project needs.  The text specimens are defined in HTML using a Jinja2 template.  This template can be edited and rendered with the approach  described above.

The Jinja2 template is on the repository path: `templates/specimen.html`.  Please refer to the Jinja2 documentation for additional details in order to address any modification needs.

The web fonts (including web font paths) are defined in the CSS file located on the repository path `static/css/app.css`.  Change all Hack-specific values to appropriate paths for your web fonts. 

## License

[MIT License](LICENSE)



