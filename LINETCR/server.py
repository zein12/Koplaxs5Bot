# -*- coding: utf-8 -*-
import re, json, requests, urllib

class LineServer(object):
    LINE_HOST_DOMAIN            = 'https://gd2.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gd2.line.naver.jp/mh/api'

    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'

    USER_AGENT  = 'Line/5.3.3'
    APP_NAME    = 'DESKTOPMAC\t5.3.3-YOSEMITE-x64\tMAC\t10.12.0'
    PHONE_NAME  = 'IOS\t7.13.1\tiPhone OS\t10.12.0'
    CARRIER     = '1-0'
    SYSTEM_NAME = 'FDLRCN'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    _session    = requests.session()
    channelHeaders  = {}
    Headers         = {}

    def __init__(self):
        self.Headers = {}
        self.channelHeaders = {}

    def parseUrl(self, path):
        return self.LINE_HOST_DOMAIN + path

    def urlEncode(self, url, path, params=[]):
        try:        # Works with python 2.x
            return url + path + '?' + urllib.urlencode(params)
        except:     # Works with python 3.x
            return url + path + '?' + urllib.parse.urlencode(params)

    def getJson(self, url, allowHeader=False):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            return json.loads(self._session.get(url, headers=self.Headers).text)

    def setHeaders(self, argument, value):
        self.Headers[argument] = value

    def setChannelHeaders(self, argument, value):
        self.channelHeaders[argument] = value

    def postContent(self, url, data=None, files=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.post(url, headers=headers, data=data, files=files)

    def getContent(self, url, headers=None):
        if headers is None:
            headers=self.Headers
return self._session.get(url, headers=headers, stream=True)
