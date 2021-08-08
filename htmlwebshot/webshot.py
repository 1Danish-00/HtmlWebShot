# -*- coding: utf-8 -*-

import os

from .config import Config
from .shotter import Clickit


class WebShot:

    """main class to pass config and parameters and get return results"""

    def __init__(
        self,
        flags=[],
        size=(None, None),
        quality=None,
        delay=None,
        config=None,
        params={},
    ):
        self.size = size
        self.flags = flags
        self.quality = quality
        self.delay = delay
        self.params = params
        self.config = Config() if not config else config
        self._cache = None

    # To update & get Config
    @property
    def config(self):
        return self.wkhp, self.wkhi

    @config.setter
    def config(self, config):
        self.wkhp, self.wkhi = config.get_ps()

    # Get & Set size tuple >> int : int
    @property
    def size(self):
        return self.height, self.width

    @size.setter
    def size(self, _size):
        self.height, self.width = _size

    # For Settings and deleting Cache
    @property
    def cache(self):
        if self._cache:
            return self._cache
        return

    @cache.setter
    def cache(self, file):
        if file:
            self._cache = file

    @cache.deleter
    def cache(self):
        self._cache = None

    def create_html(self, hfile=None, cfile=None, hstr=None, cstr=None):
        """creating & combining html with css and saving to cache

        parameters :: hfile :: str :: input html file
                   :: cfile :: str :: input css file
                   :: hstr :: str :: input html string
                   :: cstr :: str :: input css string

        return :: str :: saved cache file
        """
        if hfile:
            hstr = open(hfile).read()
        if cfile:
            cstr = open(cfile).read()
        new_html = f"""\
        <html>
        <head>
            <style>
                {cstr}
            </style>
        </head>
        <body>
            {hstr}
        </body>
        </html>
        """
        file = ".html"
        with open(file, "w") as f:
            f.write(new_html)
            f.close()
        self.cache = file
        self.file = file

    def source_set(self, url=None, html=None, css=None, other=None):
        """finding & settings, input files or strings to use

        parameters :: url :: str :: input url
                   :: html :: str :: html file or strings
                   :: css :: str :: css file or strings
                   :: other :: str :: any file or strings

        return :: str :: file/data to be process
        """
        if url:
            self.file = url
        if html and css:
            if os.path.isfile(html):
                if os.path.isfile(css):
                    self.create_html(hfile=html, cfile=css)
                else:
                    self.create_html(hfile=html, cstr=css)
            else:
                if os.path.isfile(css):
                    self.create_html(hstr=html, cfile=css)
                else:
                    self.create_html(hstr=html, cstr=css)
        elif html:
            if os.path.isfile(html):
                self.file = html
            else:
                file = ".html"
                with open(file, "w") as f:
                    f.write(str(html))
                    f.close()
                self.cache = file
                self.file = file
        elif other:
            if os.path.isfile(other):
                self.file = other
            else:
                file = ".text"
                with open(file, "w") as f:
                    f.write(str(other))
                    f.close()
                self.cache = file
                self.file = file

    # output path setup
    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, loc):
        loc = os.path.abspath(loc)
        self._output = loc

    def create_pic(
        self,
        url=None,
        html=None,
        css=None,
        other=None,
        size=(None, None),
        quality=None,
        output=None,
        *args,
        **kwargs,
    ):
        """main funcn of class to get image (non async)

        parameters :: url :: str :: input link of webpage
                   :: html :: str :: file or text (html)
                   :: css :: str :: file or text (css)
                   :: other :: str :: file or text (any)
                   :: size :: tuple (int, int) :: height & width :: default full-screen
                   :: quality :: int :: from 0 to 100
                   :: output :: str :: path to save image

        return :: str :: saved image path
        """
        if size[0] and size[1]:
            self.size = size
        if quality:
            self.quality = quality
        self.output = "webshot.png" if not output else output
        self.source_set(url, html, css, other)
        path = Clickit().create_stuff(
            self.config[1],
            self.flags,
            self.params,
            self.quality,
            self.delay,
            self.size,
            self.file,
            self.output,
        )
        # cleaning cache if present
        if self.cache:
            os.remove(self.cache)
            del self.cache
        # as per issue https://github.com/1Danish-00/htmlwebshot/blob/f1089bfd172c70b31fee76bfb17ea6d013b3a6a3/htmlwebshot/shotter.py#L172
        # need to rename as per output
        if path != self.output:
            os.rename(path, self.output)
        return self.output

    async def create_pic_async(
        self,
        url=None,
        html=None,
        css=None,
        other=None,
        output=None,
        size=(None, None),
        quality=None,
        *args,
        **kwargs,
    ):
        """main async funcn of class to get image from input parameters

        parameters :: url :: str :: input link of webpage
                   :: html :: str :: file or text (html)
                   :: css :: str :: file or text (css)
                   :: other :: str :: file or text (any)
                   :: size :: tuple (int, int) :: height & width :: default full-screen
                   :: quality :: int :: from 0 to 100
                   :: output :: str :: path to save image

        return :: str :: saved image path
        """
        self.source_set(url, html, css, other)
        self.output = "webshot.png" if not output else output
        if size[0] and size[1]:
            self.size = size
        if quality:
            self.quality = quality
        result = await Clickit().create_stuff_async(
            self.config[1],
            self.flags,
            self.params,
            self.quality,
            self.delay,
            self.size,
            self.file,
            self.output,
        )
        # as per issue https://github.com/1Danish-00/htmlwebshot/blob/main/htmlwebshot/shotter.py#L172
        # need to rename as per output
        if result != self.output:
            os.rename(result, self.output)
        # cleaning cache if present
        if self.cache:
            os.remove(self.cache)
            del self.cache
        return self.output
