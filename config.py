# -*- coding: utf-8 -*-
import argparse, ConfigParser, os

class Config:
    """
    Parses command line arguments and wormgame.ini
    Expects a setting file with following structure:
    [settings]
    arg1=value1
    arg2=value2
    ...
    """

    def __init__(self):
        self.cmd_line_args = self.parse_cmdline_args()
        self.config_file_args = self.parse_config_file()
        
    def parse_cmdline_args(self):
        parser = argparse.ArgumentParser(prog='Wormgame', description='Configurate the Wormgame.')
        parser.add_argument('-host', choices='01', help='Is the client host or not (1/0)')
        parser.add_argument('-ip', help='listen in IP')
        parser.add_argument('-port', type=int, help='listen in PORT')
        parser.add_argument('-name', help='NAME of the server')
        #parser.add_argument('-players', type=int, choices=range(1,65), help='number of players')
    
        args = parser.parse_args()
        return args

    def old_parse_config_file(self):
        conf_dict = {}
        f = open('wormgame.ini', 'r')
        for line in f:
            data = line.split('=')
            temp_dict = {data[0]:data[1].strip()}
            conf_dict.update(temp_dict)
        f.close()
        
        return conf_dict
        
    def parse_config_file(self):
        parser = ConfigParser.SafeConfigParser()
        parser.readfp(open('wormgame.ini'))
        
        conf_dict = {}
        items = ['network', 'keys']
        
        for i in items:
            conf_dict.update(parser.items(i))
        
        #return conf_dict
        return parser
        
    
if __name__ == "__main__":
    # Test code
    conf = Config()
    print vars(conf.cmd_line_args)
    print conf.config_file_args.get('keys', 'left')
    