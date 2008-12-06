mirrr (Pronounced ‘mirror’)
===========================

A tool to mirror a subset of one flickr account to another.

Assumptions
-----------

- Mirrored images should be named identically to the original, but have a
  description linking to the source photo.
- The only tags applied to the mirror should be machine tags referencing to
  the original. 
- Maximum image size of mirrors is the flickr’s ‘medium’ image size (500px on
  the longest side).

Prerequisites
-------------
- [Python interface for the flickr API][flickrapi]

[flickrapi]: http://stuvel.eu/projects/flickrapi

Configuration
-------------

Create a `config.py` (a sample is included) file in the same directory as the
mirrr script and specify your API key and secret, source username and tag,
target username, and details for the mirrors’ metadata.

On first run, __something will happen__ to authenticate with the _target_
flickr acocunt.

Todo
----

- Only mirror photos uploaded since last-run
- Only create set mirrors if no set of same name exists
- Add data paging for large mirror operations