On `IPython 7.13.0`:

`activate_env` functional magic methods.
`%python`
`%%python (%%script python)`


```py
import os
import sys
from IPython import get_ipython
from IPython.core.magics import ScriptMagics, PackagingMagics
from IPython.core.magic import Magics, magics_class, line_magic

#%alias python "sys.executable"
%alias_magic python run

# ------------------------------------------- #

def _activate_env(f):
    import os
    import sys

    OLD_PATH = os.environ['PATH']
    ENV_PATH = os.path.dirname(sys.executable)
    #NEW_PATH = ':'.join([self.ENV_PATH, self.OLD_PATH])
    if not OLD_PATH.split(':')[0] == ENV_PATH:
        os.environ['PATH'] = ':'.join([ENV_PATH, OLD_PATH])
    return f

# ------------------------------------------- #

class EnvScriptMagics(ScriptMagics):

#     @_activate_env
#     @line_magic("python")
#     def run_python(self, line):
#         print('python activated')
#         if cell is None:
#             self.shell.system(' '.join([sys.executable, line]))

    @_activate_env
    def shebang(self, line, cell):
        super(ScriptMagics, self).shebang(line, cell)

        
def load_ipython_extension(ipython):
    """
    Any module file that define a function named `load_ipython_extension`
    can be loaded via `%load_ext module.path` or be configured to be
    autoloaded by IPython at startup time.
    """
    # You can register the class itself without instantiating it.  IPython will
    # call the default constructor on it.
    ipython.register_magics(EnvScriptMagics)

# # ------------------------------------------- #
@magics_class
class EnvRunMagics(PackagingMagics):

    @line_magic("python")
    def python(self, line):
        import sys
        print('python activated')
        self.shell.system(' '.join([sys.executable, line]))
#         # super(EnvRunMagics, self).pip(line) #self.shell.system(' '.join([sys.executable, line]))


#get_ipython().register_magics(EnvRunMagics)
```

