from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ssr_url_parser',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/tyong920/ssr_url_parser',
    license='https://www.gnu.org/licenses/lgpl-3.0.en.html',
    author='tyong920',
    author_email='tyong920@gmail.com',
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'ssr-parse = ssr_url_parser.scripts.parse_ssr_url:cli'
        ]
    },
    description='A tiny CLI tool for parsing SSR url to plain text.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
