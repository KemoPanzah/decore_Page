from setuptools import setup, find_packages


setup(
    name='mkdocs_translate',
    version='0.1.0',
    description='A Plugin for MkDocs to translate the content of a page',
    long_description='',
    keywords='mkdocs',
    url='',
    author='Jean Rohark',
    author_email='no@mail',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
        'beautifulsoup4>=4.12.3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'translate = mkdocs_translate.plugin:Translate'
        ]
    }
)
