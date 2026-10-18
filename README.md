# INF 345 Notes API

A small Python/Flask HTTP service, continued from Week 3. Notes are kept in
memory and reset when the process restarts; no database is required.

| Method | Path | Result |
| --- | --- | --- |
| GET | `/` | API greeting |
| GET | `/healthz` | HTTP 200 and `{"status":"ok"}` |
| GET | `/notes` | List notes |
| POST | `/notes` | Create a note from `{"text":"Learn Docker"}` |
| DELETE | `/notes/<id>` | Delete a note |

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./scripts/run.sh
```

The app listens on `0.0.0.0` and reads `PORT` from the environment, defaulting
to `8080`. For another port: `PORT=9090 ./scripts/run.sh`.

## Test

```bash
./scripts/test.sh
```

Five real HTTP tests cover the greeting, health, listing, creating and deleting
notes. Successful output ends with `TESTS: 5/5`; any failing test exits nonzero.
The CI workflow runs these tests on pushes to main and on pull requests.

## Week 5: build and run in Docker

From the repository root:

```bash
docker run --rm hello-world
docker build --check .
docker build -t app:dev .
docker run -d --rm --name notes-api -e PORT=9000 -p 127.0.0.1:8080:9000 app:dev
curl --fail http://localhost:8080/healthz
docker logs notes-api
docker image inspect --format '{{.Config.User}}' app:dev
docker run --rm app:dev id
docker image inspect --format '{{.Os}}/{{.Architecture}}' app:dev
docker run --rm app:dev bash scripts/test.sh
docker stop notes-api
```

The same image works with any unprivileged `PORT`, without rebuilding. Match
the right-hand port in `-p HOST:CONTAINER` to `PORT`. `EXPOSE 8080` documents
the default; it does not publish a port. Without `-e PORT=...`, the container
uses 8080. The Flask server is suitable for this course lab; it is not a
production WSGI deployment.

### Why the Dockerfile is written this way

1. **Dependency file first:** copying `requirements.txt` and running `pip install`
   before `COPY . .` gives dependencies a separate cached layer. Editing
   `app.py` only rebuilds the source layer; changing requirements reinstalls
   dependencies. Versions are pinned and pip's download cache is omitted.
2. **Non-root user:** `USER 1000:1000` runs the app with an unprivileged numeric
   user and group. Without it the Python base image would run the app as root,
   granting unnecessary privileges inside the container.
3. **Brackets in CMD:** the exec form starts Python directly as PID 1, without
   a shell wrapper. Docker's stop signal reaches the application process.
   The local runner uses `exec` for the same reason.

The tagged `python:3.14-slim` runtime has no compiler toolchain. `.dockerignore`
keeps Git history, CI configuration, local dependencies, secrets and temporary
files out of the build context. No secret is needed to build or run the image.

### Prove the dependency cache

```bash
printf '\n# cache test\n' >> app.py
docker build --progress=plain -t app:cache-test .
git restore app.py
```

The `RUN pip install ...` step must say `CACHED`, while `COPY . .` runs again.
Only run the restore command when `app.py` has no other uncommitted edits.

### Image CI

`.github/workflows/image.yml` checks and builds the Dockerfile, shows layers,
size and CPU architecture, verifies UID/GID and the 500 MB limit, runs all five
tests inside the image, and calls the running API on `PORT=9123`. Failure logs
are retained and the test container is cleaned up. The workflow builds on
Ubuntu 24.04 (amd64); a local Apple Silicon build is arm64.

Week 5 builds and tests the image. Publishing to GHCR and the SHA-tagged image
belong to Week 6 and are required for the later M3 milestone.
