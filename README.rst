| |pypi| |license| |docs|
| |sonar_maintainability| |sonar_reliability| |sonar_security|

Supports Python ``2.7+`` and ``3.3+``.

Module based on `steam <https://github.com/ValvePython/steam/>`_
for interacting with CSGO's Game Coordinator.

**Documentation**: http://csgo.readthedocs.io

| Note that this module should be considered an alpha.
| Contributions and suggestion are always welcome.


How to create python proto file
------------

1. add link to proto file to proto_list.txt
2. add proto module name tp gen_enum_from_protos.py (_proto_modules)
3. run `make pb_update`
4. optionally add proto files than are needed by your proto file to proto_list.txt


Installation
------------

Install latest version from PYPI::

    pip install -U csgo

Install the current dev version from ``github``::

    pip install git+https://github.com/ValvePython/csgo


.. |pypi| image:: https://img.shields.io/pypi/v/csgo.svg?style=flat&label=latest%20version
    :target: https://pypi.python.org/pypi/csgo
    :alt: Latest version released on PyPi

.. |license| image:: https://img.shields.io/pypi/l/csgo.svg?style=flat&label=license
    :target: https://pypi.python.org/pypi/csgo
    :alt: MIT License

.. |docs| image:: https://readthedocs.org/projects/csgo/badge/?version=latest
    :target: http://csgo.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation status

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=ValvePython_csgo&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard?id=ValvePython_csgo
    :alt: SonarCloud Rating

.. |sonar_reliability| image:: https://sonarcloud.io/api/project_badges/measure?project=ValvePython_csgo&metric=reliability_rating
    :target: https://sonarcloud.io/dashboard?id=ValvePython_csgo
    :alt: SonarCloud Rating

.. |sonar_security| image:: https://sonarcloud.io/api/project_badges/measure?project=ValvePython_csgo&metric=security_rating
    :target: https://sonarcloud.io/dashboard?id=ValvePython_csgo
    :alt: SonarCloud Rating
