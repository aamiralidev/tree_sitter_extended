import pathlib
import re
import setuptools

from Cython.Build import cythonize

init = (pathlib.Path('tree_sitter_extended') / '__init__.py').read_text()
match = re.search(r"^__version__ = '(.+)'$", init, re.MULTILINE)
version = match.group(1)

with open('README.rst') as reader:
    readme = reader.read()

setuptools.setup(
    name='tree_sitter_extended',
    version=version,
    description='Binary Python wheels for all tree sitter languages.',
    long_description=readme,
    author='Aamir Ali',
    author_email='aamiraliadv1@gmail.com',
    url='https://github.com/aamiralidev/tree_sitter_extended',
    license='Apache 2.0',
    ext_modules=cythonize('tree_sitter_extended/core.pyx', language_level='3'),
    packages=['tree_sitter_extended'],
    package_data={'tree_sitter_extended': ['languages.so', 'languages.dll']},
    install_requires=['tree-sitter==0.20.2'],
    project_urls={
        'Documentation': 'https://github.com/aamiralidev/tree_sitter_extended',
        'Source': 'https://github.com/aamiralidev/tree_sitter_extended',
        'Tracker': 'https://github.com/aamiralidev/tree_sitter_extended/issues',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
