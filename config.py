import argparse

class Config:
    """
    Parses command line arguments and wormgame.ini
    """

    def __init__(self):
        self.cmd_line_args = self.parse_cmdline_args()
        self.config_file_args = self.parse_config_file()
        
    def parse_cmdline_args(self):
        parser = argparse.ArgumentParser(description='Configurate the Wormgame.')
        parser.add_argument('--host', type=bool, help='Is the client host or not (True/False)')
        parser.add_argument('--ip', help='listen in IP')
        parser.add_argument('--port', type=int, help='listen in PORT')
        parser.add_argument('--name', help='NAME of the server')
    
        args = parser.parse_args()
        return args

    def parse_config_file(self):
        conf_dict = {}
        f = open('wormgame.ini', 'r')
        for line in f:
            data = line.split('=')
            temp_dict = {data[0]:data[1].strip()}
            conf_dict.update(temp_dict)
        f.close
        
        return conf_dict
    
if __name__ == "__main__":
    # Test code
    conf = Config()
    print vars(conf.cmd_line_args)
    print conf.config_file_args
    