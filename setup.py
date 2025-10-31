from setuptools import setup, find_packages

setup(
    name='rectangular_plas',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'torch',
        'kornia',
        'tqdm',

        # sort_3d_gaussians
        'pandas',
        'plyfile',
        'trimesh',

        # sort_rgb_img
        'click',
        'pillow',


        # eval/compare_plas_flas
        'opencv-python',

        # eval/flas
        'lapjv',
        'matplotlib',
        'scipy'
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
