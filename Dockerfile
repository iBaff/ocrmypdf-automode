# ToDo: Comment
FROM jbarlow83/ocrmypdf
# install python3 inotify_simple
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-distutils
RUN pip3 install inotify_simple

# Make alias for later usage with my settings and languages german and english.
RUN echo 'alias ocrmypdf-eng-deu="ocrmypdf --optimize 1 -l deu+eng --clean --deskew --rotate-pages"' >> ~/.bashrc

COPY src/ /app/

# -u (https://stackoverflow.com/a/29745541/1781686)
ENTRYPOINT ["/usr/bin/python3", "-u"]
CMD ["/app/automode.py"]
