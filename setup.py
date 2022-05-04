from setuptools import setup, find_packages

with open("README.md", 'r',encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='LineBot',
    version='0.1.0',
    description='Simple-LINELIB',
    long_description=long_description,
    author='Tolg KR',
    author_email='tolgkr@cybertkr.com',
    url='https://github.com/CyberTKR/Simple-LINELIB',
    packages=find_packages(include=['CyberTK', 'CyberTK.*']),
    install_requires=[
        'httpx==0.19.0',
        'requests',
        'thrift',
        'CyberTKAPI'
    ],
    extras_require={'httpx': ['http2']}
)
