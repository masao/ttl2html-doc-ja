Limitations of This Tool
========================

Please note that "ttl2html" has specific limitations that are important to consider. Knowing these points can help you make informed decisions and maximize the tool's effectiveness.

URI designs
-----------

ttl2html is designed to generate files that directly reflect the URI structure of the original Linked Data dataset. Essentially, it assumes that the URI structure of each target resource corresponds one-to-one with the directory hierarchy and file groups of a static website.

As a result, URI structures that specify parts of a URI resource using a hash symbol (#), such as https://example.org/resource/#linked-data, are not supported. In such cases, avoiding the hash symbol is recommended, and instead, a directory hierarchy separated by slashes (/), such as https://example.org/resource/linked-data, is utilized.

Similarly, URI structures that specify resources as parameters using a question mark (?), such as https://example.org/resource?id=1, are also not supported and should be avoided.

Additionally, a URI structure includes URI resources that end with a slash (/) and those that do not. In that case, it becomes difficult to distinguish them on a static website, and thus, they are not supported. For example:

* https://example.org/foo
* https://example.org/foo/

When using ttl2html, please avoid the URI designs mentioned above.

Limitations on the Number of Files and Directories
--------------------------------------------------

ttl2html generates static HTML files corresponding to resource URIs. If the number of generated resources is enormous, issues may arise, including failures in file generation.

First, the file system used on your server has limits on the number of files and directories that can be created.

These limitations vary depending on the file system in use, so please check the restrictions of your OS and file system. For example, the NTFS file system used in standard Windows environments supports approximately 4.29 billion files, while the Apple File System (APFS) used in macOS supports up to approximately nine quintillion files.

Furthermore, if your dataset contains many resources within the same directory, in such cases, an excessive number of files may be generated under a single directory, potentially causing issues such as slower access times depending on the file system structure. If the number of files exceeds tens of thousands, it is advisable to implement countermeasures.

To mitigate this issue, use the `uri_mappings` configuration option to divide the generated files into multiple directories (see: :confval:`uri_mappings`).