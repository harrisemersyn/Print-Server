from config import LDAPConfig, get_config

class User:
  username: str

  def __init__(self, username: str) -> None:
    self.username = username

def auth(username: str, password: str) -> User:
  '''
  Authenticate using the mode specified in `config.toml`

  Returns a user or None if the credentials are invalid
  '''

  auth_mode = get_config().auth_mode
  if auth_mode == 'test':
    return auth_test(username, password)
  elif auth_mode == 'citadel':
    return auth_citadel(username, password, get_config().ldap)
  
  # Unreachable because of config.py validation
  return None

def auth_test(username: str, password: str) -> User:
  '''
  Test authentication

  Do not use this in production. It is primarily for testing before proper
  authentication is method and when it is not possible to authenticate to
  Citadel (i.e. running on Windows).

  Returns a user or None if the credentials are invalid
  '''

  if username == 'print' and password == 'server':
    return User(username)
  else:
    return None

conn = None
ldap_config = None

def auth_citadel(username: str, password: str, config: LDAPConfig) -> User:
  '''
  Citadel authentication

  Requires python-ldap, which only runs on linux.

  Returns a user or None if the credentials are invalid
  '''

  import ldap

  global conn

  if conn is None:
    try:
      conn = ldap.initialize(config.host)
    except:
      raise RuntimeError(f'Failed to connect to LDAP host {config.host}')

  # TODO: I'm not sure if interpolating the username like this is a vulnerabiltiy,
  # what could an attacker do? Anyways, should validate that the username only
  # contains allowable characters (probably alphanumeric and '-' and '_')
  try:
    conn.simple_bind_s(f'uid={username},{config.base_dn}', password)
    return User(username)
  except:
    return None
