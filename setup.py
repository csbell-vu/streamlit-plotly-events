import subprocess, os, shutil
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    """Customized setuptools install command which includes building npm."""
    
    def run(self):
        # Define the path to your npm project relative to setup.py
        npm_project_path = 'src/streamlit_plotly_events/frontend'

        # Change to the npm project directory
        os.chdir(npm_project_path)

        # Check that npm and package.json are available
        assert os.path.exists('package.json'), "package.json not found in the npm project directory."
        
        # Run npm commands
        subprocess.run(['npm', 'install'], check=True)
        subprocess.run(['npm', 'run', 'build'], check=True)

        # Optional: Clean up node_modules or other build files if they are not needed
        #if os.path.exists('node_modules'):
        #    shutil.rmtree('node_modules')
        #if os.path.exists('dist'):  # or any other build directories
        #    shutil.rmtree('dist')

        # Change back to the original setup.py directory
        os.chdir('../../../')  # Adjust according to your directory structure

        # Run standard setuptools install
        install.run(self)

setup(
    name="streamlit-plotly-events",
    version="0.0.7",
    author="Charreau Bell via Ellie Jones",
    author_email="charreau.s.bell@gmail.com via ellie@altaml.com",
    description="Responsive Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit.",
    long_description="Responsive Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit.",
    long_description_content_type="text/plain",
    url="https://github.com/csbell-vu/streamlit-plotly-events",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    cmdclass={
        'install': CustomInstallCommand,
    },
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
        "plotly >= 4.14.3",
    ],
)
