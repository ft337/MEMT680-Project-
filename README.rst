.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/Homework3.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/Homework3
    .. image:: https://readthedocs.org/projects/Homework3/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://Homework3.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/Homework3/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/Homework3
    .. image:: https://img.shields.io/pypi/v/Homework3.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/Homework3/
    .. image:: https://img.shields.io/conda/vn/conda-forge/Homework3.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/Homework3
    .. image:: https://pepy.tech/badge/Homework3/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/Homework3
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/Homework3

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

=========
Homework3
=========


This repository uses ``matplotlib`` to display randomly selected images from my dataset as well as random examples. 
Along with a static visualization, using ``Dash``, an interactive plot was produced. Here the dataset contains images of 
spent lithium ion batteries, including the anode, cathode, and other substances. The images were collected from industrial shredder
machines. The dataset could be used for classification of object detection. The link to the dataset: 
``https://www.kaggle.com/datasets/thgere/spent-lithium-ion-battery-recyclingslibr-dataset``

After cloning my repository, create a new environment and run:  ``pip install -r docs/requirements.txt`` to download the dependencies. 
    
Once this is complete, install the package locally with the command: ``pip install -e .``

To run the interactive plot, run: ``interactive_plot``
Which should host the interactive demo locally at the address ``http://127.0.0.1:8050/``. 






.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.6. For details and usage
information on PyScaffold see https://pyscaffold.org/.
