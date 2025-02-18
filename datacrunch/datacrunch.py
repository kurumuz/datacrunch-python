from datacrunch.authentication.authentication import AuthenticationService
from datacrunch.balance.balance import BalanceService
from datacrunch.http_client.http_client import HTTPClient
from datacrunch.images.images import ImagesService
from datacrunch.instance_types.instance_types import InstanceTypesService
from datacrunch.instances.instances import InstancesService
from datacrunch.ssh_keys.ssh_keys import SSHKeysService
from datacrunch.startup_scripts.startup_scripts import StartupScriptsService
from datacrunch.constants import Actions, InstanceStatus, ErrorCodes
from datacrunch.__version__ import VERSION


class DataCrunchClient:
    """Client for interacting with DataCrunch's public API"""

    def __init__(self, client_id: str, client_secret: str, base_url: str = "https://api.datacrunch.io/v1") -> None:
        """The DataCrunch client

        :param client_id: client id
        :type client_id: str
        :param client_secret: client secret
        :type client_secret: str
        :param base_url: base url for all the endpoints, optional, defaults to "https://api.datacrunch.io/v1"
        :type base_url: str, optional
        """

        # Constants
        self.actions: Actions = Actions()
        """Available actions to perform on an instance"""

        self.instance_status: InstanceStatus = InstanceStatus()
        """Possible instance statuses"""

        self.error_codes: ErrorCodes = ErrorCodes()
        """Available error codes"""

        self.base_url: str = base_url
        """DataCrunch's Public API URL"""

        self.version: str = VERSION
        """Current SDK Version"""

        # Services
        self._authentication: AuthenticationService = AuthenticationService(
            client_id, client_secret, self.base_url)
        self._http_client: HTTPClient = HTTPClient(
            self._authentication, self.base_url)

        self.balance: BalanceService = BalanceService(self._http_client)
        """Balance service. Get client balance"""

        self.images: ImagesService = ImagesService(self._http_client)
        """Image service"""

        self.instance_types: InstanceTypesService = InstanceTypesService(
            self._http_client)
        """Instance type service"""

        self.instances: InstancesService = InstancesService(self._http_client)
        """Instances service. Deploy, delete, hibernate (etc) instances"""

        self.ssh_keys: SSHKeysService = SSHKeysService(self._http_client)
        """SSH keys service"""

        self.startup_scripts: StartupScriptsService = StartupScriptsService(
            self._http_client)
        """Startup Scripts service"""
