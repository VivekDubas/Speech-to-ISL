import setuptools

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='0.1.0',
    description='Python project',
    author='Revanth Kumar',
    author_email='revanth3309g@gmail.com',
    url='https://github.com/revanth3309/Speech_to_ISL',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)