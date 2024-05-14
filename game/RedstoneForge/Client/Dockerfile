FROM nimmis/ubuntu:latest

#SPIGOT_HOME         default directory for SPIGOT-server
#SPIGOT_VER          default minecraft version to compile
#SPIGOT_AUTORESTART  set to yes to restart if minecraft stop command is executed
ENV CLIENT_IP=127.0.0.1 \
    CLIENT_PORT=25565 \
    CLIENT_USERNAME=HackiitBot \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8


# disable interactive functions
ENV DEBIAN_FRONTEND noninteractive

# set default java environment variable
ENV JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=1.8.0 \
    JAVA_VERSION_UPDATE=181 \
    JAVA_TYPE="" \
    JAVA_OPT=hotspot \
    JAVA_HOME=/usr/lib/jvm/default-jvm \
    PATH=${PATH}:/usr/lib/jvm/default-jvm/bin/

# add extra files needed
COPY rootfs /

RUN chmod +x /waitjava.sh && \
    chmod +x /etc/init.d/bot


RUN apt-get update && \
    # Make info file about this build
    printf "Build date: %s\n"  `date -u +"%Y-%m-%dT%H:%M:%SZ"` > /etc/BUILDS/spigot && \

    # install application
    apt-get install -y wget git jq && \

    # Make special user for minecraft to run in
    /usr/sbin/useradd -s /bin/bash -d /home/minecraft -m minecraft && \

    # get name of dist
    # export CNAME=$(cat /etc/os-release | grep UBUNTU_CODENAME | cut -d = -f 2) && \

    # req. packages
    apt-get install -y wget apt-transport-https gnupg && \

    # create java directory
    mkdir -p /usr/lib/jvm/ && \

    # download jdk and unpack in /usr/lib/jvm
    # Change the url to a vulnerable jdk
    curl -L "https://www.dropbox.com/scl/fi/ohy6s1xy5daucc4s59zlc/jdk-8u20-linux-x64.tar.gz?rlkey=ne9j0v0xgo9q9c0byvdr9xsla&dl=1" | tar xz -C /usr/lib/jvm/ && \

    # set compatible home path
    ln -s /usr/lib/jvm/jdk1.8.0_20/ /usr/lib/jvm/default-jvm && \
    ln -s /usr/lib/jvm/default-jvm/bin/java /usr/bin/java && \

    chmod a-w /home/minecraft/ && \


    # remove apt cache from image
    apt-get clean all 


