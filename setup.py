from setuptools import setup, Extension, find_packages
setup(
    name="nubcrypt",
    version="0.0.1",
    description="Data encryption",
    author="Anggi Kharisma Putra",
    author_email="anggikharismaputra@gmail.com",
    packages = find_packages(),
    setup_requires=["cython"],
    ext_modules= [
        Extension(
            'nubcrypt.core._core',
            sources=["nubcrypt/core/_core.pyx"]
        )
    ],
)
