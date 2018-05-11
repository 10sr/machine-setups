FROM nextcloud:13.0.1-fpm

COPY start.sh /
RUN chmod 755 /start.sh

CMD ["/start.sh"]
