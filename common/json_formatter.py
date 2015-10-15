# encoding: utf-8
import logging
import sys

import logstash

from common.formatter import LogstashFormatterV1


class JsonFormatter(object):
    """
    The LogstashFormatter may take the following named parameters:

    fmt: Config as a JSON string that supports:
    extra: provide extra fields always present in logs.
    source_host: override source host name.
    json_cls: JSON encoder to forward to json.dump.
    json_default: Default JSON representation for unknown types, by default
    coerce everything to a string.
    """
    def json_v1(self):
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = LogstashFormatterV1()

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return handler

    def udp(self):
        host = 'localhost'
        test_logger = logging.getLogger('python-logstash-logger')
        test_logger.setLevel(logging.INFO)
        test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))
        # test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))
        test_logger.error('python-logstash: test logstash error message.')
        test_logger.info('python-logstash: test logstash info message.')
        test_logger.warning('python-logstash: test logstash warning message.')
        # add extra field to logstash message
        extra = {
            'test_string': 'python version: ' + repr(sys.version_info),
            'test_boolean': True,
            'test_dict': {'a': 1, 'b': 'c'},
            'test_float': 1.23,
            'test_integer': 123,
            'test_list': [1, 2, '3'],
        }
        test_logger.info('python-logstash: test extra fields', extra=extra)
        return test_logger

    def amqp(self):
        test_logger = logging.getLogger('python-logstash-logger')
        test_logger.setLevel(logging.INFO)
        test_logger.addHandler(logstash.AMQPLogstashHandler(host='localhost', version=1))
        test_logger.info('python-logstash: test logstash info message.')
        try:
            1/0
        except:
            test_logger.exception('python-logstash-logger: Exception with stack trace!')
        return test_logger
