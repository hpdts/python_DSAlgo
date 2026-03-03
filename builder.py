"""
string url 
scheme
host

queryParams({"key1": "value1", "key2": "value2"})


content_copy
 both ?key1=value1&key2=value2
content_copy
 and ?key2=value2&key1=value1
"""
class UrlBuilder:
    def __init__(self):
        self.scheme = 'http://'
        self.host_var = None
        self.port_var = None
        self.path_var = None
        self.query = {}

    def https(self):
        self.scheme = 'https://'
        return self

    def host(self, host_str):
        self.host_var = host_str
        return self

    def port(self, port_int):
        self.port_var = port_int
        return self

    def path(self, path_arg):
        self.path_var = path_arg
        return self

    def query_params(self, params : dict):
        self.query.update(params)
        return self
    
    def parse_query_params_wrong(self):
        query_params_local = '?'
        for key,val in self.query.items():
            #val = query_params_arg[key]
            #print(f"key: {key} val: {val}")
            query_params_local+=f"{key}={val}&"
        #char last char for &
        return query_params_local

    def parse_query_params(self):
        if not self.query:
            return ""

        query_string = "&".join(
            f"{key}={val}" for key, val in self.query.items()
        )

        return f"?{query_string}"

    def build(self):
        #print("herere")
        url = ''
        url=self.scheme
        if self.host_var:
            url+=self.host_var
        if self.port_var:
            url+=":" + str(self.port_var)
        if self.path_var:
            url+=self.path_var
        #if self.query:
            #print(self.query)
            #self.url+=parse_query_params(self.query_params)
            url+=self.parse_query_params()
        return url

ur = UrlBuilder()
assert ur.https().build() == 'https://'


def test_builder():
    # Basic URL
    url = UrlBuilder().host("example.com").build()
    assert url == "http://example.com"

    # HTTPS
    url = UrlBuilder().https().host("example.com").build()
    assert url == "https://example.com"

    # With port
    url = UrlBuilder().host("example.com").port(8080).build()
    assert url == "http://example.com:8080"

    # With path
    url = UrlBuilder().host("example.com").path("/test").build()
    assert url == "http://example.com/test"

    # With query params (single)
    url = UrlBuilder().host("example.com").path("/test") \
        .query_params({"key": "value"}).build()

    assert url in [
        "http://example.com/test?key=value"
    ]

    # With multiple query params
    url = UrlBuilder().host("example.com").path("/test") \
        .query_params({"key1": "value1", "key2": "value2"}).build()
    print("url: ", url)
    assert url in [
        "http://example.com/test?key1=value1&key2=value2",
        "http://example.com/test?key2=value2&key1=value1",
    ]

    # With everything
    url = UrlBuilder() \
        .https() \
        .host("www.codility.com") \
        .port(8080) \
        .path("/test/hello/world") \
        .query_params({"key1": "value1", "key2": "value2"}) \
        .build()

    assert url in [
        "https://www.codility.com:8080/test/hello/world?key1=value1&key2=value2",
        "https://www.codility.com:8080/test/hello/world?key2=value2&key1=value1",
    ]

    # Empty query params
    url = UrlBuilder().host("example.com").path("/test") \
        .query_params({}).build()

    assert url == "http://example.com/test"

    # Multiple calls to query_params (merge test)
    url = UrlBuilder().host("example.com").path("/test") \
        .query_params({"a": "1"}) \
        .query_params({"b": "2"}) \
        .build()

    assert url in [
        "http://example.com/test?a=1&b=2",
        "http://example.com/test?b=2&a=1",
    ]

test_builder()
print("all test cases passed")
