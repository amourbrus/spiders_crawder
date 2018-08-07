# -*- coding: utf-8 -*-
import random

from settings import USER_AGENT_LIST

import logging



class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent

        # 主要不要return request给引擎，不然引擎会认为是下载失败的请求，会重新加入调度器请求队列


class ProxyMiddleware(object):
    def process_request(self, request, spider):

        # 验证代理格式
        # proxy = "http://maozhaojun:ntkn0npx@115.28.141.184:16818"
        # request.meta['proxy'] = proxy
        pass