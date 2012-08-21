"""Definition of the SimpleType content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from archetypes.testcase.interfaces import ISimpleType
from archetypes.testcase.config import PROJECTNAME

SimpleTypeSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))


schemata.finalizeATCTSchema(SimpleTypeSchema, moveDiscussion=False)


class SimpleType(base.ATCTContent):
    """A simple type for testing multilingual"""
    implements(ISimpleType)

    meta_type = "SimpleType"
    schema = SimpleTypeSchema


atapi.registerType(SimpleType, PROJECTNAME)
