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

    atapi.TextField(
        name='body',
        required=True,
        searchable=True,
        default_output_type='text/html',
        allowable_content_types=(
            'text/plain',
            'text/restructured',
            'text/html',
            'application/msword',
        ),
        widget=atapi.RichWidget(
            description='Enter or upload text for the body of the document.',
        ),
    ),

    atapi.StringField(
        name='contactName',
        languageIndependent=True,
        widget=atapi.StringWidget(
            description='Enter a contact person.',
        ),
    ),

    atapi.StringField(
        name='contactName2',
        languageIndependent=True,
        widget=atapi.StringWidget(
            description='Enter a contact person.',
        ),
    ),

    atapi.StringField(
        name='contactName3',
        languageIndependent=True,
        widget=atapi.StringWidget(
            description='Enter a contact person.',
        ),
    ),

    atapi.StringField(
        name='contactName4',
        languageIndependent=False,
        accessor='getFourthContactName',
        mutator='setFourthContactName',
        widget=atapi.StringWidget(
            description='This field has custom accessor and mutator.',
        ),
    ),

    atapi.StringField(
        name='contactName5',
        languageIndependent=True,
        accessor='getFifthContactName',
        mutator='setFifthContactName',
        widget=atapi.StringWidget(
            description='This field has custom accessor and mutator.',
        ),
    ),

    atapi.StringField(
        name='langIndependentInBase',
        languageIndependent=True,
        widget=atapi.StringWidget(
            description='This field is language independent in SimpleType.',
        ),
    ),

    atapi.StringField(
        name='langIndependentInDerived',
        languageIndependent=False,
        widget=atapi.StringWidget(
            description='This field is language dependent in DerivedType.',
        ),
    ),

    atapi.StringField(
        name='langIndependentInBoth',
        languageIndependent=True,
        widget=atapi.StringWidget(
            description='This field is language independent everywhere.',
        ),
    ),

    atapi.ImageField(
        name='image',
        languageIndependent=True,
    ),

    atapi.ImageField(
        name='imageDependent',
        languageIndependent=False,
    ),

    atapi.ReferenceField(
        name='reference',
        allowed_types=('SimpleType', ),
        languageIndependent=True,
        relationship='referenceType',
    ),

    atapi.ReferenceField(
        name='referenceDependent',
        allowed_types=('SimpleType', ),
        languageIndependent=False,
        relationship='referenceDependentType',
    ),

    atapi.ReferenceField(
        name='referenceMulti',
        allowed_types=('SimpleType', ),
        languageIndependent=True,
        multiValued=True,
        relationship='referenceType',
    ),

    atapi.LinesField(
        name='lines',
        languageIndependent=True,
        widget=atapi.LinesWidget(label="Lines"),
    ),

    atapi.TextField(
        name='neutralText',
        languageIndependent=True,
        default_output_type='text/html',
        widget=atapi.RichWidget(
            description='Enter some text',
        ),
    ),

))


schemata.finalizeATCTSchema(SimpleTypeSchema, moveDiscussion=False)


class SimpleType(base.ATCTContent):
    """A simple type for testing multilingual"""
    implements(ISimpleType)

    meta_type = "SimpleType"
    schema = SimpleTypeSchema

    # def setContactName(self, value, **kw):
    #     """Set contact name.
    #     This tests language independent method generation
    #     """
    #     self.getField('contactName').set(self, value, **kw)
    #     self.testing = value

    def getFourthContactName(self):
        """Custom accessor."""
        return 'getFourthContactName'

    def setFourthContactName(self, value, **kw):
        """Custom mutator."""
        self.getField('contactName4').set(self, 'cn4 ' + value, **kw)

    def getFifthContactName(self):
        """Custom accessor."""
        return 'getFifthContactName'

    def setFifthContactName(self, value, **kw):
        """Custom mutator."""
        self.getField('contactName5').set(self, 'cn5 ' + value, **kw)

    def getRawReference(self):
        return self.getField('reference').getRaw(self)

    def getRawReferenceDependent(self):
        return self.getField('referenceDependent').getRaw(self)

atapi.registerType(SimpleType, PROJECTNAME)
