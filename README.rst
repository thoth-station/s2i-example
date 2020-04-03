Thoth's TensorFlow stack guidance example
-----------------------------------------

**See different branches for different examples**

This is an example of an application which uses Thoth's recommendations to
recommend a TensorFlow stack for a specific hardware. The application is
showing a generic approach how to integrate inside OpenShift's s2i build
process or using Thamos CLI.

OpenShift s2i - Source-To-Image
===============================

To have recommendations suited for your specific hardware, you need to
configure the build to be done on a the hardware where the application is
supposed to be run (specific node placement for build and application run which
should match).  This helps to explore available hardware during the application
build. Hardware information together with the environment configuration (base
container image) are subsequently sent to Thoth's recommendation engine to
perform resolving of TensorFlow's dependencies.

To deploy this application to OpenShift:

.. code-block:: console

  oc project <YOUR-PROJECT-NAME>
  oc process -f https://raw.githubusercontent.com/thoth-station/s2i-example/master/openshift.yaml | oc apply -f -

The BuildConfig is using Fedora 31 Python 3.7 as a base for the application.

Once the templates get applied, a build is started. As the build is configured
to ask Thoth for advises, Thoth is contacted (see ``thoth_conf_template.yaml``
configuration file for info on configuration options).

Thoth computes recommendations and gives back a ``Pipfile.lock`` with
additional guidance on software stack (see build logs). Note that computing
recommendations takes some time, there is assigned a certain amount of CPU
based on Thoth's backend configuration. Results are cached (3 hours by default)
so next builds for the same stack and same software/hardware configuration are
faster (unless forced or any configuration change on client side).

To remove this application from OpenShift:

.. code-block:: console

  oc delete all --selector 'app=s2i-example-tensorflow'

Adjusting configuration options
###############################

See comments in the BuildConfig available in the repo as well as
`thoth-station/s2i-thoth <https://github.com/thoth-station/s2i-thoth>`_ for
more info. The repo stated also provides a list of Thoth's base images with
configuration options you can supply.

Follow instructions present in `Thamos repository
<https://github.com/thoth-station/thamos#using-thoth-and-thamos-in-openshifts-s2i>`_
for more info on how to configure Thoth's client - "Thamos".

See also build config present in this repo to see configuration options
supplied to this s2i based Python application.

Thamos CLI
==========

Another integration point for Thoth is `Thamos
<https://pypi.org/project/thamos>`_. You can use Thoth's recommendation engine
directly from within your terminal. First, you need to clone this repo and
install Thamos CLI:

.. code-block:: console

  git clone https://github.com/thoth-station/s2i-example.git && cd s2i-example
  pip3 install thamos
  thamos --help

The pre-configured template for Thamos CLI is available in the
``.thoth.yaml`` file:

.. code-block:: console

  cat .thoth.yaml

To generate Thoth's configuration file out of the template run the
following command:

.. code-block:: console

  thamos config --no-interactive --template thoth_conf_template.yaml
  cat .thoth.yaml  # to browse the content of the config file

Now you are ready to ask for advises:

.. code-block:: console

  thamos advise

This might take some time. Once Thoth recommends you the application stack to
be used, run the application, create a Python environment and install
requirements into it:

.. code-block:: console

  cat requirements.txt  # check requirements with digests
  cat requirements.in   # check direct dependencies
  python3 -m venv venv/
  source venv/bin/activate
  pip3 install -r requirements.txt

And finally, run the application (the virtual environment needs to be still
activated):

.. code-block:: console

  python3 ./app.py

To browse Thoth's logs during adviser run:

.. code-block:: console

  thamos log
