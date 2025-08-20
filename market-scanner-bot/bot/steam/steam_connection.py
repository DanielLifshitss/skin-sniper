from steampy.client import SteamClient

def steam_client_session_decorator(api_key, username, password, steamguard_path):
    """
    A decorator to manage a synchronous SteamClient session.
    It handles login and automatic logout for the decorated function.
    """
    def wrapper(func):
        def wrapped_func(*args, **kwargs):
            with SteamClient(api_key) as client:
                client.login(username, password, steamguard_path)
                return func(client, *args, **kwargs)
        return wrapped_func
    return wrapper

