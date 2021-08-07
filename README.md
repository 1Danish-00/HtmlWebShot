# HtmlWebShot  
[![PyPI version](https://badge.fury.io/py/htmlwebshot.svg)](https://badge.fury.io/py/htmlwebshot)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4ffdde720ca542a2973b3a79da61bd70)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=1Danish-00/HtmlWebShot&amp;utm_campaign=Badge_Grade)
[![Licence](https://img.shields.io/github/license/1Danish-00/HtmlWebShot.svg)](https://github.com/1Danish-00/HtmlWebShot/blob/main/LICENSE)  

A python3 package which Can Create Images From url, Html-CSS, Svg and from any readable file and texts with many setup features.

## Setup & Installation  
* Install HtmlWebShot:  
   ```bash
   $ pip3 install htmlwebshot
   ```  
* Install wkhtmltopdf:  
  
  * Debian/Ubuntu:  
      ```bash
      $ apt-get install wkhtmltopdf -y  
      ```  
  * MacOs:  
      ```bash
      $ brew install homebrew/cask/wkhtmltopdf
      ```  
  * Alternative Support  
      ```
      $ wget https://github.com/1Danish-00/HtmlWebShot/raw/main/script.sh && sh script.sh
      ```

## Usage  

###  Import & Instantiate  
```python
from htmlwebshot import WebShot
shot = WebShot()
```  

##### Multiple Arguments  

* `size`: (int , int) : tuple : height, width default: full-screen
* `quality`: int : (between 0-100)
* `delay`: float : delay time to load page
* `flags`: list : [know More](#flags-uses)
* `params`: dict : [know more](#available-params)
* `config`: path setup [know more](#config-path)

### Simple Method  

>  Using Url
```py
shot.create_pic(url="https://google.com")
```
>  Using Html File
```py
shot.create_pic(html="myfile.html", output="picture.jpg")
```
>  Using Html with CSS  
  >>  via files
   ```py
   shot.create_pic(html="myfile.html", css="background.css", output="picture.jpg")
   ```
  >>  via string
   ```py
   html = """<h1> Hello World </h1>
<p>Write something about the world.</p>"""
   css = "body {background: pink;} p {color: red;}" 

   shot.create_pic(html=html, css=css, output="picture.jpg")
   ```
>  Using Svg Or Any Other Readable File/Text
```py
shot.create_pic(other="violin.svg", output="picture.jpg")
```
```py
text = "What should I write here???"
shot.create_pic(other=text, size=(100,200))
```  


You can use with async too  
```py
await shot.create_pic_async( # parameters are same for both
```  

### Some Examples  

```py
from htmlwebshot import WebShot
shot = WebShot()

shot.size = (110, 270)
shot.quality = 80  # maximum 100

html = """<h1> Hello World </h1>
<p>Write something about the world.</p>"""
css = "body {background: pink;} p {color: red;}"

shot.create_pic(html=html, css=css, output="picture.jpg")
```
<details>
<summary> Click Here To See Output Image Of Above Code. </summary>
<img src="https://telegra.ph/file/7e266bf0db726865a8a00.jpg" alt="sample1"/>
</details>

```py
from htmlwebshot import WebShot
shot = WebShot()

shot.quality = 100
shot.params = {"--crop-x":300, "--crop-w": 400}

shot.create_pic(html="profile.html", css="profile.css")
```
<details>
<summary> Click Here To See Output Image Of Above Code. </summary>
<img src="https://telegra.ph/file/3d847855e8e8f1338cbad.png" alt="sample2"/>
</details>
<br>
<details>
<summary> Click For More Examples </summary>

```py
from htmlwebshot import WebShot
shot = WebShot()

shot.quality = 85
shot.flags = ["--enable-javascript"]

shot.create_pic(html="jsgraph.html")
```

<details>
<summary> Click Here To See Output Image Of Above Code. </summary>
<img src="https://telegra.ph/file/eb08c45ffd3a35a670806.png" alt="sample4"/>
</details>

```py
from kk.htmlwebshot import WebShot
shot = WebShot()

shot.flags = ["--quiet"]
shot.quality = 100

shot.create_pic(other="violin.svg", size=(500,600))
```

<details>
<summary> Click Here To See Output Image Of Above Code. </summary>
<img src="https://telegra.ph/file/a5183063ba44c5b411499.png" alt="sample3"/>
</details>

</details>

###  Flags Uses  

<details>
<summary> Click Here To Check All Flags:</summary>  

* `--quiet`: Be less verbose
* `--disable-smart-width`: To force size to be accurate
* `--custom-header-propagation`: Add HTTP headers specified by flag `--custom-header` for each resource request
* `--no-custom-header-propagation`: Don't Add HTTP headers specified by flag `--custom-header` for each resource request
* `--disable-javascript`: Don't allow web pages to run javascript
* `--enable-javascript`: Allow web pages to run javascript
* `--proxy-hostname-lookup`: Use the proxy for resolving hostnames
* `--stop-slow-scripts`: Stop slow running javascripts
* `--no-stop-slow-scripts`: Don't Stop slow running javascripts
</details>

```py
from htmlwebshot import WebShot
shot = WebShot()
shot.flags = ["--quiet", "--enable-javascript", "--no-stop-slow-scripts"]
```

### Available Params  

<details>
<summary> Click Here To Check All Params options:</summary>  

* `--bypass-proxy-for`: _`<value>`_ Bypass proxy for host (repeatable)
* `--cookie`: _`<name>` `<value>`_ Set an additional cookie (repeatable), value should be url encoded.
* `--cookie-jar`: _`<path>`_ Read and write cookies from and to the supplied cookie jar file
* `--crop-h`: _`<int>`_ Set height for cropping
* `--crop-w`: _`<int>`_ Set width for cropping
* `--crop-x`: _`<int>`_ Set x coordinate for cropping
* `--crop-y`: _`<int>`_ Set y coordinate for cropping
* `--custom-header`: _`<name>` `<value>`_ Set an additional HTTP header (repeatable)
* `--encoding`: _`<encoding>`_ Set the default text encoding, for input
* `--format`: _`<format>`_ Output file format
* `--minimum-font-size`: _`<int>`_ Minimum font size
* `--password`: _`<password>`_ HTTP Authentication password
* `--post`: _`<name>` `<value>`_ Add an additional post field (repeatable)
* `--post-file`: _`<name> <path>`_ Post an additional file (repeatable)
* `--proxy`: _`<proxy>`_ Use a proxy
* `--run-script`: _`<js>`_ Run this additional javascript after the page is done loading (repeatable)
* `--ssl-crt-path`: _`<path>`_ Path to the ssl client cert public key in OpenSSL PEM format, optionally followed by intermediate ca and trusted certs
* `--ssl-key-password`: _`<password>`_ Password to ssl client cert private key
* `--ssl-key-path`: _`<path>`_ Path to ssl client cert private key in OpenSSL PEM format
* `--user-style-sheet`: _`<path>`_ Specify a user style sheet, to load with every page
* `--username`: _`<username>`_ HTTP Authentication username
* `--window-status`: _`<windowStatus>`_ Wait until window.status is equal to this string before rendering page
* `--zoom`: _`<float>`_ Use this zoom factor
</details>

```py
from htmlwebshot import WebShot
shot = WebShot()
shot.params = {
    "--custom-header": "Accept-Encoding gzip",
    "--minimum-font-size": 50,
    "--format": "png",
    "--zoom": 10,
    }
```

### Config Path  

```py
from htmlwebshot import WebShot, Config
shot = WebShot()
shot.config = Config(wkhtmltopdf="/path/to/wkhtmltopdf", wkhtmltoimage="/path/to/wkhtmltoimage")
```
