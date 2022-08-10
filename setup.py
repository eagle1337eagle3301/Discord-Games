import setuptools
import re

requirements = []
version = ''
readme = ''

with open("README.md") as rm:
    readme = rm.read()

with open('requirements.txt') as r:
    requirements = r.read().splitlines()

with open("discord_games/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setuptools.setup(
    name="discord_games",
    author="Tom-the-Bomb",
    version= version,
    description="A library to help users easily implement games within their discord bot",
    long_description=readme,
    long_description_content_type = "text/markdown",
    license="MIT",
    url="https://github.com/eagle37/Discord-Games",
    project_urls={
        "Repository": "https://github.com/eagle37/Discord-Games",
        "Issue tracker": "https://github.com/eagle37/Discord-Games/issues",
    },
    classifiers=[
        "Intended Audience :: Developers",
        'Programming Language :: Python',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    include_package_data=True,
    package_data={
        '': [
            'assets/**',
            'assets/country-data/**',
            'assets/country-flags/**',
        ]
    },
    packages=[
        'discord_games',
        'discord_games.button_games'
    ],
    install_requires=requirements,
    zip_safe=True,
    python_requires='>=3.8',
)
