from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="auto-a2a",
    version="1.0.0",
    author="Chongqing Taoxiang Network Technology Co., Ltd.",
    author_email="wei@taoxiang.org",
    description="Automated Multi-Agent System Builder with MCP Protocol Integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taoxiang-org/auto-a2a",
    project_urls={
        "Bug Reports": "https://github.com/taoxiang-org/auto-a2a/issues",
        "Source": "https://github.com/taoxiang-org/auto-a2a",
        "Documentation": "https://github.com/taoxiang-org/auto-a2a#readme",
        "Homepage": "https://www.taoxiang.org",
    },
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: System :: Distributed Computing",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "auto_a2a=auto_a2a.cli:cli",
        ],
    },
    package_data={
        "auto_a2a": ["templates/*.j2"],
    },
    keywords="multi-agent, MCP, automation, AI, orchestration, agent-framework",
    zip_safe=False,
)