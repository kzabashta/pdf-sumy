try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PDF file summarizer.',
    'author': 'Kosta Zabashta',
    'url': 'https://github.com/kzabashta/pdf-summarizer',
    'download_url': 'https://github.com/kzabashta/pdf-summarizer',
    'author_email': 'kosta.zabashta@gmail.com',
    'version': '0.1',
    'install_requires': ['pdfminer', 'sumy'],
    'packages': ['summarizer'],
    'scripts': [],
    'name': 'pdf-summarizer'
}

setup(**config)