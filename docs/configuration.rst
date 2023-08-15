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

* ``about_file``: Specified filename is used for documenting schemas of the dataset. It requires SHACL documentation within the dataset. By default, the filename ``about.html`` is used.
* ``additional_link``: Addional links displayed at the top menu. Specify an array of link items with two keys ``href`` and ``label``. e.g. ``[ { "href": "http://example.org", "label": "Link" } ]``
* ``admin_name``: Name of the dataset publisher displayed at the footer.
* ``about_toc``: ``true`` / ``false`` to specify whether to output a table of contents in ``about.html``. The default is ``false``, which means no table of contents.
* ``base_uri``: (Required) Base URI for the dataset. Base URI is considered as the prefix for the target resources, and only the matched URIs with the prefix are picked up for the generation.
* ``breadcrumbs``: Configuration for creating a hierarchical breadcrumb list of multiple resources. Define a list of properties that are higher level resources or related resources of the resource. In the example below, the ``schema:hasPart`` and ``jp-cos:hasOfStudy`` properties, if present, respectively, are used to construct the navigation menu by considering resources linked from the current resource to be higher-level resources. The default display label on the breadcrumb list is "title", but if the ``label`` attribute is defined, the value of the property defined in the ``label`` attribute can be used as a breadcrumb link. Also, if the ``inverse`` attribute is present, then the resource being transitioned to as a property to the current resource is considered to be a higher level. It is also possible to specify a resource that spans a multi-level relationship with an empty node, etc. In that case, add a list to the ``property`` attribute and add a ``property`` attribute to its subordinate items as well. At the end of the example below, the ``schema:isPartOf`` property of the resource to which the ``schema:workExample`` property of the resource in question is specified can be used as a navigation resource.

  .. code-block:: YAML

    breadcrumbs:
      - property: http://schema.org/hasPart
        inverse: true
        label: https://w3id.org/jp-cos/sectionNumber
      - property: https://w3id.org/jp-cos/courseOfStudy
      - property:
        - property: http://schema.org/workExample
        - property: http://schema.org/isPartOf

* ``copyright_year``: Copyright year statement displayed at the footer along with the ``admin_name`` parameter above.
* ``css_file``: The path of the CSS stylesheet file to use locally.
* ``custom_css``: Specify the code snippet of the CSS stylesheet (e.g. ``nav.navbar {background-color: pink} ``).
* ``google_analytics``: Google tracking code for usage statistics by [Google Analytics](https://analytics.google.com).:: YAML
  google_analytics: G-XXXXXXXXXXXX

* ``google_custom_search_id``: Specify the search engine ID for setting up a site search form using [Google Custom Search](https://developers.google.com/custom-search). .

  .. code-block:: YAML

    google_custom_search_id: 0123456789

* ``javascript_file``: The path of the JavaScript file to use locally.
* ``labels``: Mappings for the custom property labels.
* ``locale``: Locale name for the output messages. Default: ``en`` (e.g. ``ja``, ``en``)
* ``logo``: The logo image file to be displayed on the menu. Specify the file path or URL.
* ``navbar_class``: Specifies the class setting for displaying the navigation bar at the top of the screen. If not specified, ``navbar-light`` is used. Use this if you want to specify a black background color as follows:

  .. code-block:: YAML

    navbar_class: navbar-dark bg-dark

* ``ogp``: Specify [OGP (Open Graph Protocol)](https://ogp.me) settings if you have additional logo settings for social networking sites, etc. You can specify ``ogp:image``, ``ogp:type``, etc.

  .. code-block:: YAML

    ogp:
      image: https://example.org/logo2.png
      type: article

* ``output_dir``: Output directory for the dataset.
* ``output_turtle``: Whether to output the RDF/Turtle format file corresponding to each resource URI, as ``true`` / ``false``. Default is ``true`` (i.e. output RDF/Turtle format files).
* ``shape_orders``: controls the order in which resource descriptions are output to about.html. The descriptions are output in the order of the resource shapes listed here. If not set, the default is alphabetical order of shape URIs. Set as a list, as in the following example:

  .. code-block:: YAML

    shape_orders:
      - https://example.org/ItemShape
      - https://example.org/BookShape

* ``site_title``: Main title for the whole website.
* ``template_dir``: Local template directory to find a template file. Default template files are available at [here](https://github.com/masao/ttl2html/tree/master/templates). To overwrite the contents of the original template, copy the original file to the directory specified here and rewrite it.
* ``title_property``: Specified URI is regarded as a title property for the resource. In default, a title is matched with the following properties:

  * https://www.w3.org/TR/rdf-schema/#label
  * http://purl.org/dc/terms/title
  * http://purl.org/dc/elements/1.1/title
  * http://schema.org/name
  * http://www.w3.org/2004/02/skos/core#prefLabel

* ``top_additional_property``: For each set of resources expanded by ``top_class`` setting, specify a list of additional sub-hierarchies to be expanded. The properties that make up the sub-hierarchy are specified as a list.
* ``top_class``: Specified URI is the class of the records listed in the top page. By default, this tool does not generate the top page.
