# -*- coding: utf-8 -*- äöü vim: sw=4 sts=4 ts=8 scrolloff=3 cul si et
from .unbound import getContext

class GetContextMixin(object):
    """
    Mixin-Klasse für getContext-Methode
    """

GetContextMixin.getContext = getContext
