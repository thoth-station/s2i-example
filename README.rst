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
  oc process -f https://raw.githubusercontent.com/thoth-station/s2i-example-tensorflow/master/openshift.yaml | oc apply -f -

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

See `thoth-station/s2i-thoth <https://github.com/thoth-station/s2i-thoth>`_ for
more info and a list of Thoth's base images with configuration options you can
supply.

Follow instructions present in `Thamos repository
<https://github.com/thoth-station/thamos#using-thoth-and-thamos-in-openshifts-s2i>`_
for more info on how to configure Thoth's client - "Thamos".

See also build config present in this repo to see configuration options
supplied to this s2i based Python application.

