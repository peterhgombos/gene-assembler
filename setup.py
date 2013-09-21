from distutils.core import setup

setup(
    name='Gene Assembler',
    version='0.1',
    author=u'Sigve Sebastian Farstad',
    author_email='sigvefarstad@gmail.com',
    packages=['gene'],
    url='http://github.com/dmpro-ytelse/gene-as',
    description='Assembles GENE assembly',
    entry_points={
        'console_scripts': [
            'gene-as = gene:main'
        ]
    }
)
