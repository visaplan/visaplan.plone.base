.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

===================
visaplan.plone.base
===================

This package simply collects some basic constants etc. (e.g. permission names)
which are used by other packages, e.g. ``visaplan.plone.browsers``.

The purpose of this package is *not* to provide new functionality
but to factor out existing functionality from an existing monolitic Zope product.
Thus, it is more likely to lose functionality during further development
(as parts of it will be forked out into their own packages,
or some functionality may even become obsolete because there are better
alternatives in standard Plone components).


Features
--------

- ``exceptions`` module


Examples
--------

This add-on can be seen in action at the following sites:

- https://www.unitracc.de
- https://www.unitracc.com



Installation
------------

Install visaplan.plone.base by adding it to your buildout::

    [buildout]

    ...

    eggs =
        visaplan.plone.base


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/visaplan/visaplan.plone.base/issues
- Source Code: https://github.com/visaplan/visaplan.plone.base


Support
-------

If you are having issues, please let us know;
please use the issue tracker mentioned above.


License
-------

The project is licensed under the GPLv2.

.. vim: tw=79 cc=+1 sw=4 sts=4 si et
