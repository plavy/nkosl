#!/bin/bash
set -euo pipefail


flask db upgrade

gunicorn -b 0.0.0.0:80 app:nkosl_app

