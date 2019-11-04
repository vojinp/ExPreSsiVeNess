from setuptools import setup, find_packages

setup(
    name="data-visualizer-complex",
    version="0.1",
    packages=find_packages(),
    install_requires=['expressiveness-core>=0.1'],
    namespace_packages=['visualizer_plugin', 'visualizer_plugin.complex', 'visualizer_plugin.complex.templates'],
    package_data={'visualizer_plugin.complex.templates': ['*.html']},
    include_package_data=True,
    entry_points={
        'visualizer':
            ['complex_visualizer=visualizer_plugin.complex.complex_visualizer:ComplexVisualizer'],
    },
    zip_safe=False
)
