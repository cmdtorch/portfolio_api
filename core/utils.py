import os
import random
import uuid
import calendar
import math
import datetime
import shutil
from django.utils.deconstruct import deconstructible
from typing import List
from fastapi import File, HTTPException, status
from django.conf import settings


def pref_iter(instance, pref: List[str] = None):
    data = {}
    for p in pref:
        relation_name, child_relation = parse_pref(p)

        if hasattr(instance, relation_name) and getattr(instance, relation_name) is not None:
            all_method = getattr(getattr(instance, relation_name), "all", None)
            if callable(all_method):
                items = []
                for c in getattr(instance, relation_name).all():
                    items.append(c.get_data(child_relation))
                data[relation_name] = items
            else:
                data[relation_name] = getattr(instance, relation_name).get_data(child_relation)
        else:
            data[relation_name] = None

    return data


def parse_pref(pref):
    if isinstance(pref, str):
        return pref, None
    else:
        return list(pref.keys())[0], list(pref.values())[0]


def paginator(page: int):
    offset = (page-1) * 10
    limit = offset + 10
    return offset, limit


def password_validate(passwd):
    val = True

    if len(passwd) < 8:
        val = False, 'length should be at least 8'

    if len(passwd) > 32:
        val = False, 'length should be not be greater than 32'

    if not any(char.isdigit() for char in passwd):
        val = False, 'Password should have at least one numeral'

    if val:
        return val, 'Password is correct'


def create_file_name(format: str):
    ts = str(uuid.uuid4())
    filename = str(ts) + format
    return filename


def create_file(image: File, path: str):
    filename = create_file_name('.png')
    if image is not None:
        with open(f"{settings.MEDIA_SRC}{path}/{filename}", "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        return filename, f"{settings.MEDIA_SRC}{path}/{filename}"
    raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Image not found",
        )


def get_utc_timestamp():
    """Converts a datetime object to UTC timestamp

    naive datetime will be considered UTC.

    """

    return calendar.timegm(datetime.datetime.utcnow().utctimetuple())


def generate_code():
    return random.randrange(0, 999999)


def calc_offset(count, count_pre_page, page):
    pc = count / count_pre_page
    page_count = math.ceil(pc) if pc > 1 else 1
    offset = (page - 1) * count_pre_page
    return offset, page_count


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        rand_name = datetime.datetime.now().timestamp()
        rand_name = str(rand_name).replace(".", "")

        filename = '{}.{}'.format(rand_name, ext)
        return os.path.join(self.path, filename)
