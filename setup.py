from setuptools import setup, find_packages

setup(
    name='panasonic-concat',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/xamgore/panasonic-concat',
    license='MIT',
    author='Igor Strebezhev',
    author_email='xamgore+pip@ya.ru',
    description='Convert camera\'s video files into a single mp4 file',
    install_requires=['ffmpeg-python', 'ffmpeg-normalize', 'pymediainfo', 'iso8601', ]
)
