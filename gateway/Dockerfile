FROM kong/kong-gateway:3.4.3.12

USER root

# Install required tools
RUN cat /etc/*release
RUN apt-get update && apt-get install -y build-essential zsh unzip wget git

# Clone the repository
RUN git clone https://github.com/jeromeguillaume/kong-plugin-soap-xml-handling.git

# Copy the plugin files from the cloned repository to Kong's plugin directory
RUN cp -r /kong-plugin-soap-xml-handling/kong/plugins/soap-xml-handling-lib /usr/local/share/lua/5.1/kong/plugins/soap-xml-handling-lib && \
    cp -r /kong-plugin-soap-xml-handling/kong/plugins/soap-xml-response-handling /usr/local/share/lua/5.1/kong/plugins/soap-xml-response-handling && \
    cp -r /kong-plugin-soap-xml-handling/kong/plugins/soap-xml-request-handling /usr/local/share/lua/5.1/kong/plugins/soap-xml-request-handling

# Set environment variables for library path and plugins
ENV KONG_PLUGINS=bundled,soap-xml-request-handling

