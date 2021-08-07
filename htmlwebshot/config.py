# -*- coding: utf-8 -*-


import shutil


class Config(object):

    """Config class to configure path of wkhtmltoimage, wkhtmltopdf"""

    def __init__(self, wkhtmltoimage=None, wkhtmltopdf=None):
        """To Config Binary Path of wkhtmltopdf & wkhtmltoimage

        parameters:: wkhtmltoimage :: Put Binary Path of file
                  :: wkhtmltopdf :: put Binary path of file
        """
        self.wkhi = wkhtmltoimage
        self.wkhp = wkhtmltopdf

    def get_ps(self):
        """To get return of configured binary paths

        return :: tuple , (str, str) wkhtmltopdf, wkhtmltoimage path

        raise :: FileNotFoundError :: if Not Configured path or Config path wrong
        """
        # Auto configure if files exists on right place like /usr/bin/wkhtmltopdf
        # else you have to configure the binary paths
        if not self.wkhi:
            if shutil.which("wkhtmltoimage"):
                self.wkhi = "wkhtmltoimage"
        else:
            if not shutil.which(self.wkhi):
                self.wkhi = None
        # well for now wkhtmltopdf not needed , we using wkhtmltoimage
        # its for future use...
        # And for using wkhtmltoimage we have to install wkhtmltopdf.
        if not self.wkhp:
            if shutil.which("wkhtmltopdf"):
                self.wkhp = "wkhtmltopdf"
        else:
            if not shutil.which(self.wkhp):
                self.wkhp = None
        # if configuration success , return binary path
        # else raise error
        if not self.wkhp:
            raise FileNotFoundError(
                "pkg wkhtmltopdf not found, Be sure you set correct config"
            )
        elif not self.wkhi:
            raise FileNotFoundError(
                "pkg wkhtmltopdf exist but can't find wkhtmltoimage binary file location, Be sure to set correct config"
            )
        else:
            return self.wkhp, self.wkhi
