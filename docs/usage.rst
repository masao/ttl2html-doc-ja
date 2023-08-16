Usage
=====

.. _installation:

Installation
------------

To use ttl2html, first install it using Rubygems:

.. code-block:: console

   $ gem install ttl2html

Command line usage
------------------

First, you must create a configuration file named ``config.yml`` with a YAML format.
One required key for the configuration is ``base_uri``:

.. code-block:: YAML

   base_uri: https://www.example.org/

With this configuration file, you can execute a command on the dataset file(s) :

.. code-block:: console

   $ ttl2html dataset.ttl

The command parses the dataset file(s) and generate HTML files.


Command line options
--------------------

.. code-block:: console
   
   $ ttl2html --config test.yml dataset.ttl

The command ``ttl2html`` accepts the following options:

* ``--config file``: Read the configuration file from file (Default: ``config.yml``).
