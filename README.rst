s2i-thoth-example
-----------------

This is an example S2I application which uses Thoth's recommendations to
recommend a TensorFlow stack.

Usage
=====

To deploy this application to OpenShift:

.. code-block:: console

  oc project <YOUR-PROJECT-NAME>
  oc process -f openshift.yaml | oc apply -f -

The BuildConfig is using UBI8 Pythpn 3.6 to build the application.

Once the templates get applied, a build is started. As there is no
``Pipfile.lock`` present (no locked dependencies), Thoth is contacted (see
``thoth_conf_template.yaml`` configuration file for info on configuration
options).

Thoth computes recommendations and gives back a ``Pipfile.lock`` with
additional guidance on software stack (see build logs). Note that computing
recommendations takes some time, there is assigned a certain amount of CPU based
on Thoth's backend configuration (typically you get back results for a
TensorFlow stack in less than 2 minutes, but this varies based on load in Thoth
deployment). Results are cached (3 hours by default) so next builds for same
stack and same software/hardware configuration are faster (unless forced or any
configuration change on client side). The cache is by default omitted as there
is set `THAMOS_FORCE` configuration option in the ``openshift.yaml`` file.

The adviser on Thoth's side is run in debug mode (see `THAMOS_DEBUG`
configuration option in the ``openshift.yaml`` file).

You can configure which Thoth deployment should be contacted by setting
`THOTH_HOST` environment variable which is used during expansion of
``.thoth.yaml`` file from ``thoth_conf_template.yaml`` template file. See also
other parts which get expanded based on software and hardware detection
performed during the build process.

To remove this application from OpenShift:

.. code-block:: console

  oc delete all --selector 'app=s2i-example-tensorflow'


Using Thoth in your s2i builds
==============================

To enable Thoth in your s2i builds, copy content of `.s2i` directory present in
this repository into your Git repository which is s2i enabled and remove
``Pipfile.lock`` from your repository (locking is left on Thoth based on the
recommendation engine). And thats it!

Follow instructions present in `<https://github.com/thoth-station/thamos> Thamos
repository`_ for more info.

