# Use an official Python runtime as a parent image
FROM python:3
# Set the working directory to /app
WORKDIR /opt/app

# Copy the current directory contents into the container at /app
ADD . /opt/app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt&& \
    pip install merlinwf



# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]


# Start from the official Ubuntu Bionic (18.04 LTS) image
FROM ubuntu:bionic

# Install any extra things we might need
RUN apt-get update \
	&& apt-get install -y \
		vim \
		ssh \
		sudo \
		wget \
		software-properties-common ;\
		rm -rf /var/lib/apt/lists/*

# Create a new user called foam
RUN useradd --user-group --create-home --shell /bin/bash foam ;\
	echo "foam ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Install OpenFOAM v6 (without ParaView)
# including configuring for use by user=foam
# plus an extra environment variable to make OpenMPI play nice
RUN sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -" ;\
	add-apt-repository http://dl.openfoam.org/ubuntu ;\
	apt-get update ;\
	apt-get install -y --no-install-recommends openfoam6 ;\
	rm -rf /var/lib/apt/lists/* ;\
	echo "source /opt/openfoam6/etc/bashrc" >> ~foam/.bashrc ;\
	echo "export OMPI_MCA_btl_vader_single_copy_mechanism=none" >> ~foam/.bashrc

# set the default container user to foam
USER foam
COPY --from=0 /opt/app .
