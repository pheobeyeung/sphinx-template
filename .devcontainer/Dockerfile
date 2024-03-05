ARG VARIANT=3-bullseye
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

RUN set -ex; \
   apt-get update -y; \
   export DEBIAN_FRONTEND=noninteractive; \
   apt-get -y install --no-install-recommends bash-completion \
   tig \
   texlive \
   texlive-latex-extra \
   latexmk \
   git \
   weasyprint \
   tex-gyre
