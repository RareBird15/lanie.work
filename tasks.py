"""Invoke tasks for building, serving, and publishing the Pelican static site."""

# pyright: basic
from __future__ import annotations

import os
import shlex
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path
from typing import TYPE_CHECKING, Any

from invoke.main import program
from invoke.tasks import task
from livereload import Server
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

# Put type-only imports in this block
if TYPE_CHECKING:
    from invoke.context import Context

OPEN_BROWSER_ON_SERVE = True
SETTINGS_FILE_BASE = "pelicanconf.py"

# Tell Pylance this is a dictionary with string keys and Any values
SETTINGS: dict[str, Any] = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG: dict[str, Any] = {
    "settings_base": SETTINGS_FILE_BASE,
    "settings_publish": "publishconf.py",
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    "host": "localhost",
    "port": 8000,
}

LOCAL_URL = f"http://{CONFIG['host']}:{CONFIG['port']}"


@task
def clean(_c: Context) -> None:
    """Remove generated files."""
    deploy_path = Path(CONFIG["deploy_path"])
    if deploy_path.is_dir():
        shutil.rmtree(deploy_path)
        deploy_path.mkdir(parents=True)


@task
def build(_c: Context) -> None:
    """Build local version of site."""
    pelican_run(f"-s {CONFIG['settings_base']}")


@task
def rebuild(_c: Context) -> None:
    """`build` with the delete switch."""
    pelican_run(f"-d -s {CONFIG['settings_base']}")


@task
def regenerate(_c: Context) -> None:
    """Automatically regenerate site upon file modification."""
    pelican_run(f"-r -s {CONFIG['settings_base']}")


@task
def serve(_c: Context) -> None:
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)."""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"],
        (CONFIG["host"], CONFIG["port"]),
        ComplexHTTPRequestHandler,
    )
    if OPEN_BROWSER_ON_SERVE:
        webbrowser.open(LOCAL_URL)
    sys.stderr.write(f"Serving at {LOCAL_URL} ...\n")
    server.serve_forever()


@task
def reserve(_c: Context) -> None:
    """`build`, then `serve`."""
    build(_c)
    serve(_c)


@task
def preview(_c: Context) -> None:
    """Build production version of site."""
    pelican_run(f"-s {CONFIG['settings_publish']}")


@task
def livereload(_c: Context) -> None:
    """Automatically reload browser tab upon file modification."""

    def cached_build() -> None:
        env = os.environ.copy()
        env["CACHE_CONTENT"] = "true"
        env["LOAD_CONTENT_CACHE"] = "true"
        cmd = f"-s {CONFIG['settings_base']}"
        pelican_run(cmd, env=env)

    cached_build()
    server = Server()
    theme_path = str(SETTINGS["THEME"])
    watched_globs = [
        CONFIG["settings_base"],
        f"{theme_path}/templates/**/*.html",
    ]
    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_glob = f"{SETTINGS['PATH']}/**/*{extension}"
        watched_globs.append(content_glob)
    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file_glob = f"{theme_path}/static/**/*{extension}"
        watched_globs.append(static_file_glob)
    for glob in watched_globs:
        server.watch(glob, cached_build)
    if OPEN_BROWSER_ON_SERVE:
        webbrowser.open(LOCAL_URL)
    server.serve(host=CONFIG["host"], port=CONFIG["port"], root=CONFIG["deploy_path"])


@task
def publish(_c: Context) -> None:
    """Publish to production via rsync."""
    pelican_run(f"-s {CONFIG['settings_publish']}")


def pelican_run(cmd: str, env: dict[str, str] | None = None) -> None:
    """Run the Pelican static site generator with the given command."""
    cmd += " " + program.core.remainder  # allows to pass-through args to pelican
    pelican_executable = shutil.which("pelican")
    if pelican_executable is None:
        raise RuntimeError("Could not find 'pelican' executable in PATH.")  # noqa: EM101, TRY003
    if env is not None:
        subprocess.run(  # noqa: S603
            [pelican_executable, *shlex.split(cmd)],
            env=env,
            check=True,
        )
    else:
        pelican_main(shlex.split(cmd))
