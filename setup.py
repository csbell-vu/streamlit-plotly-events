import setuptools

setuptools.setup(
    name="streamlit-plotly-events",
    version="0.0.7",
    author="Charreau Bell via Ellie Jones",
    author_email="charreau.s.bell@gmail.com via ellie@altaml.com",
    description="Responsive Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit.",
    long_description="Responsive Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit.",
    long_description_content_type="text/plain",
    url="https://github.com/csbell-vu/streamlit-plotly-events",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
        "plotly >= 4.14.3",
    ],
)
