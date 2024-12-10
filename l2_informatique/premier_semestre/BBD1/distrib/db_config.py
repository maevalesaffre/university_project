import configparser

dict_filter = lambda d,l : {k:d[k] for k in d.keys()&l}
dict_exclude = lambda d,l : {k:d[k] for k in d.keys()-l}

def get_from_wallet(host, user) :
    import keyring
    return keyring.get_password(host+'_pg',user)

def get_interactive() :
    import getpass
    return getpass.getpass('password ?')

def get_db_parms(config_section = None, config_file = 'db_parms.ini') :
        conf = configparser.ConfigParser()
        conf.read(config_file)
        config_section = config_section  or conf.sections()[0]
        parms = conf[config_section]
        #print(dict(parms))
        
        password_mode = parms.get('password_mode')
        if password_mode in ('no','false','off') and 'password' in parms :
            del parms['password']
        elif password_mode in ('ask',) :
            parms['password'] = get_interactive() 
        elif password_mode in ('wallet','keyring') :
            parms['password'] = get_from_wallet(parms['host'],parms['user'])
            
        return dict_filter(parms,{'host','user','port','password','dbname'})
