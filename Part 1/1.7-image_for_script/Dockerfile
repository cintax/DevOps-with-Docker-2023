# Start from the ubuntu:20.04 image
FROM ubuntu:20.04

# Use /usr/src/app as our workdir. The following instructions will be executed in this location.
WORKDIR /usr/src/app

# Copy the webpull.sh file from this location to /usr/src/app/ creating /usr/src/app/webpull.sh
COPY webpull.sh .

# Alternatively, if we skipped chmod earlier, we can add execution permissions during the build.
RUN chmod +x webpull.sh

# Execute a command with `/bin/sh -c` prefix.
RUN apt-get update && apt-get -y install curl

# When running docker run the command will be ./hello.sh
CMD ./webpull.sh
