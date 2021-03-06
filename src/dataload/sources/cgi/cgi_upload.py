import biothings.dataload.uploader as uploader
from dataload.uploader import SnpeffPostUpdateUploader


class CgiUploader(uploader.DummySourceUploader, SnpeffPostUpdateUploader):
    name = "cgi"
    __metadata__ = {"mapper": 'observed',
                    "assembly": "hg19",
                    "src_meta": {
                        "url": "https://www.cancergenomeinterpreter.org/home",
                        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
                        "license_url_short": "https://goo.gl/wtye9y",
                        "licence": "CC0 1.0 Universal",
                    }
                    }

    @classmethod
    def get_mapping(self):
        mapping = {
            "cgi": {
                "properties": {'association': {'analyzer': 'string_lowercase', 'type': 'string'},
                               'cdna': {'analyzer': 'string_lowercase', 'type': 'string'},
                               'drug': {'analyzer': 'string_lowercase', 'type': 'string'},
                               'evidence_level': {'analyzer': 'string_lowercase', 'type': 'string'},
                               'gene': {'analyzer': 'string_lowercase', 'type': 'string'},
                               'primary_tumor_type': {'analyzer': 'string_lowercase', 'type': 'string'},
                               'protein_change': {'analyzer': 'string_lowercase', 'type': 'string'},
                               'region': {'analyzer': 'string_lowercase', 'type': 'string'},
                               'source': {'analyzer': 'string_lowercase', 'type': 'string'},
                               'transcript': {'analyzer': 'string_lowercase', 'type': 'string'}}
            }
        }
        return mapping
