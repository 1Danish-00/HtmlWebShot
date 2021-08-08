import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()


name = "htmlwebshot"
version = "v0.1.1"
author = "1Danish-00"
author_email = "danish@ultroid.tech"
desc = "Create Web Preview Images From url, Html-CSS ,svg, any other readable file or string."
lic = "GNU AFFERO aa rha posts GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/1Danish-00/htmlwebshot/"
project_urls = {
    "Bug Tracker": "https://github.com/1Danish-00/htmlwebshot/issues",
}
reqs = ["asyncio"]
keys = [
    "screenshot",
    "Webshot",
    "url to image",
    "html to image",
    "css to image",
    "svg to image",
    "text to image",
    "file to image",
]
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Topic :: Text Processing",
    "Topic :: Text Processing :: General",
    "Topic :: Text Processing :: Markup",
    "Topic :: Text Processing :: Markup :: HTML",
    "Topic :: Text Processing :: Markup :: XML",
    "Topic :: Utilities",
]

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=desc,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url=url,
    project_urls=project_urls,
    license=lic,
    keywords=keys,
    packages=setuptools.find_packages(),
    install_requires=reqs,
    classifiers=classifiers,
    python_requires=">=3.5",
)
