# ToDo: Comment
FROM jbarlow83/ocrmypdf

# Folder watch config for incron
COPY ./src/10-ocr-watch /etc/incron.d/10-ocr-watch

# Make empty folders in case no mount is provided
RUN mkdir /ocr-in /ocr-out
# Make alias for later usage with my settings and languages german and english.
RUN echo 'alias ocrmypdf-eng-deu="ocrmypdf --optimize 1 -l deu+eng --clean --deskew --rotate-pages"' >> ~/.bashrc

# install incron
RUN apt-get install -y incron
# Add current user to incron
RUN echo 'root' >> /etc/incron.allow

# ENTRYPOINT ["/usr/bin/sh", "-c"]
# CMD ["/usr/sbin/incrond; while true; do sleep 1; done"]
