import string
import random

class TinyURL:
    def __init__(self):
        self.url_map = {}
        self.key_map = {}
        self.base_url = "http://tinyurl.com/"
        self.chars = string.ascii_letters + string.digits

    def _generate_key(self, length=6):
        return ''.join(random.choice(self.chars) for _ in range(length))

    def encode(self, long_url):
        if long_url in self.url_map:
            return self.base_url + self.url_map[long_url]
        key = self._generate_key()
        while key in self.key_map:
            key = self._generate_key()
        self.url_map[long_url] = key
        self.key_map[key] = long_url
        return self.base_url + key

    def decode(self, short_url):
        key = short_url.replace(self.base_url, '')
        return self.key_map.get(key, None)


service = TinyURL()
short = service.encode("https://www.example.com")
print("Short URL:", short)
original = service.decode(short)
print("Original URL:", original)
