Thoth's TensorFlow stack guidance example
-----------------------------------------

This is an example of OpenShift's s2i (source-to-image) application which uses
Thoth's recommendations to recommend a TensorFlow stack for a specific hardware
where TensorFlow application is supposed to be run together with software
environment (base image).

The application is showing a generic approach and how to integrate inside
OpenShift's s2i build process. To have recommendations suited for your specific
hardware, you need to configure the build to be done on specific hardware where
the application is supposed to be run (specific node placement for build and
application run which should match).

Usage
=====

To deploy this application to OpenShift:

.. code-block:: console

  oc project <YOUR-PROJECT-NAME>
  oc process -f openshift.yaml | oc apply -f -

The BuildConfig is using UBI8 Pythpn 3.6 to build the application.

Once the templates get applied, a build is started. As the build is
configuration to ask Thoth for advises, Thoth is contacted (see
``thoth_conf_template.yaml`` configuration file for info on configuration
options).

Thoth computes recommendations and gives back a ``Pipfile.lock`` with
additional guidance on software stack (see build logs). Note that computing
recommendations takes some time, there is assigned a certain amount of CPU based
on Thoth's backend configuration (typically you get back results for a
TensorFlow stack in less than 2 minutes, but this varies based on load in Thoth
deployment). Results are cached (3 hours by default) so next builds for same
stack and same software/hardware configuration are faster (unless forced or any
configuration change on client side). The cache is by default used in this
example as there is not set `THAMOS_FORCE` configuration option in the
``openshift.yaml`` file.

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

To enable Thoth in your s2i builds, copy the content of `.s2i` directory
present in this repository into your Git repository which is s2i enabled and
remove ``Pipfile.lock`` from your repository (locking is left on Thoth based on
the recommendation engine) or set ``THOTH_ADVISE`` environment variable to `1`
in the build config.

... And thats it!

Configuration options of s2i asseble script:

* ``THOTH_ADVISE`` - always use the recommended stack by Thoth (even if ``Pipfile.lock`` is present in the repo)
* ``THOTH_DRY_RUN`` - submit stack to Thoth's recommendation engine but do not use the recommended ``Pipfile.lock`` file, use the ``Pipfile.lock`` file present in the repo instead

Follow instructions present in `Thamos repository
<https://github.com/thoth-station/thamos>`_ for more info.

