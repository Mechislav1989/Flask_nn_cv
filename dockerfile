FROM python:3.8.8-slim-buster

MAINTAINER Mechislav

COPY ./requirements.txt /MMNIST/requirements.txt

WORKDIR /MMNIST


# ENV HDF5_MINOR_REL       hdf5-1.8.16 
# ENV HDF5_SRC_URL   http://www.hdfgroup.org/ftp/HDF5/releases                  
# # RUN cd /tmp                                                                        ; \ 
#     echo "Getting: ${HDF5_SRC_URL}/${HDF5_MINOR_REL}/src/${HDF5_MINOR_REL}.tar"                ; \ 
#     wget ${HDF5_SRC_URL}/${HDF5_MINOR_REL}/src/${HDF5_MINOR_REL}.tar                           ; \ 
#     tar -xvf ${HDF5_MINOR_REL}.tar --directory /usr/local/src                      ; \
#     rm ${HDF5_MINOR_REL}.tar                                                       ; \
#     cd /usr/local/src/${HDF5_MINOR_REL}                                            ; \
#     ./configure --prefix=/usr/local/hdf5                                           ; \
#     make                                                                           ; \
#     make check                                                                     ; \
#     make install                                                                   ; \
#     make check-install                                                             ; \
#     for f in /usr/local/hdf5/bin/* ; do ln -s $f /usr/local/bin ; done             ; \
#     pip install numpy                                                              ; \  
#     cd /usr/local/src                                                              ; \
#     git clone https://github.com/h5py/h5py.git                                     ; \
#     cd h5py                                                                        ; \
#     export HDF5_DIR=/usr/local/hdf5  

# RUN apk add --no-cache py3-numpy
# RUN apk add make automake gcc g++ subversion python3-dev
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install -r requirements.txt

# RUN apk add --no-cache bash

ENTRYPOINT ('python')
CMD ('flask_app3.py') 

EXPOSE 80 