import json
import os
import unittest
import tempfile

import transcriptic.config

class ConnectionInitTests(unittest.TestCase):
    def test_inits_valid(self):
        with tempfile.NamedTemporaryFile() as config_file:

            with open(config_file.name, 'w') as f:
                json.dump(
                    {
                        "email": "somebody@transcriptic.com",
                        "token": "foobarinvalid",
                        "organization_id": "transcriptic",
                        "api_root": "http://foo:5555",
                        "analytics": True,
                        "user_id": "ufoo2",
                        "feature_groups": [
                            "can_submit_autoprotocol",
                            "can_upload_packages"
                        ]
                    },
                    f
                )

            transcriptic.config.Connection.from_file(config_file.name)

    def test_inits_invalid(self):
        with tempfile.NamedTemporaryFile() as config_file:    
            with open(config_file.name, 'w') as f:
                json.dump(
                    {
                        "email": "somebody@transcriptic.com",
                        # "token": "foobarinvalid",  (missing token)
                        "organization_id": "transcriptic",
                        "api_root": "http://foo:5555",
                        "analytics": True,
                        "user_id": "ufoo2",
                        "feature_groups": [
                            "can_submit_autoprotocol",
                            "can_upload_packages"
                        ]
                    },
                    f
                )

            # TODO(meawoppl) - assertRaisesRegexp deprecated in py3
            # Move it to assertRaisesRegex()
            with self.assertRaisesRegexp(OSError, "token"):
                transcriptic.config.Connection.from_file(config_file.name)