# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from elasticsearch_dsl import Keyword, Text, Integer, Document, Completion
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])


class LkPersonType(Document):
    suggest = Completion(analyzer="ik_max_word")
    id = Keyword()
    parent_id = Keyword()
    url = Keyword()
    name = Keyword()
    occupation = Text(analyzer="ik_max_word")
    # location = scrapy.Field()
    photo_url = Keyword()
    photo_path = Keyword()
    gender = Keyword()
    beauty_score = Integer()

    class Index:
        name = "lnkn"
        settings = {
            "number_of_shards": 5,
            "number_of_replicas": 1,
        }
