from import_shims.warn import warn_deprecated_import

warn_deprecated_import('commerce.tests.test_views', 'lms.djangoapps.commerce.tests.test_views')

from lms.djangoapps.commerce.tests.test_views import *
