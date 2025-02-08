Configuration
=============

You can setup several options on the configuration file, ``config.yml`` (default).

The example below is a basic configuration for ttl2html:

.. code-block:: YAML

  base_uri: https://www.example.org/
  output_dir: /var/www/html/dataset/
  labels:
    http://www.w3.org/1999/02/22-rdf-syntax-ns#type: Class
    http://schema.org/name: Title
  site_title: A sample dataset
  title_property: http://example.org/title
  top_class: http://schema.org/Book

Configuration parameters
------------------------

All configuration keys available are documeted as follows:

.. confval:: about_file
  :default: ``about.html``
  
  Specified filename is used for documenting schemas of the dataset. It requires SHACL documentation within the dataset. By default, the filename ``about.html`` is used.

.. confval:: additional_link
  
  Addional links displayed at the top menu. Specify an array of link items with two keys ``href`` and ``label``. e.g. ``[ { "href": "http://example.org", "label": "Link" } ]``

.. confval:: admin_name
  
  Name of the dataset publisher displayed at the footer.

.. confval:: about_toc
  :type: boolean
  :default: ``false``

  ``true`` / ``false`` to specify whether to output a table of contents in ``about.html``. The default is ``false``, which means no table of contents.

.. confval:: base_uri
  
  **[required]** Base URI for the dataset. Base URI is considered as the prefix for the target resources, and only the matched URIs with the prefix are picked up for the generation.

.. confval:: breadcrumbs
  
  Configuration for creating a hierarchical breadcrumb list of multiple resources. Define a list of properties that are higher level resources or related resources of the resource. In the example below, the ``schema:hasPart`` and ``jp-cos:hasOfStudy`` properties, if present, respectively, are used to construct the navigation menu by considering resources linked from the current resource to be higher-level resources. The default display label on the breadcrumb list is "title", but if the ``label`` attribute is defined, the value of the property defined in the ``label`` attribute can be used as a breadcrumb link. Also, if the ``inverse`` attribute is present, then the resource being transitioned to as a property to the current resource is considered to be a higher level. It is also possible to specify a resource that spans a multi-level relationship with an empty node, etc. In that case, add a list to the ``property`` attribute and add a ``property`` attribute to its subordinate items as well. At the end of the example below, the ``schema:isPartOf`` property of the resource to which the ``schema:workExample`` property of the resource in question is specified can be used as a navigation resource.

  .. code-block:: YAML

    breadcrumbs:
      - property: http://schema.org/hasPart
        inverse: true
        label: https://w3id.org/jp-cos/sectionNumber
      - property: https://w3id.org/jp-cos/courseOfStudy
      - property:
        - property: http://schema.org/workExample
        - property: http://schema.org/isPartOf

.. confval:: copyright_year
  
  Copyright year statement displayed at the footer along with the :confval:`admin_name` parameter above.

.. confval:: css_file
  
  The path of the CSS stylesheet file to use locally.

.. confval:: custom_css
  
  Specify the code snippet of the CSS stylesheet (e.g. ``nav.navbar {background-color: pink}``).

.. confval:: google_analytics
  
  Google tracking code for usage statistics by `Google Analytics <https://analytics.google.com>`_.

  .. code-block:: YAML

    google_analytics: G-XXXXXXXXXXXX

.. confval:: google_custom_search_id
  
  Specify the search engine ID for setting up a site search form using `Google Custom Search <https://developers.google.com/custom-search>`_.

  .. code-block:: YAML

    google_custom_search_id: 0123456789

.. confval:: javascript_file
  
  The path of the JavaScript file to use locally.

.. confval:: labels
  
  Specify the custom label name for each property.
  Specify the property URI as the key and the label name as the value.
  
  For example, the following setting specifies that the ``dct:description`` property should be displayed as "Item details":

  .. code:: yaml

    labels:
      http://purl.org/dc/terms/description: Item details

  If you need to change the label for each class, use the :confval:`labels_with_class` setting or the :doc:`shape method <shapes>`.

  If you do not specify a name for the property using these settings (default), the string at the end of the property URI with the first letter capitalized will be displayed.

  For example, ``dct:description`` will be displayed as "Description," and ``schema:name`` will be displayed as "Name".

.. confval:: labels_with_class

  labels_with_class is a configuration item that specifies the property name for resources belonging to a specific RDF class.
  Use this when you want to give different names to the same property for each class.

  The name is specified with the class URI as the key and each property URI and its name as the value.

  For example, in the following example, the ``dct:description`` property is represented as "Item details" for resources of the ``ex:Item`` class, and "Detailed text" for resources of the ``ex:Work`` class:

  .. code:: yaml

    labels_with_class:
      https://example.org/Item:
        http://purl.org/dc/terms/description: Item details
      https://example.org/Work:
        http://purl.org/dc/terms/description: Detailed text

  There is a method for more detailed labeling, :doc:`using shapes <shapes>`.

  Also, if you don't need to distinguish between classes, specify it using the :confval:`labels` setting.

.. confval:: locale
  :default: ``en``
  
  Locale name for the output messages. Default: ``en`` (e.g. ``ja``, ``en``)

.. confval:: logo
  
  The logo image file to be displayed on the menu. Specify the file path or URL.

.. confval:: navbar_class
  
  Specifies the class setting for displaying the navigation bar at the top of the screen. If not specified, ``navbar-light`` is used. Use this if you want to specify a black background color as follows:

  .. code-block:: YAML

    navbar_class: navbar-dark bg-dark

.. confval:: ogp
  
  Specify `OGP (Open Graph Protocol) <https://ogp.me>`_ settings if you have additional logo settings for social networking sites, etc. You can specify ``ogp:image``, ``ogp:type``, etc.

  .. code-block:: YAML

    ogp:
      image: https://example.org/logo2.png
      type: article

.. confval:: output_dir
  :default: ``.``

  Output directory for the dataset. If not specified, the current working directory is used for the outputs.

.. confval:: output_turtle
  :type: boolean
  :default: ``true``
  
  Whether to output the RDF/Turtle format file corresponding to each resource URI, as ``true`` / ``false``. Default is ``true`` (i.e. output RDF/Turtle format files).

.. confval:: shape_orders
  
  This configuration option controls the order in which resource descriptions are output to :confval:`about_file`. The descriptions are output in the order of the resource shapes listed here. If not set, the default is alphabetical order of shape URIs. Set as a list, as in the following example:

  .. code-block:: YAML

    shape_orders:
      - https://example.org/ItemShape
      - https://example.org/BookShape

.. confval:: site_title
  
  Main title for the whole website.

.. confval:: template_dir
  :default: ``templates/``
  
  Local template directory to find a template file. Default template files are available at `here <https://github.com/masao/ttl2html/tree/master/templates>`_. To overwrite the contents of the original template, copy the original file to the directory specified here and rewrite it.

.. confval:: title_property
  
  Specified URI is regarded as a title property for the resource. In default, a title is matched with the following properties:

  * https://www.w3.org/TR/rdf-schema/#label
  * http://purl.org/dc/terms/title
  * http://purl.org/dc/elements/1.1/title
  * http://schema.org/name
  * http://www.w3.org/2004/02/skos/core#prefLabel

.. confval:: title_property_perclass

  This setting specifies property URIs for each class URI. If a specified property exists on a resource, its value will be used as the title of the generated resource page.

  For example, in the following case: Resources of the ``foaf:Person`` class use the ``foaf:name`` property as the title, while resources of the ``example:Item`` class use the ``dct:description`` property as the title.

  .. code-block:: YAML

   title_property_perclass:
     http://xmlns.com/foaf/0.1/Person:
       http://xmlns.com/foaf/0.1/name
     http://example.org/Item:
       http://purl.org/dc/terms/description

  If a resource does not belong to a class specified in ``title_property_perclass``, the :confval:`title_property` setting will be used.

.. confval:: top_additional_property
  
  For each set of resources expanded by :confval:`top_class` setting, specify a list of additional sub-hierarchies to be expanded. The properties that make up the sub-hierarchy are specified as a list.

.. confval:: top_class
  
  Specified URI is the class of the records listed in the top page. By default, this tool does not generate the top page.

.. confval:: uri_mappings

  If you want to change the output file names when outputting local files corresponding to a URI, use this setting. You can specify the patterns for the part of paths in a URI and then determine how the matched part of the path has to be changed. For example, when outputting many files in a single directory, you can specify a pattern for the first few characters and the rest of the filename so that each directory contains a separate set of files with different destinations. The example below specifies that a URI path consisting of 16 alphanumeric characters is divided into the first three characters and the rest of the path. Hence, the output files are placed for each two-character directory.
  
  .. code-block:: YAML
  
    uri_mappings:
      - regexp: !ruby/regexp /^(\d\w\w)(\w{13})$/
        path: '\1/\2'
