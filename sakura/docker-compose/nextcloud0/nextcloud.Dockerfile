FROM nextcloud:14-fpm

COPY start.sh /
RUN chmod 755 /start.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start.sh"]
