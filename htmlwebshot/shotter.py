# -*- coding: utf-8 -*-

import asyncio
import re
import subprocess
import time

# optional flags list & details
# https://github.com/1Danish-00/htmlwebshot#flags-uses

all_flags = [
    "--quiet",  # Be less verbose
    "--disable-smart-width",  # To force size to be accurate
    "--custom-header-propagation",  # Add HTTP headers for each request.
    "--no-custom-header-propagation",  # Do not add HTTP headers for each resource
    "--disable-javascript",  # Do not allow web pages to run javascript
    "--enable-javascript",  # Do allow web pages to run javascript
    "--proxy-hostname-lookup",  # Use the proxy for resolving hostnames
    "--stop-slow-scripts",  # Stop slow running javascripts
    "--no-stop-slow-scripts",  # Do not Stop slow running javascripts
]

# optional params details :-
# https://github.com/1Danish-00/htmlwebshot#available-params

options = [
    "--bypass-proxy-for",
    "--cookie",
    "--cookie-jar",
    "--crop-h",
    "--crop-w",
    "--crop-x",
    "--crop-y",
    "--custom-header",
    "--encoding",
    "--format",
    "--minimum-font-size",
    "--password",
    "--post",
    "--post-file",
    "--proxy",
    "--run-script",
    "--ssl-crt-path",
    "--ssl-key-password",
    "--ssl-key-path",
    "--user-style-sheet",
    "--username",
    "--window-status",
    "--zoom",
]


class Clickit:

    """class Clickit for setting up commands & processing"""

    def __init__(self):
        pass

    @staticmethod
    def make_setup(
        config=None,
        flags=[],
        params={},
        quality=None,
        delay=None,
        size=(None, None),
        file=None,
        output=None,
    ):
        """To create command setup as per the input data

        parameters :: config :: configuration of Config class
                   :: flags :: list :: passed flags
                   :: params :: dict :: extra options with values
                   :: quality :: int :: output image quality (1-100)
                   :: delay :: float :: time to wait for js loading
                   :: size :: tuple (int, int) :: height & width
                   :: file :: str :: file
                   :: output :: str :: saving path

        return :: setup command
        """
        setup = []
        setup.append(config)
        for flag in flags:
            if flag in all_flags:
                setup.append(flag)
        for flag in list(params.keys()):
            if flag in options:
                setup.append(flag)
                values = str(params[flag]).strip().split()
                for value in values:
                    setup.append(value)
        setup.append("--images")
        if size[0] and size[1]:
            setup.append("--height")
            setup.append(str(size[0]))
            setup.append("--width")
            setup.append(str(size[1]))
        if quality:
            if quality <= 100 and quality >= 1:
                setup.append("--quality")
                setup.append(str(quality))
        if delay:
            setup.append("--javascript-delay")
            setup.append(str(delay))
        setup.append(file)
        setup.append(output)
        return setup

    def _proc(self, data):
        """processing setup data non async

        parameters :: data :: list :: returned from func setup

        return :: output logs
        """
        process = subprocess.Popen(
            data, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )  # nosec
        _, output = process.communicate()
        return output.decode().strip()

    def create_stuff(self, *args):
        """creating image from args non async

        return :: str :: image path

        raise :: SystemError :: while processing data
        """
        data = Clickit.make_setup(*args)
        proc = self._proc(data)
        if proc:
            # issue with wkhtmltoimage
            # sometimes can't save on a specific file
            # so, for bypass it change name & rename again on main return
            if "Could not write to output file" in proc:
                data.remove(data[-1])
                data.append(str(time.time()).split(".")[0] + ".jpg")
                proc = self._proc(data)
                if proc and "Error:" in proc:
                    raise SystemError(re.findall("Error:(.*)", proc))
            elif re.search("Error:", proc):
                raise SystemError(re.findall("Error:(.*)", proc))
        return data[-1]

    async def _sh(self, data):
        """running setup data async

        parameters :: data :: list :: returned from func setup

        return :: output logs
        """
        process = await asyncio.create_subprocess_exec(
            *data, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )  # nosec
        _, out = await process.communicate()
        return out.decode().strip()

    async def create_stuff_async(self, *args):
        """creating image from args async

        raise :: SystemError :: while processing data

        return :: str :: image path

        """
        setups = Clickit.make_setup(*args)
        err = await self._sh(setups)
        if err:
            # issue with wkhtmltoimage
            # sometimes can't save on a specific file
            # so, for bypass it change name & rename again on main return
            if "Could not write to output file" in err:
                setups.remove(setups[-1])
                setups.append(str(time.time()).split(".")[0] + ".jpg")
                err = await self._sh(setups)
                if err and "Error:" in err:
                    raise SystemError(re.findall("Error:(.*)", err))
            elif re.search("Error:", err):
                raise SystemError(re.findall("Error:(.*)", err))
        return setups[-1]
