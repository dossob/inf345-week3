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

    def test_create_note(self):
        data = json.dumps({"text": "Test note"}).encode()

        request = urllib.request.Request(
            "http://127.0.0.1:9091/notes",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        response = urllib.request.urlopen(request)
        result = json.loads(response.read())

        self.assertEqual(response.status, 201)
        self.assertEqual(result["text"], "Test note")

    def test_delete_note(self):
        data = json.dumps({"text": "Delete me"}).encode()

        create_request = urllib.request.Request(
            "http://127.0.0.1:9091/notes",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        create_response = urllib.request.urlopen(create_request)
        note = json.loads(create_response.read())

        note_id = note["id"]

        delete_request = urllib.request.Request(
            f"http://127.0.0.1:9091/notes/{note_id}",
            method="DELETE"
        )

        response = urllib.request.urlopen(delete_request)
        result = json.loads(response.read())

        self.assertEqual(response.status, 200)
        self.assertEqual(result["message"], "Note deleted")


if __name__ == "__main__":
    unittest.main()
