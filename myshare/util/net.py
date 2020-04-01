from io import BytesIO
import pycurl


def request(url, encoding='GBK'):
    buffer = BytesIO()
    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.perform()
    curl.close()
    return buffer.getvalue().decode(encoding)
