from setuptools import setup, find_packages

setup(
    name="discord_pagination",
    version="0.1",
    packages=find_packages(),
    description="A Python library for creating dynamic paginated embeds in Discord bots using the discord.py library.",
    author="BosonsHiggs",
    url="https://github.com/BosonsHiggs/discord_pagination",
    install_requires=["discord.py>=2.0"],
    python_requires=">=3.8",
)