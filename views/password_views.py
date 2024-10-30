import base64
import hashlib
import secrets
import string
from pathlib import Path


class FernetHasher:
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent
    KEY_DIR = BASE_DIR / "keys"

    @classmethod
    def _get_random_string(cls, lenght=25):
        randstr = ''
        for i in range(lenght):
            randstr = randstr + secrets.choice(cls.RANDOM_STRING_CHARS)
        return randstr

    @classmethod
    def create_key(cls, archive=False):
        value = cls._get_random_string(lenght=5)
        hasher = hashlib.sha256(value.encode('utf-8')).digest()
        key = base64.b64encode(hasher)
        if archive:
            return key, cls.archive_key(key)
        return key, None

    @classmethod
    def archive_key(cls, key):
        file = 'key.key'
        while Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(lenght=5)}.key'
        with open(cls.KEY_DIR / 'key.txt', 'wb') as arq:
            arq.write(key)
        return cls.KEY_DIR / file


FernetHasher.create_key()
