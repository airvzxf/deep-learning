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

# If the follow lines return and error, please check that the file exist.
#RUN find / -iname "*oracle.py*" 2>/dev/null || true

RUN sed -i "s/self\._max_collisions\ =\ 20/self\._max_collisions\ =\ 1000000/g" \
    "/home/${USER_NAME}/.local/lib/python3.8/site-packages/keras_tuner/engine/oracle.py"

RUN cat "/home/${USER_NAME}/.local/lib/python3.8/site-packages/keras_tuner/engine/oracle.py" | \
    grep -ins --color=always "self._max_collisions"
