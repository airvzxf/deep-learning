FROM tensorflow/tensorflow:latest-gpu

ARG UID=1000
ARG GID=1000
ARG USER_NAME="generic-user"
ARG GROUP_NAME="generic-group"

RUN groupadd --gid "${GID}" --non-unique "${GROUP_NAME}"
RUN useradd --uid "${UID}" --gid "${GID}" --non-unique --create-home "${USER_NAME}"
USER "${USER_NAME}"

WORKDIR "/home/${USER_NAME}/code"

COPY requirements.txt .
ENV PATH="/home/${USER_NAME}/.local/bin:${PATH}"
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
