import re
from urllib.parse import urljoin
from scrapy import Selector
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join

def get_author_id(item):
    re_pattern = re.compile(r"youlaId%22%2C%22([a-zA-Z|\d]+)%22%2C%22avatar")
    result = re.findall(re_pattern, item)
    return result


def clear_unicode(itm):
    return itm.replace("\u2009", "").replace("\xa0", "")

def clear_str(itm):
    return itm.strip()

def get_specifications(item):
    tag = Selector(text=item)
    name = tag.xpath("//div[@class='AdvertSpecs_label__2JHnS']/text()").get()
    value = tag.xpath("//div[@class='AdvertSpecs_data__xK2Qx']//text()").get()
    return {name: value}

def flat_dict(items):
    result = {}
    for itm in items:
        result.update(itm)
    return result

def vac_description(itm):
    if '.tmpl_hh_wrapper' in itm or 'window.jquery' in itm:
        itm = ''
        return itm
    else:
        return itm.replace("\u2009", "").replace("\xa0", "").replace('\n', "").replace('\u200b', "")