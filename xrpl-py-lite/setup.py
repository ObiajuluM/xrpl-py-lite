import setuptools

with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="xrpl-lite-py",
    version="0.0.1",
    author="Obiajulu_M",
    author_email="oambanefo@outlook.com",
    packages=setuptools.find_packages(),
    description="A lite XRPL SDK for python devs, to focus on developing real world applications, while keeping out the ambiguity",
    long_description=description,
    long_description_content_type="text/markdown",
    url="",
    license='MIT',
    python_requires='>=3.8',
    install_requires=["xrpl-py", "cryptoconditions"])
