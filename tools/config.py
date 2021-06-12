import configparser
import optparse
import os
import sys
import release
from config import dictlogging


class MyOption (optparse.Option, object):
    """ optparse Option with two additional attributes.

    The list of command line options (getopt.Option) is used to create the
    list of the configuration file options. When reading the file, and then
    reading the command line arguments, we don't want optparse.parse results
    to override the configuration file values. But if we provide default
    values to optparse, optparse will return them and we can't know if they
    were really provided by the user or not. A solution is to not use
    optparse's default attribute, but use a custom one (that will be copied
    to create the default values of the configuration file).

    """

    def __init__(self, *opts, **attrs):
        self.my_default = attrs.pop('my_default', None)
        super(MyOption, self).__init__(*opts, **attrs)


class confitgmanager(object):
    def __init__(self) -> None:

        self.options = {
            'test': 'test',
            'logging_config': dictlogging.LOGGING_CONFIG
        }

        self.casts = {}
        self.misc = {}

        version = "%s %s" % (release.description, release.version)
        self.parser = parser = optparse.OptionParser(version=version, option_class=MyOption)

        group = optparse.OptionGroup(parser, "Common options")
        group.add_option("-c", "--config", dest="config", help="specify alternate config file", my_default='123f')
        parser.add_option_group(group)

        # Copy all optparse options (i.e. MyOption) into self.options.
        for group in parser.option_groups:
            for option in group.option_list:
                if option.dest not in self.options:
                    self.options[option.dest] = option.my_default
                    self.casts[option.dest] = option

        self._parse_config()

    def _parse_config(self, args=None):
        # TODO use appdirs
        rcfilepath = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'config', 'discord-robot.conf')
        print('rcfilepath:', rcfilepath)
        self.rcfile = os.path.abspath(rcfilepath)
        self.load()

    def load(self):
        p = configparser.ConfigParser()
        try:
            p.read([self.rcfile])
            for (name, value) in p.items('options'):
                print(name, value)
                if value == 'True' or value == 'true':
                    value = True
                if value == 'False' or value == 'false':
                    value = False
                self.options[name] = value
            # parse the other sections, as well
            for sec in p.sections():
                print('sec:', sec)
                if sec == 'options':
                    continue
                if not self.misc.has_key(sec):
                    self.misc[sec] = {}
                for (name, value) in p.items(sec):
                    if value == 'True' or value == 'true':
                        value = True
                    if value == 'False' or value == 'false':
                        value = False
                    self.misc[sec][name] = value
        except IOError:
            pass
        except configparser.NoSectionError:
            pass

    def get(self, key, default=None):
        return self.options.get(key, default)

    def __setitem__(self, key, value):
        self.options[key] = value
        if key in self.options and isinstance(self.options[key], basestring) and \
                key in self.casts and self.casts[key].type in optparse.Option.TYPE_CHECKER:
            self.options[key] = optparse.Option.TYPE_CHECKER[self.casts[key].type](self.casts[key], key, self.options[key])

    def __getitem__(self, key):
        return self.options[key]


config = confitgmanager()
