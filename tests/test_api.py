import unittest
import urllib.request
import json
import subprocess
import time
import os


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        env = os.environ.copy()
        env["PORT"] = "9091"

        cls.server = subprocess.Popen(
            ["./scripts/run.sh"],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.server.terminate()
        cls.server.wait()

    def get(self, path):
        response = urllib.request.urlopen(
            "http://127.0.0.1:9091" + path
        )
        return response.status, json.loads(response.read())

    def test_home(self):
        status, data = self.get("/")
        self.assertEqual(status, 200)
        self.assertIn("message", data)

    def test_health(self):
        status, data = self.get("/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(data["status"], "ok")

    def test_notes(self):
        status, data = self.get("/notes")
        self.assertEqual(status, 200)
        self.assertIsInstance(data, list)


if __name__ == "__main__":
    unittest.main()
