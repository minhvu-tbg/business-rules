from business_rules.variables import BaseVariables, rule_variable, TYPE_STRING
from unittest2 import TestCase

class VariablesClassTests(TestCase):
    """ Test methods on classes that inherit from BaseVariables
    """
    def test_base_has_no_variables(self):
        self.assertEqual(len(BaseVariables.get_all_variables()), 0)

    def test_get_all_variables(self):
        """ Returns a dictionary listing all the functions on the class that
        have been decorated as variables, with some of the data about them.
        """
        class SomeVariables(BaseVariables):

            @rule_variable(TYPE_STRING)
            def this_is_rule_1(self):
                return "blah"

            def non_rule(self):
                return "baz"

        vars = SomeVariables.get_all_variables()
        self.assertEqual(len(vars), 1)
        self.assertEqual(vars[0]['name'], 'this_is_rule_1')
        self.assertEqual(vars[0]['description'], 'This Is Rule 1')
        self.assertEqual(vars[0]['return_type'], TYPE_STRING)
        self.assertEqual(vars[0]['options'], [])

        # should work on an instance of the class too
        self.assertEqual(len(SomeVariables().get_all_variables()), 1)
