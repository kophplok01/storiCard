import base64
import configparser

def read_properties(file_path, key):
    config = configparser.ConfigParser()
    config.read(file_path)
    environment = key[:3].upper()
    if "users.properties" == file_path:
        user = config.get(environment, key)
        email, encoded_password = user.split(',')
        password = base64.b64decode(encoded_password).decode('utf-8')
        email = email.strip()
        password = password.strip()
        return email, password
    if "urls.properties" == file_path:
        if environment == "DEV":
            environment = "development"
        if environment == "ACC":
            environment = "acceptance"
        if environment == "QA":
            environment = "qa"
        return config.get(key[:3].upper(), environment)

