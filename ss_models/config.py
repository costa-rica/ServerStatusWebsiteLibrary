import os
from ss_config import ConfigDev, ConfigProd, ConfigWorkstation

match os.environ.get('FSW_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- ss_models/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- ss_models/config: Production')
    case _:
        config = ConfigWorkstation()
        print('- ss_models/config: Local')
    