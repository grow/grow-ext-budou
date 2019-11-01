from googleapiclient import discovery
from grow.common import oauth
from grow.common import utils
from jinja2.ext import Extension
import budou
import httplib2
import jinja2


_parser = None

SCOPES = ('https://www.googleapis.com/auth/cloud-platform',)
STORAGE_KEY = 'Grow SDK - Budou'
SUPPORTED_LANGUAGES = [
    'ja',
    'ko',
    'zh',
    'zh_Hans',
    'zh_Hant',
]


def _get_parser():
    global _parser
    if _parser is None:
        credentials = oauth.get_or_create_credentials(
            scope=SCOPES, storage_key=STORAGE_KEY)
        http = httplib2.Http(ca_certs=utils.get_cacerts_path())
        http = credentials.authorize(http)
        service = discovery.build('language', 'v1beta2', http=http)
        _parser = budou.get_parser('nlapi', service=service)
    return _parser


@jinja2.contextfilter
def do_budou(context, value, options=None):
    if options is None:
        options = {}

    doc = context.get('doc')
    if doc.locale and doc.locale.language in SUPPORTED_LANGUAGES:
        data = _get_parser().parse(value, **options)
        return jinja2.Markup(data['html_code'])
    return value


class BudouExtension(Extension):
    def __init__(self, environment):
        super(BudouExtension, self).__init__(environment)
        environment.filters['budou'] = do_budou
