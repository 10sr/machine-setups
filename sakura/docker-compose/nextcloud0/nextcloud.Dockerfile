FROM nextcloud:14-fpm

COPY start.sh /
RUN chmod 755 /start.sh

ENV NEXTCLOUD_UPDATE 1

CMD ["/start.sh"]
