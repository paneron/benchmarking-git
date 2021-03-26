import glob
import yaml
import string
import random
import pathlib

from uuid import uuid4, uuid5, NAMESPACE_OID as ns_oid

import config as cfg

# top level directory:


tld = [
    'ara',
    'ces',
    'deu',
    'eng',
    'fin',
    'fra',
    'ita',
    'jpn',
    'kor',
    'mon',
    'nld',
    'nno',
    'nob',
    'pol',
    'por',
    'rus',
    'slv',
    'spa',
    'srp',
    'swe',
    'uni',
    'zho',
]

data_template = {
    'data': {
        'digit': 0,
        'designation': '',
        'destination': '',
        'examples': [],
        'notes': [],
        'testStringStatus': None,
        'type': 'test item',
        'randId': ''
    },
    'dateAccepted': '2018-11-17',
    'id': '',
    'status': ''
}

statuses = ['standart', 'non standart', 'experimental', 'unknown']


def save_yaml_a(uuid, dname, data):
    file_path = '%s/a/subregisters/%s/%s/%s' % (cfg.output_dir, dname, uuid[0:4], uuid[4:8])
    pathlib.Path(file_path).mkdir(parents=True, exist_ok=True)
    file = open('%s/%s.yaml' % (file_path, uuid), 'w')
    file.write(yaml.dump(data, allow_unicode=True))
    file.close()


def save_yaml_b(uuid, dname, data):
    file_path = '%s/b/subregisters/%s' % (cfg.output_dir, dname)
    pathlib.Path(file_path).mkdir(parents=True, exist_ok=True)
    file = open('%s/%s.yaml' % (file_path, uuid), 'w')
    file.write(yaml.dump(data, allow_unicode=True))
    file.close()


def rnd_str(lng):
    return ''.join(random.choices(string.ascii_lowercase, k=lng))


def make_item():
    result = data_template
    result['data']['testStringStatus'] = bool(random.getrandbits(1))
    result['data']['designation'] = rnd_str(36)
    result['data']['destination'] = rnd_str(48)

    _l = []
    for i in range(0, random.randint(2, 7)):
        _l.append('%s %s' % (rnd_str(random.randint(8, 24)), rnd_str(random.randint(11, 21))))
    result['data']['examples'] = _l
    del _l

    _l = []
    for i in range(0, random.randint(3, 9)):
        _l.append(rnd_str(random.randint(11, 16)))
    result['data']['notes'] = _l
    del _l

    result['data']['digit'] = random.randint(1, 9)
    result['data']['randId'] = str(uuid4())

    result['status'] = statuses[random.randint(0, 3)]

    result['id'] = str(uuid5(ns_oid, str(result)))

    return result


for lang in tld:
    print(lang)
    for i in range(0, cfg.files_per_lng):
        item = make_item()
        save_yaml_a(item['id'], lang, item)
        save_yaml_b(item['id'], lang, item)
