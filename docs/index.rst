Welcome to ttl2html documentation!
==================================

**ttl2html** is a static site generator for Linked Data.

This tool accepts RDF/Turtle format as input to generate the corresponding HTML files.

The Linked Data Principle [TBL_2006]_ suggests that identifying things as HTTP URIs (resources) and resolving them on the Web is important.
This tool helps to generate a website for a Linked Data dataset and publish it on the Web.

Check out the :doc:`usage` and :doc:`configuration` sections for further information, including
how to :ref:`installation` the project.

Contents
--------

.. toctree::
   :maxdepth: 2
   
   usage
   configuration
   templates
   limitations
   dataset
   shapes
   usecases
   contact

.. toctree::
   :hidden:

   xlsx2shape

See also
--------

There is another tool **xlsx2shape** to describe a dataset schema using SHACL.
See :doc:`xlsx2shape` for details.

This tool is based on experiences from publishing Japanese Textbook LOD dataset [JP-TEXTBOOK_2017]_.

References
----------

.. [TBL_2006] Tim-Berner Lee (2006). "Linked Data". https://www.w3.org/DesignIssues/LinkedData.html
.. [JP-TEXTBOOK_2017] Y. Egusa & M. Takaku (2017). "Japanese Textbook LOD". https://w3id.org/jp-textbook/
