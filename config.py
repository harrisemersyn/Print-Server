from typing import Any, Dict

import toml

def require_field(config: Dict, location: str, key: str, message='') -> Any:
  if key not in config:
    raise ValueError(f'{location} is missing a required field: {key}. {message}')
  return config[key]

class PrintingConfig:
  max_pages: int
  printer_bw: str
  printer_color: str

  def __init__(self, printing_config: Dict) -> None:
    self.max_pages = require_field(printing_config, 'config.toml#printing', 'max_pages')
    self.printer_bw = require_field(printing_config, 'config.toml#printing', 'printer_bw')
    self.printer_color = require_field(printing_config, 'config.toml#printing', 'printer_color')

class LDAPConfig:
  host: str
  base_dn: str

  def __init__(self, ldap_config: Dict) -> None:
    self.host = require_field(ldap_config, 'config.toml#ldap', 'host')
    self.base_dn = require_field(ldap_config, 'config.toml#ldap', 'base_dn')

class Config:
  auth_mode: str
  printing: PrintingConfig
  ldap: LDAPConfig

  def __init__(self, config: Dict) -> None:
    self.auth_mode = require_field(config, 'config.toml', 'auth_mode')
    if self.auth_mode not in ['test', 'citadel']:
      raise ValueError(f'config.toml#auth_mode specifies an invalid value "{self.auth_mode}", expected one of "test", "citadel"')
    
    self.printing = PrintingConfig(require_field(config, 'config.toml', 'printing'))

    if self.auth_mode == 'citadel':
      self.ldap = LDAPConfig(require_field(config, 'config.toml', 'ldap', message='This field is required because auth_mode is set to citadel.'))

global_config: Config = None

def get_config() -> Config:
  '''
  Read and validate the config stored in `config.toml`. Caches the results to
  only read the file once.

  Sample config:

  ```toml
  auth_mode = 'citadel'

  [printing]
  max_copies = 5
  printer_bw = 'black and white printer device name'
  printer_color = 'color printer device name'

  [ldap]
  host = 'ldap://ldap.host.com'
  base_dn = 'cn=baseDnForUsers,dn=ldap,dn=host,dn=com'
  ```
  '''

  global global_config

  if global_config is None:
    config_data = toml.load('config.toml')
    global_config = Config(config_data)

  return global_config
