
from basistheory import api


class RequestOptions(object):
  def __init__(self, api_key=None, correlation_id=None):
    self.api_key = api_key
    self.correlation_id = correlation_id
  