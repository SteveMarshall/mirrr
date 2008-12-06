#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import Template

api_key              = 'YOUR_API_KEY'
api_secret           = 'YOUR_API_SECRET'

source_username      = 'Stevie BM'
source_tag           = 'flickr:republishas=The Photo Album'

target_username      = 'The Photo Album'

# Settings for uploaded photos
image_url            = Template( 'http://farm${farm_id}.static.flickr.com/${server_id}/${id}_${secret}.jpg' )
base_description     = Template(
                            'Photo © Steve Marshall; see '
                          + '<a href="/photos/steviebm/">his photostream</a> '
                          + 'for <a href="${photo_url}">the original</a> '
                          + '(where you can comment or see the photo at higher resolution).'
                       )
base_url             = Template( '${photos_url}${id}/' )
base_tags            = Template( 'flickr:takenby=${user},flickr:original=${id}' )

# Settings for sets in target
base_set_description = Template( '''${description}

Photos © Steve Marshall; see <a href="${set_url}">his original set</a>''' )
base_set_url         = Template('${photos_url}sets/${photoset_id}')