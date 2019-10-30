from setuptools import setup, find_packages

setup(
    name="data-visualizer-simple",
    version="0.1",
    packages=find_packages(),
    install_requires=['expressiveness-core>=0.1', 'Django>=1.10'],
    namespace_packages=['visualizer_plugin', 'visualizer_plugin.simple', 'visualizer_plugin.simple.templates'],
    package_data={'visualizer_plugin.simple.templates': ['*.html']},
    include_package_data=True,
    entry_points={
        'visualizer':
            ['simple_visualizer=visualizer_plugin.simple.simple_visualizer:SimpleVisualizer'],
    },
    zip_safe=False
)
