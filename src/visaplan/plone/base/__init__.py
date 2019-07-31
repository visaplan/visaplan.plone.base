"""\
visaplan.plone.base: simple base modules
"""
from logging import getLogger
logger = getLogger(__package__)
try:
    # "BrowserView implements Interface":
    from .browserview import BrowserView
    from zope.interface import implements, Interface
    from .adapter import Base

    from Products.CMFCore.utils import getToolByName
except ImportError as e:
    logger.error('Install failed: %(e)s', locals())
else:
    logger.info('Initialized successfully.')
