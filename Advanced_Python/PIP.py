# Some important pip instructions

# python --version, shows version of python

# INSTALLING PACKAGES
# pip install "blabla", to install blabla package
# pip install blabla==1.14.1, install 1.14.1 version
# pip install blabla>1,<2, install greater than 1 and lower than 2
# pip install blabla~=1.4.2, install any version of 1.4 it can be grater than 1.4.2 but not grater than 1.4


# UPGRADING PACKAGES
# pip install --upgrade blabla

# To install packages that is for user
# pip install --user blabla

# Install from url
# pip install --index-url http://my.package.repo/simple/ SomeProject

# Install from github
# e is for editable mode! can install without -e
# pip install -e git+https://git.repo/some_pkg.git

# Install from path (locally)
# pip install -e <path> or pip install <path>

# Install from source code
# pip install ./downloads/SomeProject-1.0.4.tar.gz

# To ensure pip, setuptools are up to date
# python -m pip install --upgrade pip setuptools wheel

# To create a virtual environment
# python3 -m venv tutorial_env
# source tutorial_env/bin/activate
# This will create a new virtual environment in the tutorial_env subdirectory,
# and configure the current shell to use it as the default python environment.

# python3 -m venv <DIR>
# source <DIR>/bin/activate

# To remove a package
# pip uninstall blabla
