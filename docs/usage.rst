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

First, you must create a configuration file named ``config.yml`` in YAML format.
One required key for the configuration is ``base_uri``:

.. code-block:: YAML

   base_uri: https://www.example.org/

With this configuration file, you can execute a command on the dataset file(s) :

.. code-block:: console

   $ ttl2html dataset.ttl

The command parses the dataset file(s) and generates HTML files.

Input File Specification
------------------------

The command sequentially reads one or more Turtle files given as command-line arguments.
The following forms are supported:

- **Single file**: ``ttl2html data.ttl``
- **Multiple files (processed in order)**: ``ttl2html a.ttl b.ttl c.ttl``
- **Gzip-compressed file**: ``ttl2html data.ttl.gz``
  (files ending with ``.gz`` are automatically decompressed, and then read)
- **Shell wildcard expansion**: ``ttl2html data/*.ttl``
  (the shell expands the list of files, which are then processed sequentially)

During execution, messages such as ``loading <path>...`` are printed to
standard error. After loading, the number of triples and subjects is shown: ``<N> triples. <M> subjects.``

Supported format
^^^^^^^^^^^^^^^^

- Only the **Turtle** format is supported.
- Even if the file extension is not ``.ttl``, the file content **must** be Turtle.
- Other formats such as RDF/XML or N-Triples are **not supported**.

Multiple files
^^^^^^^^^^^^^^

If multiple files are provided, they are merged into a single internal dataset.
When merging, all the values are appended for the same subject and predicate, and **duplicates are not removed.**

Command line options
--------------------

.. code-block:: console
   
   $ ttl2html --config test.yml dataset.ttl

The command ``ttl2html`` accepts the following options:

* ``--config file``: Read the configuration file from file (Default: ``config.yml``).
