from import_shims.warn import warn_deprecated_import

warn_deprecated_import('commerce.api.v1.tests', 'lms.djangoapps.commerce.api.v1.tests')

from lms.djangoapps.commerce.api.v1.tests import *
