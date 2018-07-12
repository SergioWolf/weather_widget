from setuptools import setup

setup(
    name="Weather_Widget",
    version='0.11',
    description='Simple weather widget',
    long_description='Simple weather widget with country and city selection',
    url='https://github.com/SergioWolf/weather_widget',
    license='MIT',
    keywords=['python', 'weather', 'OpenWeatherMap'],
    author='Sergey Volkov',
    author_email='sergio_volf@mail.ru',
    packages=[
        'weather_widget',
        'weather_widget/files',
        'weather_widget/images',
    ],
    package_data={
        '': ['Saint-Petersburg'],
    },
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=[
        'PyQt5==5.10.1',
        'SQLAlchemy==1.2.7',
        'Jinja2==2.10',
        'Pillow==5.1.0',
        'PyOpenGL==3.1.0',
    ],
)
