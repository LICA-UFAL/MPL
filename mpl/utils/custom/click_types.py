import os
import click 

class Choice_file(click.Choice):
    name = "choice"
    def __init__(self,files_paths, description):
        self.files_paths = files_paths + ["custom"]
        self.description = description
        super().__init__(self.files_names)

    
    def convert(self, value, param, ctx):
        try:
            value_index = int(value)
            if value_index == len(self.files_paths) - 1:
                return click.prompt(self.description, type = click.Path())
            else:
                return self.files_paths[value_index]
        except ValueError as e:
            self.fail('invalid choice: %s. (choose from %s)' %
                  (value, ', '.join(self.files_names)), param, ctx)
        except IndexError as e:
            self.fail('invalid choice: %s. (choose from %s to %s)' %
                  (value, 0, str(len(self.files_names) - 1)), param, ctx)

    def __repr__(self):
        return 'Choice(%r)' % list(self.files_names)

    @property
    def files_names(self):
        return [str(count) + " - " + os.path.basename(file_path) for count,file_path in enumerate(self.files_paths)]
