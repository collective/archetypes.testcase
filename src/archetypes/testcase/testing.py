from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class ArchetypesTestcase(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import archetypes.testcase
        xmlconfig.file('configure.zcml',
                       archetypes.testcase,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'archetypes.testcase:default')

ARCHETYPES_TESTCASE_FIXTURE = ArchetypesTestcase()
ARCHETYPES_TESTCASE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(ARCHETYPES_TESTCASE_FIXTURE, ),
                       name="ArchetypesTestcase:Integration")