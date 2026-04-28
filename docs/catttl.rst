catttl
======

Overview
--------

``catttl`` is a simple command-line tool for safely concatenating multiple RDF/Turtle (ttl) files.

If you simply concatenate Turtle files using the `cat <https://en.wikipedia.org/wiki/Cat_(Unix)>`_ command, the following issues may occur:

* Duplicate or conflicting ``@prefix`` declarations
* Generation of syntactically invalid Turtle

``catttl`` avoids these problems and merges files while preserving RDF validity.

Key Features
^^^^^^^^^^^^

* Concatenates multiple Turtle files into one
* Normalizes and merges prefix declarations

Use Cases
^^^^^^^^^

* Merging partitioned RDF datasets
* Combining Turtle files collected from multiple sources

Basic Usage
-----------

To concatenate multiple Turtle files, run:

.. code-block:: console

   $ catttl dataset1.ttl dataset2.ttl > all-dataset.ttl

This command reads ``dataset1.ttl`` and ``dataset2.ttl``, and writes the merged Turtle output to ``all-dataset.ttl``.

If no output file is specified, the result is written to standard output:

.. code-block:: console

   $ catttl dataset1.ttl dataset2.ttl

Options
-------

``catttl`` provides command-line options to control how input files are handled.

.. code-block:: console

   $ catttl [options] [files]

Options List
^^^^^^^^^^^^

==========  ===============================
Option      Description
==========  ===============================
-f, --no-expand  Do not expand filenames
-h, --help       Show this help message
==========  ===============================

-f, --no-expand Option
^^^^^^^^^^^^^^^^^^^^^^

Suppresses filename expansion.

By default, ``catttl`` interprets version numbers at the end of filenames (excluding extensions) and automatically selects the latest available version among matching files.

When this option is specified, such expansion is disabled, and the given strings are treated as literal filenames.

Example
.......

.. code-block:: console

    $ catttl dataset.ttl dataset-partA.ttl > all-20260501.ttl

In this case, suppose the working directory contains multiple files such as:

- dataset-20260401.ttl
- dataset-20260501.ttl
- dataset-partA-001.ttl
- dataset-partA-010.ttl

The numeric suffix at the end of each filename is interpreted as a version number.  
``catttl`` automatically selects the highest versions (in this example, 20260501 and 010).

As a result, ``dataset-20260501.ttl`` and ``dataset-partA-010.ttl`` are selected and passed to ``catttl``.

On the other hand, when the ``--no-expand`` option is specified:

.. code-block:: console

    $ catttl --no-expand dataset-*.ttl

The string ``dataset-*.ttl`` is treated as a literal filename.  
No pattern or version expansion is performed.

Typical Use Cases
................

* Handling filename patterns in scripts
* Disabling automatic version resolution in ``catttl``
* Managing file lists externally

-h, --help Option
^^^^^^^^^^^^^^^^^

Displays the help message.

.. code-block:: console

    $ catttl --help
    Usage: catttl [options] [files]
    Options:
      -f, --no-expand  Do not expand filenames
      -h, --help       Show this help message

Related Information
------------------

* `RDF 1.1 Turtle <https://www.w3.org/TR/turtle/>`_ (W3C Recommendation, 25 February 2014)

