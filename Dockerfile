FROM kong/kong-gateway:3.4.3.12

# Copy the plugin directories to their respective locations in Kong
COPY ./kong/plugins/soap-xml-handling-lib /usr/local/share/lua/5.1/kong/plugins/soap-xml-handling-lib
COPY ./kong/plugins/soap-xml-response-handling /usr/local/share/lua/5.1/kong/plugins/soap-xml-response-handling
COPY ./kong/plugins/soap-xml-request-handling /usr/local/share/lua/5.1/kong/plugins/soap-xml-request-handling

# Set up the necessary directory for Saxon libraries
COPY ./kong/saxon/so/amd64 /usr/local/lib/kongsaxon

# Set environment variables for library path and plugins
ENV LD_LIBRARY_PATH=/usr/local/lib/kongsaxon
ENV KONG_PLUGINS=bundled,soap-xml-request-handling
