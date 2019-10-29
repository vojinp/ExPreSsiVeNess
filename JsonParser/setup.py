from setuptools import setup, find_packages

setup(
    name="data-parser-json",
    version="0.1",
    packages=find_packages(),
    install_requires=['expressiveness-core>=0.1'],
    namespace_packages=['parser_plugin', 'parser_plugin.json'],
    entry_points={
        'parser':
            ['json_parser=parser_plugin.json.json_parser:JsonParser'],
    },
    zip_safe=True
)
