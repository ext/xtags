# XTags metadata pseudo-filesystem

XTags is a proof-of-concept implementation of a filesystem with nothing but
metadata. Files does not exist in directories at all, but "directories" is used
to browse files matching metadata.

For my own purposes, it is useful to store anything from mediafiles to
documents. For this purpose XTags allows to query for metadata from sources like
imdb, anidb, etc, and supports storing a thumbnail.

This implementation is using symlinks and must be manually updated after editing
metadata, and only works on directories (on the real filesystem)

    # ls tag-test
    year:2009 year:2010 year:2011 content-type:image-png content-type:video-x-matroska
    # ls tag-test/content-type:image-png
    year:2009 year:2010 year:2011 holiday-pictures-2009 holiday-pictures-2010 holiday-pictures-2011 sample-pictures
    # ls tag-test/content-type:image-png/year:2010
    holiday-pictures-2010 sample-pictures
    # ls tag-test/content-type:image-png/year:2010/sample-pictures
    sample01.png sample02.png sample03.png sample04.png sample05.png

For each "directory" an intersection is performed, e.g.
`content-type:image-png/year:2010` is the intersection of all files tagged with
`content-type:image/png` and `year:2010`. It also means that reversing the tags
yields the same result: `year:2010/content-type:image-png".

Custom queries can be made using the xtags cli tool,
e.g. `xtags query year:1995-2005`.
