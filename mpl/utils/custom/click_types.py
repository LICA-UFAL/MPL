import os
import click 

class ChoiceElement(click.Choice):
    name = "choice"
    def __init__(self, elements, description):
        self.elements = ["None" ,"custom"] + elements
        self.description = description
        super().__init__(self.elements_with_index)

    def convert(self, value, param, ctx):
        try:
            value_index = int(value)
            if value_index == 0:
                return None
            elif value_index == None:
                return click.prompt(self.description, type = click.Path())
            else:
                return self.elements[value_index]

        except ValueError as e:
            self.fail('invalid choice: %s. (choose from %s)' %
                  (value, ', '.join(self.elements_with_index)), param, ctx)
        except IndexError as e:
            self.fail('invalid choice: %s. (choose from %s to %s)' %
                  (value, 0, str(len(self.elements_with_index) - 1)), param, ctx)

    def __repr__(self):
        return 'Choice(%r)' % list(self.elements_with_index)

    @property
    def elements_with_index(self):
        return [str(count) + " - " + str(element) for count,element in enumerate(self.elements)]
