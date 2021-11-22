import pathlib
import re

from setuptools import setup
# from setuptools_rust import Binding, RustExtension

ROOT = pathlib.Path(__file__).parent

with open('rusttp/__init__.py', 'r') as f:
    content = f.read()
    try:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)  # type: ignore
    except AttributeError:
        raise RuntimeError('Unable to find version string')

    try:
        author = re.search(r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)  # type: ignore
    except AttributeError:
        author = 'Cryptex'

with open(ROOT / 'README.md', encoding='utf-8') as f:
    readme = f.read()

with open(ROOT / 'requirements.txt', encoding='utf-8') as f:
    requirements = f.readlines()

setup(
    name="rusttp",
    author=author,
    url="https://github.com/Cryptex-github/rusttp",
    project_urls={
        "Issue tracker": "https://github.com/Cryptex-github/rusttp/issues/new",
    },
    version=version,
    packages=["rusttp"],
    license="EUPL v1.2",
    description="Blazingly fast python HTTP module with Rust's reqwest",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8.0",
    zip_safe=False,
    # rust_extensions=[RustExtension("rusttp.rusttp", binding=Binding.PyO3)],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
